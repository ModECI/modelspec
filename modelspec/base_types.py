import collections
import json
import yaml
import sys

import numpy as np
import attr
import cattr

from typing import Optional, List, Dict, Any, Union, Tuple, Type, TypeVar, Callable, Iterable

# If we running python version 3.7 or lower, we need to using typing_compat
if sys.version_info < (3, 8):
    from typing_compat import get_args, get_origin
else:
    from typing import get_args, get_origin

from typing import Union, List, Dict, Any

from attr import has, field, fields
from attr.validators import optional, instance_of, in_

from cattr.gen import make_dict_unstructure_fn, make_dict_structure_fn, override
from cattr.preconf.pyyaml import make_converter as make_yaml_converter


from collections import OrderedDict
from tabulate import tabulate

verbose = False

MARKDOWN_FORMAT = "markdown"
RST_FORMAT = "rst"

DICT_FORMAT = "dict"


class EvaluableExpression(str):
    def __init__(self, expr):
        self.expr = expr


# Union of types that are allowed as value expressions for parameters.
ValueExprType = Union[EvaluableExpression, List, Dict, np.ndarray, int, float, str]
value_expr_types = (EvaluableExpression, list, dict, np.ndarray, int, float, str)


def print_(text, print_it=False):
    """
    Print a message preceded by modelspec, only if print_it=True
    """
    prefix = "modelspec >>> "
    if not isinstance(text, str):
        text = ("%s" % text).decode("ascii")
    if print_it:
        print("%s%s" % (prefix, text.replace("\n", "\n" + prefix)))


def print_v(text):
    """
    Print a message preceded by modelspec always
    """
    print_(text, True)


# A general purpose converter for all model spec objects
converter = cattr.Converter()

# A setup an additional converter to apply when we are serializing using PyYAML.
# This handles things like tuples as lists.
yaml_converter = make_yaml_converter()

# A simple converter that handles only value expressions.
value_expr_converter = cattr.Converter()


