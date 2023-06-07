import sys
import json
import bson
import yaml
import os
import math
import numpy as np
from xml.dom.minidom import parseString
import xml.etree.ElementTree as ET
import dicttoxml

from modelspec.base_types import print_
from modelspec.base_types import EvaluableExpression

from random import Random
from typing import Union

verbose = True


def load_json(filename: str):
    """
    Load a generic JSON file

    Args:
        filename: The name of the JSON file to load
    """

    with open(filename) as f:
        data = json.load(f, object_hook=ascii_encode_dict)

    return data


def load_yaml(filename: str):
    """
    Load a generic YAML file

    Args:
        filename: The name of the YAML file to load
    """
    with open(filename) as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)

    return data


def load_bson(filename: str):
    """
    Load a generic BSON file

    Args:
        filename: The name of the BSON file to load
    """
    with open(filename, "rb") as infile:
        data_encoded = infile.read()
        data = bson.decode(data_encoded)

    return data


def load_xml(filename: str):
    """
    This Loads a generic XML file

    Args:
        filename: The name of the XML file to laod
    """
    with open(filename) as file:
        tree = ET.parse(file)

    return tree


def save_to_json_file(info_dict, filename, indent=4):
    """
    This saves a dictionary to a JSON file.

    Args:
        info_dict (dict): The dictionary containing the data to be saved.
        filename (str): The name of the file to save the JSON data to.
        indent (int, optional): The number of spaces used for indentation in the JSON file.
                                Defaults to 4.
    """
    strj = json.dumps(info_dict, indent=indent)
    with open(filename, "w") as fp:
        fp.write(strj)


def save_to_yaml_file(info_dict, filename, indent=4):
    """
    This saves a dictionary to a YAML file.

    Args:
        info_dict (dict): The dictionary containing the data to be saved.
        filename (str): The name of the file to save the YAML data to.
        indent (int, optional): The number of spaces used for indentation in the YAML file.
                                Defaults to 4.
    """
    if sys.version_info[0] == 2:
        stry = yaml.dump(info_dict, indent=indent, default_flow_style=False)
    else:
        stry = yaml.dump(info_dict, indent=indent, sort_keys=False)
    with open(filename, "w") as fp:
        fp.write(stry)


def save_to_xml_file(info_dict, filename, indent=4):
    """
    This saves a dictionary to an XML file.

    Args:
        info_dict (dict): The dictionary containing the data to be saved.
        filename (str): The name of the file to save the XML data to.
        indent (int, optional): The number of spaces used for indentation in the XML file.
                                Defaults to 4.
    """
    xml = dicttoxml.dicttoxml(
        info_dict,
        custom_root=None,
        xml_declaration=False,
        attr_type=False)
    
    parsed_xml = parseString(xml)
    pretty_xml = parsed_xml.toprettyxml(indent=" " * indent)

    with open(filename, "w") as file:
        file.write(pretty_xml)


def ascii_encode_dict(data):
    """
    This encodes the values in a dictionary to ASCII.

    Args:
        data (dict): The dictionary to be encoded.

    Returns:
        dict: The dictionary with encoded values.
    """
    ascii_encode = (
        lambda x: x.encode("ascii")
        if (sys.version_info[0] == 2 and isinstance(x, unicode))
        else x
    )
    return dict(map(ascii_encode, pair) for pair in data.items())


def _parse_element(dict_format, to_build):
    """
    This parses an element represented in dictionary format and construct an object with the parsed data.

    Args:
        dict_format (dict): The dictionary representation of the element.
        to_build: The object to be constructed with the parsed data.

    Returns:
        The constructed object with the parsed data.
    """
    if verbose:
        print("Parse for element: [%s]" % dict_format)
    for k in dict_format.keys():
        if verbose:
            print(
                "  Setting id: {} in {} ({})".format(k, type.__name__, type(to_build))
            )
        to_build.id = k
        to_build = _parse_attributes(dict_format[k], to_build)

    return to_build


