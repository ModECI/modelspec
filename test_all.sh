#!/bin/bash
set -ex

## Install

pip install .


## Test main example

cd examples
python document.py

cd test
python test.py


## Test NeuroML example

cd ../neuroml2
python neuroml2_spec.py

# Requires: pip install pyneuroml
pynml -validate hello_world_neuroml.net.nml
pynml -validate TestNeuroML.xml

cd ../..


## Run pytest

pytest tests -v


## Generate the docs

cd docs
python generate.py
cd sphinx
make clean
make html
cd ..

pre-commit run --all-files
