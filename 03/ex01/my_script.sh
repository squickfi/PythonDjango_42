#!/usr/bin/env bash

LOG_FILE="pip_install.log"
PYTHON="python3"
PATH_PY_URL="https://github.com/jaraco/path.git"
VENV_DIR="../local_lib"
SMALL_PROGRAM="my_program.py"

# setup venv
$PYTHON -m venv $VENV_DIR
source $VENV_DIR/bin/activate

# pip version
python3 -m pip --version

# pip install
python3 -m pip install --log $LOG_FILE --force-reinstall git+$PATH_PY_URL

# execute the small program
python3 $SMALL_PROGRAM