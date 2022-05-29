#!/usr/bin/env bash

PYTHON="python3"
VENV_DIR="/Users/squickfi/goinfre/django_venv"

# setup venv
$PYTHON -m venv $VENV_DIR
source $VENV_DIR/bin/activate

# pip version
python3 -m pip --version

# pip install
python3 -m pip install --force-reinstall -r requirement.txt