@attr.define(eq=False)
class Base:
    """
    Base class for all object in a model specification. Any object should inherit from this class.

        Args:
            notes: Human readable notes.
    """

    notes: Optional[str] = attr.ib(kw_only=True, default=None, validator=optional(instance_of(str)))

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Base object to a nested dict structure."""

        d = converter.unstructure(self)

        # If this object has an id attribute, by default lets serialize it within a dict with the id as the key, even if
        # it is a single object.
        if 'id' in [f.name for f in attr.fields(self.__class__)] and 'id' in d.keys():
            # Drop the id field
            del d["id"]
            return {self.id: d}
        else:
            return d


    def to_json(self) -> str:
        """
        Convert the Base object to a JSON string representation.
        """
        return json.dumps(self.to_dict(), indent=4)

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Base":
        """Instantiate an Base object from a dictionary"""

        # If this object has an id attribute, it may have been serialized within a dict with the id as the key, even if
        # it is a single object.
        if 'id' in [f.name for f in attr.fields(cls)] and 'id' not in d.keys():

            keys = list(d.keys())
            if len(keys) == 0:
                raise ValueError(f"Cannot deserialize Base modelspec object ({cls}) because it is empty.")

            # Get the first key, this should be the id
            id_val = keys[0]

            return converter.structure({"id": id_val, **d[id_val]}, cls)
        else:
            return converter.structure(d, cls)

    @classmethod
    def from_json(cls, json_str: str) -> "Base":
        """Instantiate an MDF object from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_json_file(
        self, filename: Optional[str] = None, include_metadata: bool = True
    ) -> str:
        """Convert the MDF model to JSON format and save to a file.

         .. note::
            JSON is standard file format uses human-readable text to store and transmit data objects consisting of attribute–value pairs and arrays

        Args:
            filename: The name of the file to save. If None, use the  (.json extension)
            include_metadata: Contains contact information, citations, acknowledgements, pointers to sample data,
                              benchmark results, and environments in which the specified model was originally implemented
        Returns:
            The name of the generated JSON file
        """

        if filename is None:
            filename = f"{self.id}.json"

        with open(filename, "w") as outfile:
            json.dump(self.to_dict(), outfile, indent=4)

        return filename

    def to_yaml_file(self, filename: str, include_metadata: bool = True) -> str:
        """Convert file in MDF format to yaml format

        Args:
            filename: File in MDF format (Filename extension: .mdf )
            include_metadata: Contains contact information, citations, acknowledgements, pointers to sample data,
                              benchmark results, and environments in which the specified model was originally implemented
        Returns:
            The name of the generated yaml file
        """

        if filename is None:
            filename = f"{self.id}.yaml"

        with open(filename, "w") as outfile:

            # We need to setup another
            yaml.dump(yaml_converter.unstructure(self.to_dict()), outfile, sort_keys=False)

        return filename

    @classmethod
    def from_file(cls, filename: str) -> "Model":
        """
        Create a :class:`.Model` from its representation stored in a file. Auto-detect the correct deserialization code
        based on file extension. Currently supported formats are; JSON(.json) and YAML (.yaml or .yml)

        Args:
            filename: The name of the file to load.

        Returns:
            An MDF :class:`.Model` for this file.
        """
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            return cls.from_yaml_file(filename)
        elif filename.endswith(".json"):
            return cls.from_json_file(filename)
        else:
            raise ValueError(
                f"Cannot auto-detect MDF serialization format from filename ({filename}). The filename "
                f"must have one of the following extensions: .json, .yml, or .yaml."
            )

    @classmethod
    def from_json_file(cls, filename: str) -> "Model":
        """
        Create a :class:`.Model` from its JSON representation stored in a file.

        Args:
            filename: The file from which to load the JSON data.

        Returns:
            An MDF :class:`.Model` for this JSON
        """
        with open(filename) as infile:
            d = json.load(infile)
            return cls.from_dict(d)

    @classmethod
    def from_yaml_file(cls, filename: str) -> "Model":
        """
        Create a :class:`.Model` from its YAML representation stored in a file.

        Args:
            filename: The file from which to load the YAML data.

        Returns:
            An MDF :class:`.Model` for this YAML
        """
        with open(filename) as infile:
            d = yaml.safe_load(infile)
            d = yaml_converter.structure(d, Dict)
            return cls.from_dict(d)

    def get_child(self, id: str, type_: str) -> Any:
        """
        Get a child object from the model specification.

        Args:
            id: The unique string identifier of the child object.
            type_: The type of the child object. Must be an attribute name that contains a list of child objects with
                id attributes..

        Returns:
            The child object. If the child object is not found, None is returned.
        """

        # We can't find the container for this type of child object.
        if not type_ in [f.name for f in attr.fields(self.__class__)]:
            return None

        children = self.__getattribute__(type_)

        # Find the child object with the given id.
        for c in children:
            if c.id == id:
                return c

        # We didn't find the child object.
        return None


class NetworkReader:
    pop_locations = {}

    def parse(self, handler):
        raise Exception("This needs to be implemented...")

    def get_locations(self):
        return self.pop_locations

# Below are a set of structure and unstructure hooks needed to help cattr serialize and deserialize from JSON the
# non-standard things.

def _unstructure_value_expr(o):
    """Handle unstructuring of value expressions from JSON"""
    try:
        # If this is an np.ndarray type, it should have a tolist
        return o.tolist()
    except AttributeError:
        return converter.unstructure(o)


def _structure_value_expr(o, t):
    """Handle re-structuring of value expressions from JSON"""

    # Don't convert scalars to arrays
    if np.isscalar(o):
        return o

    # # Try to turn it into a numpy array
    # arr = np.array(o)
    #
    # # Make sure the dtype is not object or string, we want to keep these as lists
    # if arr.dtype.type not in [np.object_, np.str_]:
    #     return arr

    return o