def _parse_attributes(dict_format, to_build):
    """
    This parses the attributes of an element represented in dictionary format and set them in the `to_build` object.

    Args:
        dict_format (dict): The dictionary representation of the element attributes.
        to_build: The object in which to set the attributes.

    Returns:
        The `to_build` object with the attributes set.
        """
    for key in dict_format:
        value = dict_format[key]
        new_format = True
        if verbose:
            print(
                "  Setting {}={} ({}) in {}".format(key, value, type(value), to_build)
            )

        if new_format:
            if type(to_build) == dict:
                to_build[key] = value

            elif key in to_build.allowed_children:
                type_to_use = to_build.allowed_children[key][1]
                for v in value:
                    ff = type_to_use()
                    if verbose:
                        print(f"    Type for {key}: {type_to_use} ({ff})")
                    ff = _parse_element({v: value[v]}, ff)
                    exec("to_build.%s.append(ff)" % key)
            else:
                if (
                    type(value) == str
                    or type(value) == int
                    or type(value) == float
                    or type(value) == bool
                    or type(value) == list
                    or value is None
                ):
                    to_build.__setattr__(key, value)
                else:
                    type_to_use = to_build.allowed_fields[key][1]
                    if verbose:
                        print(
                            "type_to_use: {} ({})".format(
                                type_to_use, type(type_to_use)
                            )
                        )
                        print(f"- {key} = {value}")

                    if type_to_use == EvaluableExpression:
                        vv = {}
                        to_build.__setattr__(key, vv)
                    else:
                        ff = type_to_use()
                        ff = _parse_attributes(value, ff)
                        exec("to_build.%s = ff" % key)

        else:
            if type(to_build) == dict:
                to_build[key] = value
            elif type(value) == str or type(value) == int or type(value) == float:
                to_build.__setattr__(key, value)
            elif type(value) == list:
                type_to_use = to_build.allowed_children[key][1]

                for vl in value:
                    ff = type_to_use()
                    ff = _parse_element(vl, ff)
                    exec("to_build.%s.append(ff)" % key)
            else:
                type_to_use = to_build.allowed_fields[key][1]
                ff = type_to_use()
                ff = _parse_attributes(value, ff)
                exec("to_build.%s = ff" % key)

    return to_build


def locate_file(f, base_dir):
    """
    This utility method is for finding the full path to a filename.

    Args:
        f (str): The filename to locate.
        base_dir (str): The base directory in which to search for the file.

    Returns:
        The full path to the file as a string.
    """
    if base_dir is None:
        return f
    file_name = os.path.join(base_dir, f)
    real = os.path.realpath(file_name)
    # print_v('- Located %s at %s'%(f,real))
    return real


def _val_info(param_val):
    """
    This generates a string representation of a parameter value.

    Args:
        param_val: The parameter value to generate the string representation for.

    Returns:
        The string representation of the parameter value.
    """
    if type(param_val) == np.ndarray:
        pp = "%s" % (np.array2string(param_val, threshold=4, edgeitems=1))
        pp = pp.replace("\n", "")
        pp += f" (NP {param_val.shape} {param_val.dtype})"
    elif type(param_val).__name__ == "EagerTensor":
        pp = "%s" % param_val
        pp = pp.replace("\n", "")
        # pp+=' (TF %s %s)'%(param_val.shape,param_val.dtype)
    elif type(param_val) == tuple:
        # If param_val is a tuple, recursively print its elements
        # separated by commas and wrapped in parentheses
        pp = "(" + ", ".join([_val_info(el) for el in param_val]) + ")"
    else:
        pp = "%s" % param_val
        t = type(param_val)
        if not (t == int or t == float):
            pp += "(%s)" % (t if type(t) == str else t.__name__)
    return pp


def _params_info(parameters, multiline=False):
    """
    Short info on names, values and types in parameter list.
    
    Args:
        parameters: The parameter list to generate the string representation for.
        multiline: A boolean indicating whether to include line breaks between parameter entries. Default is False.

    Returns:
        The string representation of the parameter list.
    """
    pi = "["
    if parameters is not None and len(parameters) > 0:
        for p in parameters:
            if not p == "__builtins__":
                param_val = parameters[p]
                pp = _val_info(param_val)

                pi += "{}={}, {}".format(p, pp, "\n" if multiline else "")
        pi = pi[:-2]
    pi += "]"
    return pi


# Ideas in development...
FORMAT_NUMPY = "numpy"
FORMAT_TENSORFLOW = "tensorflow"


