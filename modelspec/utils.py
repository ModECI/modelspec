from modelspec import *
import sys
import json
import yaml
import os
import math
import numpy as np

from modelspec.BaseTypes import print_v, print_
from modelspec.BaseTypes import EvaluableExpression

verbose = False


def load_json(filename):
    """
    Load a generic JSON file
    """

    with open(filename, "r") as f:

        data = json.load(f, object_hook=ascii_encode_dict)

    return data


def load_yaml(filename):
    """
    Load a generic YAML file
    """
    with open(filename, "r") as f:

        data = yaml.load(f, Loader=yaml.SafeLoader)

    return data



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
            print("  Setting id: %s in %s (%s)" % (k, type.__name__, type(to_build)))
        to_build.id = k
        to_build = _parse_attributes(dict_format[k], to_build)

    return to_build


def _parse_attributes(dict_format, to_build):

    for key in dict_format:
        value = dict_format[key]
        new_format = True
        if verbose:
            print("  Setting %s=%s (%s) in %s" % (key, value, type(value), to_build))

        if new_format:
            if type(to_build) == dict:
                to_build[key] = value

            elif key in to_build.allowed_children:
                type_to_use = to_build.allowed_children[key][1]
                for v in value:
                    ff = type_to_use()
                    if verbose:
                        print("    Type for %s: %s (%s)" % (key, type_to_use, ff))
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
                        print("type_to_use: %s (%s)" % (type_to_use, type(type_to_use)))
                        print("- %s = %s" % (key, value))

                    if type_to_use == EvaluableExpression:
                        vv = {}
                        dd = _parse_attributes(value, vv)
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

                for l in value:
                    ff = type_to_use()
                    ff = _parse_element(l, ff)
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
    if base_dir == None:
        return f
    file_name = os.path.join(base_dir, f)
    real = os.path.realpath(file_name)
    # print_v('- Located %s at %s'%(f,real))
    return real


def _val_info(param_val):
    if type(param_val) == np.ndarray:
        pp = "%s" % (np.array2string(param_val, threshold=4, edgeitems=1))
        pp = pp.replace("\n", "")
        pp += " (NP %s %s)" % (param_val.shape, param_val.dtype)
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
    if parameters is not None and len(parameters)>0:
        for p in parameters:
            if not p == "__builtins__":
                param_val = parameters[p]
                pp = _val_info(param_val)

                pi += "%s=%s, %s" % (p, pp, '\n' if multiline else '')
        pi = pi[:-2]
    pi += "]"
    return pi


# Ideas in development...
FORMAT_NUMPY = "numpy"
FORMAT_TENSORFLOW = "tensorflow"


def evaluate(expr, parameters={}, rng=None, array_format=FORMAT_NUMPY, verbose=False):
    """
    Evaluate a general string like expression (e.g. "2 * weight") using a dict
    of parameters (e.g. {'weight':10}). Returns floats, ints, etc. if that's what's
    given in expr
    """

    if array_format == FORMAT_TENSORFLOW:
        import tensorflow as tf

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
            print_("Using for that param: %s" % _val_info(expr), verbose)

        if type(expr) == str:
            try:
                if array_format == FORMAT_TENSORFLOW:
                    expr = tf.constant(int(expr))
                else:
                    expr = int(expr)
            except:
                pass
            try:
                if array_format == FORMAT_TENSORFLOW:
                    expr = tf.constant(float(expr))
                else:
                    expr = float(expr)
            except:
                pass

        if type(expr) == list:
            print_("Returning a list in format: %s" % array_format, verbose)
            if array_format == FORMAT_TENSORFLOW:
                return tf.constant(expr, dtype=tf.float64)
            else:
                return np.array(expr)

        if type(expr) == np.ndarray:
            print_("Returning a numpy array in format: %s" % array_format, verbose)
            if array_format == FORMAT_TENSORFLOW:
                return tf.convert_to_tensor(expr, dtype=tf.float64)
            else:
                return np.array(expr)

        if "Tensor" in type(expr).__name__:
            print_(
                "Returning a tensorflow Tensor in format: %s" % array_format, verbose
            )
            if array_format == FORMAT_NUMPY:
                return expr.numpy()
            else:
                return expr

        if int(expr) == expr:
            print_("Returning int: %s" % int(expr), verbose)
            return int(expr)
        else:  # will have failed if not number
            print_("Returning float: %s" % expr, verbose)
            return float(expr)
    except:
        try:
            if rng:
                expr = expr.replace("random()", "rng.random()")
                parameters["rng"] = rng

            if type(expr) == str and "math." in expr:
                parameters["math"] = math
            if type(expr) == str and "numpy." in expr:
                parameters["numpy"] = np

            print_(
                "Trying to eval [%s] with Python using %s..."
                % (expr, parameters.keys()),
                verbose,
            )

            v = eval(expr, parameters)
            print_("Evaluated with Python: %s = %s" % (expr, _val_info(v)), verbose)
            if (type(v) == float or type(v) == str) and int(v) == v:
                print_("Returning int: %s" % int(v), verbose)

                if array_format == FORMAT_TENSORFLOW:
                    return tf.constant(int(v))
                else:
                    return int(v)
            return v
        except Exception as e:
            print_("Returning without altering: %s (error: %s)" % (expr, e), verbose)
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
            l = eval(list_str)
            return l
