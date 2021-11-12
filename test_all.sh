#!/bin/bash
set -ex

pip install .

cd modelspec/test
pytest -v
