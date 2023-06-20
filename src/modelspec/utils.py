import sys
import json
import bson
import yaml
import xml.etree.ElementTree as ET
import xml.dom.minidom
import os
import math
import numpy as np
import xmltodict

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
    Load a generic XML file.

    Args:
        filename: The name of the XML file to load.
    """
    with open(filename, "rb") as infile:
        tree = ET.parse(infile)  # Parse the XML file into an ElementTree object
    root = tree.getroot()  # Get the root element

    # Convert the ElementTree object to a dictionary
    data = element_to_dict(root)

    return convert_values(data)


def element_to_dict(element):
    """
    Convert an ElementTree element to a dictionary.

    Args:
        element: The ElementTree element to convert.

    Returns:
        The converted dictionary.
    """
    if len(element) == 0:
        return element.text

    result = {}
    for child in element:
        child_data = element_to_dict(child)
        if child.tag in result:
            if not isinstance(result[child.tag], list):
                result[child.tag] = [result[child.tag]]
            result[child.tag].append(child_data)
        else:
            result[child.tag] = child_data

    return result

def convert_values(value):
    if isinstance(value, str):
        if value.isdigit():
            return int(value)
        try:
            return float(value)
        except ValueError:
            pass
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        elif value.lower() == "none":
            return None
    elif isinstance(value, dict):
        return {key: convert_values(val) for key, val in value.items()}
    elif isinstance(value, list):
        return [convert_values(item) for item in value]

    return value



def save_to_json_file(info_dict, filename, indent=4):

    strj = json.dumps(info_dict, indent=indent)
    with open(filename, "w") as fp:
        fp.write(strj)


def save_to_yaml_file(info_dict, filename, indent=4):

    if sys.version_info[0] == 2:
        stry = yaml.dump(info_dict, indent=indent, default_flow_style=False)
    else:
        stry = yaml.dump(info_dict, indent=indent, sort_keys=False)
    with open(filename, "w") as fp:
        fp.write(stry)


def save_to_xml_file(info_dict, filename, indent=4, root="modelspec"):
    """
    Save a dictionary to an XML file.

    Args:
        info_dict (dict): The dictionary containing the data to be saved.
        filename (str): The name of the file to save the XML data to.
        indent (int, optional): The number of spaces used for indentation in the XML file.
                                Defaults to 4.
    """
    root = ET.Element(root)

    build_xml_element(root, info_dict)

    # Create an ElementTree object with the root element
    tree = ET.ElementTree(root)

    # Generate the XML string
    xml_str = ET.tostring(root, encoding="utf-8", method="xml").decode("utf-8")

    # Create a pretty-formatted XML string using minidom
    dom = xml.dom.minidom.parseString(xml_str)
    pretty_xml_str = dom.toprettyxml(indent=" " * indent)

    # Write the XML data to the file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(pretty_xml_str)


def build_xml_element(parent, data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                element = ET.SubElement(parent, key.replace(" ", "_"))
                build_xml_element(element, value)
            elif isinstance(value, list):
                for item in value:
                    subelement = ET.SubElement(parent, key.replace(" ", "_"))
                    build_xml_element(subelement, item)
            else:
                element = ET.SubElement(parent, key.replace(" ", "_"))
                element.text = str(value)
    else:
        parent.text = str(data)


def ascii_encode_dict(data):
    ascii_encode = (
        lambda x: x.encode("ascii")
        if (sys.version_info[0] == 2 and isinstance(x, unicode))
        else x
    )
    return dict(map(ascii_encode, pair) for pair in data.items())


def _parse_element(dict_format, to_build):

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
    Utility method for finding full path to a filename as string
    """
    if base_dir is None:
        return f
    file_name = os.path.join(base_dir, f)
    real = os.path.realpath(file_name)
    # print_v('- Located %s at %s'%(f,real))
    return real


def _val_info(param_val):
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
    Short info on names, values and types in parameter list
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
