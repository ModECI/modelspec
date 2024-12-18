#!/bin/bash
set -ex

## Install modelspec incl. dev dependencies

pip install .[all]


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

## Test SBML example

cd ../sbml
./regenerateAndTest.sh

cd ../..


## Run pytest

pytest tests -v

## Run OMV tests

# See https://github.com/OpenSourceBrain/osb-model-validation
omv all -V


## Generate the docs

cd docs
python generate.py
python contributors.py
cd sphinx
make clean
make html
cd ..

## Format all file

/bin/bash -c 'pre-commit run --all-files; echo Finished running pre-commit!' # Note: prevents error code when reformatting