def evaluate(
    expr: Union[int, float, str, list, dict],
    parameters: dict = {},
    rng: Random = None,
    array_format: str = FORMAT_NUMPY,
    verbose: bool = False,
    cast_to_int: bool = False,
):
    """
    Evaluate a general string like expression (e.g. "2 * weight") using a dict
    of parameters (e.g. {'weight':10}). Returns floats, ints, etc. if that's what's
    given in expr

    Args:
        expr: The expression to convert
        parameters: A dict of the parameters which can be substituted in to the expression
        rng: The random number generator to use
        array_format: numpy or tensorflow
        verbose: Print the calculations
        cast_to_int: return an int for float/string values if castable
    """

    if array_format == FORMAT_TENSORFLOW:
        import tensorflow as tf

    if verbose:
        print_(
            " > Evaluating: [%s] which is a: %s, vs parameters: %s (using %s arrays)..."
            % (expr, type(expr).__name__, _params_info(parameters), array_format),
            verbose,
        )
    try:
        if type(expr) == str and expr in parameters:
            expr = parameters[
                expr
            ]  # replace with the value in parameters & check whether it's float/int...
            if verbose:
                print_("   Using for that param: %s" % _val_info(expr), verbose)

        if type(expr) == str:
            try:
                if array_format == FORMAT_TENSORFLOW:
                    expr = tf.constant(int(expr))
                else:
                    expr = int(expr)
            except:

                try:
                    if array_format == FORMAT_TENSORFLOW:
                        expr = tf.constant(float(expr))
                    else:
                        expr = float(expr)
                except:
                    pass

        if type(expr) == list:
            if verbose:
                print_("   Returning a list in format: %s" % array_format, verbose)
            if array_format == FORMAT_TENSORFLOW:
                return tf.constant(expr, dtype=tf.float64)
            else:
                return np.array(expr)

        if type(expr) == np.ndarray:
            if verbose:
                print_(
                    "   Returning a numpy array in format: %s" % array_format, verbose
                )
            if array_format == FORMAT_TENSORFLOW:
                return tf.convert_to_tensor(expr, dtype=tf.float64)
            else:
                return np.array(expr)

        if "Tensor" in type(expr).__name__:
            if verbose:
                print_(
                    "   Returning a tensorflow Tensor in format: %s" % array_format,
                    verbose,
                )
            if array_format == FORMAT_NUMPY:
                return expr.numpy()
            else:
                return expr

        if int(expr) == expr and cast_to_int:
            if verbose:
                print_("   Returning int: %s" % int(expr), verbose)
            return int(expr)
        else:  # will have failed if not number
            if verbose:
                print_("   Returning {}: {}".format(type(expr), expr), verbose)
            return expr
    except:
        try:
            if rng:
                expr = expr.replace("random()", "rng.random()")
                parameters["rng"] = rng
            elif "random()" in expr:
                raise Exception(
                    "The expression [%s] contains a random() call, but a random number generator (rng) must be supplied to the evaluate() call when this expression string is to be evaluated"
                )

            if type(expr) == str and "math." in expr:
                parameters["math"] = math
            if type(expr) == str and "numpy." in expr:
                parameters["numpy"] = np

            if verbose:
                print_(
                    "   Trying to eval [%s] with Python using %s..."
                    % (expr, parameters.keys()),
                    verbose,
                )

            v = eval(expr, parameters)

            if verbose:
                print_(
                    "   Evaluated with Python: {} = {}".format(expr, _val_info(v)),
                    verbose,
                )

            if (type(v) == float or type(v) == str) and int(v) == v:

                if verbose:
                    print_("   Returning int: %s" % int(v), verbose)

                if array_format == FORMAT_TENSORFLOW:
                    return tf.constant(int(v))
                else:
                    return int(v)
            return v
        except Exception as e:
            if verbose:
                print_(f"   Returning without altering: {expr} (error: {e})", verbose)
            return expr


"""
    Translates a string like '3', '[0,2]' to a list
"""


def parse_list_like(list_str):
    """
    This parse a list-like object represented as a string and convert it back into a Python list.

    Args:
        list_str: The string representation of the list-like object.

    Returns:
        A Python list containing the parsed elements from the list-like object.
    """
    if isinstance(list_str, int):
        return [list_str]
    elif isinstance(list_str, float):
        return [list_str]
    elif isinstance(list_str, list):
        return list_str
    elif type(list_str) == str:
        try:
            expr = int(list_str)
            return [expr]
        except:
            pass
        try:
            expr = float(list_str)
            return [expr]
        except:
            pass
        if "[" in list_str:
            return eval(list_str)
