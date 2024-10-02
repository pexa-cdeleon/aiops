#!/usr/bin/env bash
set -e

#------------------------------------------------------------------
echo "Create Python virtual environment"
pip install virtualenv

`python3 aiops/scripts/pvt.py`
