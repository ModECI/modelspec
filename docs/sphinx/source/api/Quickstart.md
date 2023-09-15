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

A basic example which illustrates how to create the specification for a document (i.e. the model definition for a document) and create serialized instances can be found [here](examples/README).

### Serialization formats

Python scripts can be used to generate the specification of a type of model (e.g. [this](https://github.com/ModECI/modelspec/blob/main/examples/document.py)), but the models are saved in standardized format in either text based ([JSON](https://github.com/ModECI/modelspec/blob/main/examples/document.json) or [YAML](https://github.com/ModECI/modelspec/blob/main/examples/document.yaml)) formats or in binary ([BSON](https://github.com/ModECI/modelspec/blob/main/examples/document.bson)) format. Support for [XML](https://github.com/ModECI/modelspec/blob/main/examples/document.xml) serialization has recently been added.

### Current formats using modelspec

#### MDF (Model Description Format)

[ModECI's MDF](https://modeci.org/quickstart) uses modelspec to create the structure of its models and convert the models into serialized formats such as JSON, YAML, and BSON.

#### NeuroML

[NeuroMLlite](https://github.com/NeuroML/NeuroMLlite) uses modelspec to create the structure of its models and convert the models into serialize formats such as JSON, YAML, and BSON.
The XML serialisation of modelspec will be useful for integrating NeuroML 2 files into the framework, see [here](https://github.com/ModECI/modelspec/tree/main/examples/neuroml2).
