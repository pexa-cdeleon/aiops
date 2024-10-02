#!/usr/bin/env bash
set -e

#------------------------------------------------------------------
echo "Create Python virtual environment"

echo 'Hello PEXA'
#Check if virtual env is installed
check=$(pip list | grep virtualenv)
if [[ -z ${check} ]]; then
    echo "virtualenv not installed, installing..."
    pip install virtualenv
else
    echo "virtualenv already installed"
fi


`python3 aiops/scripts/pvt.py`
