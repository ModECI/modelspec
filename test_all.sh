#!/bin/bash
set -ex

pip install .

cd examples
python document.py

cd ..

pytest tests
