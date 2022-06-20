import json
import yaml
import bson
import sys

import numpy as np
import attr
import cattr

from typing import (
    Optional,
    Tuple,
)

from docstring_parser import parse

# If we running python version 3.7 or lower, we need to using typing_compat
if sys.version_info < (3, 8):
    from typing_compat import get_args, get_origin
else:
    from typing import get_args, get_origin

from typing import Union, List, Dict, Any

from cattr.gen import make_dict_unstructure_fn, override
from cattr.preconf.pyyaml import make_converter as make_yaml_converter
from cattr.preconf.bson import make_converter as make_bson_converter

from tabulate import tabulate

verbose = False

MARKDOWN_FORMAT = "markdown"
RST_FORMAT = "rst"
DICT_FORMAT = "dict"


class EvaluableExpression(str):
    """
    EvaluableExpression is a string that can be evaluated to a value during modelspec execution. This class inherits from
    str, so it can be used as a string.
    """

    def __init__(self, expr):
        self.expr = expr


# Union of types that are allowed as value expressions for parameters.
ValueExprType = Union[EvaluableExpression, List, Dict, np.ndarray, int, float, str]
value_expr_types = (EvaluableExpression, list, dict, np.ndarray, int, float, str)


def print_(text: str, print_it: bool = False):
    """
    Print a message preceded by modelspec, only if print_it=True
    """
    prefix = "modelspec >>> "
    if not isinstance(text, str):
        text = ("%s" % text).decode("ascii")
    if print_it:
        print("{}{}".format(prefix, text.replace("\n", "\n" + prefix)))


def print_v(text: str):
    """
    Print a message preceded by modelspec always
    """
    print_(text, True)


# A general purpose converter for all model spec objects
converter = cattr.Converter()

# A setup an additional converter to apply when we are serializing using PyYAML.
# This handles things like tuples as lists.
yaml_converter = make_yaml_converter()
bson_converter = make_bson_converter()

# A simple converter that handles only value expressions.
value_expr_converter = cattr.Converter()