# Register a structure and unstructure hook to handle value expressions that
# can either be str or Dict (not sure if this should be allowed but ACT-R examples
# depend on this feature). Value expressions should probably become their own
# type later down the line. We want a converter that just handles value expressions
# and we also want to add hooks for this to the general converter.
# value_expr_converter.register_structure_hook(
#     Optional[ValueExprType], _structure_value_expr
# )
value_expr_converter.register_unstructure_hook(
    Optional[ValueExprType], _unstructure_value_expr
)
converter.register_unstructure_hook(Optional[ValueExprType], _unstructure_value_expr)
converter.register_structure_hook(Optional[ValueExprType], _structure_value_expr)
converter.register_unstructure_hook(ValueExprType, _unstructure_value_expr)
converter.register_structure_hook(ValueExprType, _structure_value_expr)


# Setup a hook factory for any Base class so we don't serialize attributes whose
# current value is the default value.
def _base_unstruct_hook_factory(cl):
    """Generate an unstructure hook for the a class that inherits from Base"""

    # Generate overrides for all fields so that we omit default values from serialization
    field_overrides = {
        a.name: override(omit_if_default=True)
        for a in fields(cl)
        if a.metadata.get("omit_if_default", True)
    }

    return make_dict_unstructure_fn(cl, converter, **field_overrides)


# Most of the code below is needed to handle serialization and deserialization of lists of
# Base objects that have ids as dicts where the keys are the ids.
def _base_struct_hook_factory(cl):
    """
    This is a very simple modification to cattr.Converter.structure_attrs_fromdict. The only
    difference is that we give the id value a default value of empty string when structuring.
    This is because objects with id are serialized without id when they are stored in a list.
    The id is stored in the key of a dictionary.
    """

    def _structure_base(obj, t):
        """Instantiate a subclass of Base class from a mapping (dict)."""

        conv_obj = {"id": ""}
        for a in fields(cl):  # type: ignore
            name = a.name

            try:
                val = obj[name]
            except KeyError:
                continue

            if name[0] == "_":
                name = name[1:]

            conv_obj[name] = converter._structure_attribute(a, val)

        return cl(**conv_obj)

    return _structure_base


# Register the structure and unstructure hooks for collections of Base classes.
def _unstructure_list_base(cl):
    """Serialize list of Base objects as dicts if all of their elements have ids"""

    def f(obj_list):
        try:
            # If all the elements of this list have id's, we can serialize them as a dict.
            d = {o.id: converter.unstructure(o) for o in obj_list}

            # Remove the ids from each element since they are stored in the dict's keys now.
            for id, objd in d.items():
                del objd["id"]

            return d

        except AttributeError:
            return obj_list

    return f


def _structure_list_mdfbase(cl):
    """Deserialize list of dict of Base objects as a list if all of their elements have ids"""
    mdf_class = get_args(cl)[0]

    def f(obj_dict, t):
        try:
            obj_list = [converter.structure(v, mdf_class) for v in obj_dict.values()]

            # Give each object the id that is its key in the dict.
            for id, obj in zip(obj_dict.keys(), obj_list):
                obj.id = id

            return obj_list

        except AttributeError:
            return obj_dict

    return f


def _is_list_base(cl):
    """
    Check if a class is a list of Base objects. These will be serialized as dicts if the underlying class has an id
    attribute.
    """
    return get_origin(cl) == list and issubclass(get_args(cl)[0], Base)


converter.register_unstructure_hook_factory(_is_list_base, _unstructure_list_base)
converter.register_unstructure_hook_factory(
    lambda cl: issubclass(cl, Base), _base_unstruct_hook_factory,
)

converter.register_structure_hook_factory(_is_list_base, _structure_list_mdfbase)
converter.register_structure_hook_factory(
    lambda cl: issubclass(cl, Base) and "id" in [a.name for a in fields(cl)],
    _base_struct_hook_factory,
)

