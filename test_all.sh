#!/bin/bash
set -ex

pip install .

cd examples
python document.py

cd test
python test.py

cd ../neuroml2
python neuroml2_spec.py

cd ../..

pytest tests -v

pre-commit run --all-files
