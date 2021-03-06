#!/bin/bash

set -eux

echo " + Checking for Python 3"
if command -v python3 >/dev/null 2>&1; then
    echo "   + Found python3!"
else
    echo "   E No python 3 installed. Please install and retry!"
    exit 1
fi

echo " + Checking for pip3"
if command -v pip3 >/dev/null 2>&1; then
    echo "   + Found pip3!"
else
    echo "   E No pip3 installed. Please install and retry!"
    exit 1
fi


pip3 install -U --user pip setuptools 

echo " + Checking for dependencies"

if pip3 install --user -r scripts/requirements.txt; then
	echo " + Successully Installed Modules"
	exit 0
fi
echo " E Pip Install Failed. Exiting."
exit 16

