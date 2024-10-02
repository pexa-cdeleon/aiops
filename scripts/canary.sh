#!/usr/bin/env bash
set -e

log() { printf "INFO: ${1}\n"; }
loge() { printf "ERROR: ${1}\n"; }

#------------------------------------------------------------------
log "Create Python virtual environment"

echo 'Hello PEXA'
#Check if virtual env is installed
check=$(pip list | grep virtualenv)
if [[ -z ${check} ]]; then
    log "virtualenv not installed, installing..."
    pip install virtualenv
else
    log "virtualenv already installed"
fi


`python3 aiops/scripts/pvt.py`
