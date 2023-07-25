# Quick Start Guide to Modelspec

This is a quick guide to the various parts of the modelspec module and examples.

## Installation of Python API

Use **pip** to install the latest version of modelspec (plus dependencies) from [PyPI](https://pypi.org/project/modelspec):
```
pip install modelspec
```

More details, and importantly, how to set up a [virtual environment](https://virtualenv.pypa.io/en/latest/) for the package, can be found [here](Installation).

## Examples of Modelspec

### Simple example

A basic example which illustrates how to create the specification for a document(model) and create serialized instances can be found [here](examples/README).

### Serialization formats

Python scripts can be used to generate the specification of a type of model(e.g. [this](https://github.com/ModECI/modelspec/blob/main/examples/document.py)), but the models are saved in standardized format in either text based [JSON](https://github.com/ModECI/modelspec/blob/main/examples/document.json) or [YAML](https://github.com/ModECI/modelspec/blob/main/examples/document.yaml) formats or in binary [BSON](https://github.com/ModECI/modelspec/blob/main/examples/document.bson) format. Support for XML serialization is under development.

### Current formats using modelspec

#### MDF

MDF uses modelspec to create the structure of its models and convert the models into serialized formats such as JSON, YAML, and BSON.

#### NeuroML

NeuroMLlite uses modelspec to create the structure of its models and convert the models into serialize formats such as JSON, YAML, and BSON.
