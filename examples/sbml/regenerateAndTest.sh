#!/bin/bash
set -ex

python test_sbml3.py

python sbml_validators.py example_sbml_minimal.xml
python sbml_validators.py test_minimal_example.xml