@attr.define(eq=False)
class Base:
    """
    Base class for all object in a model specification. Any object should inherit from this class.
    """

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Base object to a nested dict structure."""

        d = converter.unstructure(self)

        # If this object has an id attribute, by default lets serialize it within a dict with the id as the key, even if
        # it is a single object.
        if "id" in [f.name for f in attr.fields(self.__class__)] and "id" in d.keys():
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

    def to_bson(self) -> str:
        """
        Convert the Base object to a BSON string representation.
        """
        return bson.encode(self.to_dict())

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Base":
        """Instantiate an Base object from a dictionary"""

        # If this object has an id attribute, it may have been serialized within a dict with the id as the key, even if
        # it is a single object.
        if "id" in [f.name for f in attr.fields(cls)] and "id" not in d.keys():

            keys = list(d.keys())
            if len(keys) == 0:
                raise ValueError(
                    f"Cannot deserialize Base modelspec object ({cls}) because it is empty."
                )

            # Get the first key, this should be the id
            id_val = keys[0]

            return converter.structure({"id": id_val, **d[id_val]}, cls)
        else:
            return converter.structure(d, cls)

    @classmethod
    def from_json(cls, json_str: str) -> "Base":
        """Instantiate an modelspec object from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    @classmethod
    def from_bson(cls, bson_str: str) -> "Base":
        """Instantiate an modelspec object from a BSON string"""
        return cls.from_dict(bson.decode(bson_str))

    def to_json_file(
        self, filename: Optional[str] = None, include_metadata: bool = True
    ) -> str:
        """Convert the modelspec model to JSON format and save to a file.

         .. note::
            JSON is standard file format uses human-readable text to store and transmit data objects consisting of
                attribute–value pairs and arrays

        Args:
            filename: The name of the file to save. If None, use :code:`f"{self.id}.json"`
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

    def to_bson_file(self, filename: str, include_metadata: bool = True) -> str:
        """Convert modelspec format to bson format

        Args:
            filename: File in modelspec format (Filename extension: .bson )
            include_metadata: Contains contact information, citations, acknowledgements, pointers to sample data,
                              benchmark results, and environments in which the specified model was originally implemented
        Returns:
            The name of the generated bson file
        """

        if filename is None:
            filename = f"{self.id}.bson"

        with open(filename, "wb") as outfile:
            bson_data = bson.encode(
                bson_converter.unstructure(self.to_dict()),
            )
            outfile.write(bson_data)

        return filename

    def to_yaml(self, include_metadata: bool = True) -> str:
        """
        Convert the Base object to a YAML dictionary representation.

        Args:
            include_metadata: Should metadata be included in the YAML output?

        Returns:
            A YAML string representation of the object.
        """
        return yaml.dump(
            yaml_converter.unstructure(self.to_dict()), sort_keys=False, indent=4
        )

    def to_yaml_file(self, filename: str, include_metadata: bool = True) -> str:
        """Convert modelspec format to yaml format

        Args:
            filename: File in modelspec format (Filename extension: .yaml )
            include_metadata: Contains contact information, citations, acknowledgements, pointers to sample data,
                              benchmark results, and environments in which the specified model was originally implemented
        Returns:
            The name of the generated yaml file
        """

        if filename is None:
            filename = f"{self.id}.yaml"

        with open(filename, "w") as outfile:

            # We need to setup another
            yaml.dump(
                yaml_converter.unstructure(self.to_dict()),
                outfile,
                sort_keys=False,
                indent=4,
            )

        return filename

    @classmethod
    def from_file(cls, filename: str) -> "Base":
        """
        Create a :class:`.Base` from its representation stored in a file. Auto-detect the correct deserialization code
        based on file extension. Currently supported formats are; JSON(.json) and YAML (.yaml or .yml)

        Args:
            filename: The name of the file to load.

        Returns:
            An modelspec :class:`.Base` for this file.
        """
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            return cls.from_yaml_file(filename)
        elif filename.endswith(".json"):
            return cls.from_json_file(filename)
        elif filename.endswith(".bson"):
            return cls.from_bson_file(filename)
        else:
            raise ValueError(
                f"Cannot auto-detect modelspec serialization format from filename ({filename}). The filename "
                f"must have one of the following extensions: .json, .yml, or .yaml."
            )

    @classmethod
    def from_json_file(cls, filename: str) -> "Base":
        """
        Create a :class:`.Base` from its JSON representation stored in a file.

        Args:
            filename: The file from which to load the JSON data.

        Returns:
            An modelspec :class:`.Base` for this JSON
        """
        with open(filename) as infile:
            d = json.load(infile)
            return cls.from_dict(d)

    @classmethod
    def from_bson_file(cls, filename: str) -> "Base":
        """
        Create a :class:`.Base` from its BSON representation stored in a file.

        Args:
            filename: The file from which to load the BSON data.

        Returns:
            An modelspec :class:`.Base` for this BSON
        """
        with open(filename, "rb") as infile:
            data_encoded = infile.read()
            d = bson.decode(data_encoded)
            return cls.from_dict(d)

    @classmethod
    def from_yaml_file(cls, filename: str) -> "Base":
        """
        Create a :class:`.Base` from its YAML representation stored in a file.

        Args:
            filename: The file from which to load the YAML data.

        Returns:
            An modelspec :class:`.Base` for this YAML
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
        if type_ not in [f.name for f in attr.fields(self.__class__)]:
            return None

        children = self.__getattribute__(type_)

        # Find the child object with the given id.
        for c in children:
            if c.id == id:
                return c

        # We didn't find the child object.
        return None

    @property
    def definition(self) -> str:
        """
        The definition of the model.

        Returns:
            The definition of the model.
        """
        return self.__class__._parse_definition()

    @property
    def allowed_fields(self) -> Dict[str, Tuple[str, Any]]:
        """
        Get the list of allowed fields for this model.

        Returns:
            The allowed fields are returned as dict keyed by field name
                and with values of tuple with (field_description, field_type).
        """
        return self.__class__._parse_allowed_fields()

    @property
    def allowed_children(self) -> Dict[str, Tuple[str, Any]]:
        """
        Get the list of allowed children for this model. Children are defined as
        any attribute of this object that is a collection of objects that inherits from :class:`Base`.

        Returns:
            The allowed children are returned as dict keyed attribute name of the collection
                and with values of tuple with (description, type).
        """
        return self.__class__._parse_allowed_children()

    @classmethod
    def _parse_definition(cls) -> str:
        """
        Parse the definition of the model from its doc string.

        Returns:
            The definition of the model.
        """
        # Parse the docstring
        p = parse(cls.__doc__)

        # Extract the description, use the long description if available.
        # "short_description" only parse the first non-empty line and
        # "long_description" parse the rest of the docstring i.e.
        # it skips the first non-empty line and parse the rest of the docstring
        if p.long_description:
            definition = f"{p.short_description} {p.long_description}"
        else:
            definition = p.short_description
        return definition

    @classmethod
    def _parse_allowed_fields(cls) -> Dict[str, Tuple[str, Any]]:
        """
        Get the list of allowed fields for this model.

        Returns:
            The allowed fields are returned as dict keyed by field name
                and with values of tuple with (field_description, field_type).
        """
        # Parse the docstring
        p = parse(cls.__doc__)

        # Extract the description for each parameter from the docstring if available.
        field_descriptions = {p.arg_name: p.description for p in p.params}

        # Build up the old-style dict format for allowed_fields
        allowed_fields = {
            f.name: (field_descriptions.get(f.name, ""), f.type)
            for f in attr.fields(cls)
            if not cls._is_child_field(f.name)
        }

        # If this class has a parent class, add the parent's allowed fields to this class's allowed fields.
        for base_class in cls.__bases__:
            if hasattr(base_class, "allowed_fields"):
                allowed_fields.update(base_class._parse_allowed_fields())

        return allowed_fields

    @classmethod
    def _is_child_field(cls, field_name: str) -> bool:
        """
        Check if a field is a child field. A child field is an attribute that is a collection of objects
        that inherits from :class:`Base`.

        Args:
            field_name: The name of the field to check.

        Returns:
            True if the field is a child field, False otherwise.
        """
        try:
            f = attr.fields_dict(cls)[field_name]
        except KeyError:
            raise ValueError(
                f"Field '{field_name}' not found in modelspec class '{cls.__name__}'"
            )

        # Check if the type of the field is a list or dict
        collection_arg = None
        if get_origin(f.type) == list and len(get_args(f.type)) > 0:
            collection_arg = get_args(f.type)[0]
        elif get_origin(f.type) == dict and len(get_args(f.type)) > 0:
            collection_arg = get_args(f.type)[1]

        try:
            is_child = issubclass(collection_arg, Base)
        except TypeError:
            is_child = False

        return is_child

    @classmethod
    def _parse_allowed_children(cls) -> Dict[str, Tuple[str, Any]]:
        """
        Get the list of allowed children for this model. Children are defined as
        any attribute of this object that is a collection of objects that inherits from :class:`Base`.

        Returns:
            The allowed children are returned as dict keyed attribute name of the collection
                and with values of tuple with (description, type).
        """
        # Parse the docstring
        p = parse(cls.__doc__)

        # Extract the description for each parameter from the docstring if available.
        field_descriptions = {p.arg_name: p.description for p in p.params}

        # Build up the old-style dict format for allowed_children
        allowed_children = {
            f.name: (field_descriptions.get(f.name, ""), f.type)
            for f in attr.fields(cls)
            if cls._is_child_field(f.name)
        }

        # If this class has a parent class, add the parent's allowed fields to this class's allowed fields.
        for base_class in cls.__bases__:
            if hasattr(base_class, "allowed_children"):
                allowed_children.update(base_class._parse_allowed_children())

        return allowed_children

    @staticmethod
    def _is_evaluable_expression(value: Any) -> bool:
        """Helper method to check if a value is of type EvaluableExpressions"""
        if not hasattr(value, "__name__"):
            return False
        return (
            value.__name__ == "EvaluableExpression"
            or value.__name__ == "modelspec.EvaluableExpression"
        )

    @classmethod
    def _is_base_type(
        cls,
        value,
        can_be_list=False,
        can_be_dict=False,
        can_be_ndarray=False,
        can_be_none=False,
        can_be_eval_expr=False,
    ):

        import numpy

        if verbose:
            print_v(
                " > Checking type of %s, ee: %s"
                % (value, cls._is_evaluable_expression(value))
            )

        # If this is a generic type, get the actual type
        if get_origin(value):
            value = get_origin(value)

        return (
            value == int
            or value == str
            or value == bool
            or value == float
            or (can_be_list and value == list)
            or (can_be_dict and value == dict)
            or (can_be_ndarray and value == numpy.ndarray)
            or (can_be_none and value is None)
            or (can_be_eval_expr and cls._is_evaluable_expression(value))
            or value == Union
        )

    @staticmethod
    def _type_to_str(type_: Any) -> str:
        """
        Convert a Python type (or type annotation) (from :code:`typing`) to a prettier format. Also handles normal types as well.

        Args:
            type_: The type or type annotation to convert.

        Returns:
            A string with a prettier format of the type annotation.
        """

        # If the type as a __name__ attribute, use that
        if hasattr(type_, "__name__"):
            return type_.__name__

        # If its a Generic type
        elif get_origin(type_) is not None:
            if get_origin(type_) == list and len(get_args(type_)) > 0:
                return Base._type_to_str(get_args(type_)[0])
            elif get_origin(type_) == dict and len(get_args(type_)) > 0:
                return Base._type_to_str(get_args(type_)[1])
            elif get_origin(type_) == Union and len(get_args(type_)) > 0:
                return (
                    "Union["
                    + ", ".join([Base._type_to_str(arg) for arg in get_args(type_)])
                    + "]"
                )

        # Fallback to returning just the string representation. Drop any occurrence of typing
        return str(type_).replace("typing.", "")

    def generate_documentation(self, format: str = MARKDOWN_FORMAT) -> str:
        """
        Generate documentation for the modelspec object.

        Args:
            format: The format to generate the documentation in. Currently supported formats are: ['markdown', 'dict']
        """
        return self.__class__._cls_generate_documentation(format=format)

    @classmethod
    def _cls_generate_documentation(cls, format: str = MARKDOWN_FORMAT):
        """
        Generate documentation for the modelspec object.

        Args:
            format: The format to generate the documentation in. Currently supported formats are: ['markdown', 'dict']
        """

        if format == MARKDOWN_FORMAT or format == RST_FORMAT:
            doc_string = ""
        if format == DICT_FORMAT:
            doc_dict = {}

        definition = cls._parse_definition()
        allowed_fields = cls._parse_allowed_fields()
        allowed_children = cls._parse_allowed_children()

        print(f" - {cls.__name__} ({definition})")

        rst_url_format = "`%s <%s>`__"

        def insert_links(text, format=MARKDOWN_FORMAT):

            code_ref = ":code:`"
            # print("    > Converting: %s" % text)
            text2 = text
            while code_ref in text2:
                ind = text2.index(code_ref)
                ind2 = text2.index("`", ind + len(code_ref) + 1)
                pre = text2[0:ind]
                ref = text2[ind + len(code_ref) : ind2]
                post = text2[ind2 + 1 :]

                if format == MARKDOWN_FORMAT:
                    text2 = f"{pre}<b>{ref}</b>{post}"
                elif format == RST_FORMAT:
                    text2 = f"{pre}**{ref}**{post}"

            # print("    > Converted to: %s" % text2)
            text = text2

            class_ref = ":class:`"
            # print("    > Converting: %s" % text)
            text2 = text
            while class_ref in text2:
                ind = text2.index(class_ref)
                ind2 = text2.index("`", ind + len(class_ref) + 1)
                pre = text2[0:ind]
                ref = text2[ind + len(class_ref) : ind2]
                if ref[0] == "~":
                    ref = ref[1:]
                post = text2[ind2 + 1 :]
                if format == MARKDOWN_FORMAT:
                    text2 = f'{pre}<a href="#{ref.lower()}">{ref}</a>{post}'
                elif format == RST_FORMAT:
                    rr = ref
                    pp = post

                    ######################################
                    # Some hardcoded fixes for plurals...
                    if pp.startswith("s "):
                        rr += "s"
                        pp = pp[1:]
                    if pp.startswith("s."):
                        rr += "s"
                        pp = pp[1:]
                    if pp.startswith("(s)"):
                        rr += "(s)"
                        pp = pp[3:]
                    ######################################

                    text2 = f"{pre}`{rr} <#{ref.lower()}>`__{pp}"

            # print("    > Converted to: %s" % text2)
            text = text2

            if "_" not in text:
                return text
            if '"' in text:
                return text  # Assume it's a quoted string containing an underscore...
            if format == RST_FORMAT:
                return text  # No need to remove underscore for RST format

            split = text.split("_")
            text2 = ""
            for i in range(int(len(split) / 2.0)):
                pre = split[i * 2]
                type = split[i * 2 + 1]
                text2 += f'{pre}<a href="#{type.lower()}">{type}</a>'

            if int(len(split) / 2.0) != len(split) / 2.0:
                text2 += split[-1]
            return text2

        name = cls.__name__

        if format == MARKDOWN_FORMAT:
            doc_string += "## %s\n" % name
            if definition is not None:
                doc_string += "%s\n\n" % insert_links(definition)
        elif format == RST_FORMAT:
            doc_string += "{}\n{}\n{}\n".format("=" * len(name), name, "=" * len(name))
            if definition is not None:
                doc_string += "%s\n\n" % insert_links(definition, format=RST_FORMAT)
        elif format == DICT_FORMAT:
            doc_dict[name] = {}
            if definition is not None:
                doc_dict[name]["definition"] = definition

        if len(allowed_fields) > 0:
            if format == MARKDOWN_FORMAT:
                doc_string += "### Allowed parameters\n<table>"
            if format == RST_FORMAT:
                ap = "**Allowed parameters**"
                doc_string += "%s\n\n" % (ap)
                table_info = []
        if format == DICT_FORMAT:
            doc_dict[name]["allowed_parameters"] = {}

        referenced = []

        for f, (description, type_) in allowed_fields.items():
            referencable = not Base._is_base_type(
                type_, can_be_eval_expr=True, can_be_dict=True
            )
            type_str = Base._type_to_str(type_)
            print("    Allowed parameter: {} {}".format(f, (description, type_str)))

            if format == DICT_FORMAT:
                doc_dict[name]["allowed_parameters"][f] = {}
                doc_dict[name]["allowed_parameters"][f]["type"] = type_str
                doc_dict[name]["allowed_parameters"][f]["description"] = description

            elif format == MARKDOWN_FORMAT:
                doc_string += (
                    "\n  <tr>\n    <td><b>{}</b></td>\n    <td>{}</td>".format(
                        f,
                        f'<a href="#{type_str.lower()}">{type_str}</a>'
                        if referencable
                        else type_str,
                    )
                )
                doc_string += "\n    <td><i>%s</i></td>\n </tr>\n\n" % (
                    insert_links(description)
                )

            elif format == RST_FORMAT:
                n = "**%s**" % f
                t = "{}".format(
                    rst_url_format % (type_, "#" + type_str.lower())
                    if referencable
                    else type_str,
                )
                d = "%s" % (insert_links(description, format=RST_FORMAT))
                table_info.append([n, t, d])

            if referencable:
                referenced.append(type_)

        if len(allowed_fields) > 0:
            if format == MARKDOWN_FORMAT:
                doc_string += "\n</table>\n\n"
            elif format == RST_FORMAT:
                doc_string += "%s\n\n" % (
                    tabulate(
                        table_info,
                        ["Allowed field", "Data Type", "Description"],
                        tablefmt="rst",
                    )
                )

        if len(allowed_children) > 0:
            if format == MARKDOWN_FORMAT:
                doc_string += "### Allowed children\n<table>"
            elif format == RST_FORMAT:
                ap = "**Allowed children**"
                doc_string += "%s\n\n" % (ap)
                table_info = []
            elif format == DICT_FORMAT:
                doc_dict[name]["allowed_children"] = {}

        for c, (description, type_) in allowed_children.items():
            type_str = Base._type_to_str(type_)
            print("    Allowed child: {} {}".format(c, (description, type_str)))

            referencable = not Base._is_base_type(type_, can_be_dict=True)

            if format == DICT_FORMAT:
                doc_dict[name]["allowed_children"][c] = {}
                doc_dict[name]["allowed_children"][c]["type"] = type_str
                doc_dict[name]["allowed_children"][c]["description"] = allowed_children[
                    c
                ][0]

            elif format == MARKDOWN_FORMAT:
                doc_string += (
                    "\n  <tr>\n    <td><b>{}</b></td>\n    <td>{}</td>".format(
                        c,
                        f'<a href="#{type_str.lower()}">{type_str}</a>'
                        if referencable
                        else type_str,
                    )
                )
                doc_string += "\n    <td><i>%s</i></td>\n  </tr>\n\n" % (
                    insert_links(description)
                )

            elif format == RST_FORMAT:
                n = "**%s**" % c
                t = "{}".format(
                    rst_url_format % (type_str, "#" + type_str.lower())
                    if referencable
                    else type_str,
                )
                d = "%s" % (insert_links(description, format=RST_FORMAT))
                table_info.append([n, t, d])

            # Get the contained type
            if get_origin(type_) == list and len(get_args(type_)) > 0:
                referenced.append(get_args(type_)[0])
            elif get_origin(type_) == dict and len(get_args(type_)) > 1:
                referenced.append(get_args(type_)[1])
            else:
                referenced.append(type_)

        if len(allowed_children) > 0:
            if format == MARKDOWN_FORMAT:
                doc_string += "\n</table>\n\n"
            elif format == RST_FORMAT:
                doc_string += "%s\n\n" % (
                    tabulate(
                        table_info,
                        ["Allowed child", "Data Type", "Description"],
                        tablefmt="rst",
                    )
                )

        for r in referenced:
            if format in (MARKDOWN_FORMAT, RST_FORMAT):
                doc_string += r._cls_generate_documentation(format=format)
            if format in (DICT_FORMAT):
                doc_dict.update(r._cls_generate_documentation(format=format))

        if format in (MARKDOWN_FORMAT, RST_FORMAT):
            return doc_string
        if format == DICT_FORMAT:
            return doc_dict


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

    # This is a pass through right now. In the future we may want to convert nested lists to np.ndarrays.
    # but for now we just pass through. We need to add the hook to cattr or it will complain it doesn't
    # know how to structure the Union with EvaluableExpression and np.ndarray. Right now, these are just
    # serialized as strings and lists respectively
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
            return converter.unstructure(obj_list)

    return f


def _structure_list_base(cl):
    """Deserialize list of dict of Base objects as a list if all of their elements have ids"""
    base_class = get_args(cl)[0]

    def f(obj_dict, t):
        try:
            obj_list = [converter.structure(v, base_class) for v in obj_dict.values()]

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
    lambda cl: issubclass(cl, Base),
    _base_unstruct_hook_factory,
)

converter.register_structure_hook_factory(_is_list_base, _structure_list_base)
converter.register_structure_hook_factory(
    lambda cl: issubclass(cl, Base) and "id" in [a.name for a in fields(cl)],
    _base_struct_hook_factory,
)

# Add a general hook for handling ndarray unstructure
converter.register_unstructure_hook(np.ndarray, _unstructure_value_expr)

# Define some aliases for attr.define and other attrs stuff. This should hid attrs from the user a bit.
define = attr.define
has = attr.has
field = attr.field
fields = attr.fields
optional = attr.validators.optional
instance_of = attr.validators.instance_of
in_ = attr.validators.in_
