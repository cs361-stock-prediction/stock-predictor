#!/bin/bash

echo " + Checking for Python 3"
if command -v python3 >/dev/null 2>&1; then
    echo "   + Found python3!"
else
    echo "   E No python 3 installed. Please install and retry!"
    exit 1
fi

python3 -m pip install -U --user pip setuptools 

echo " + Checking for dependencies"

if python3 -m pip install --user -r scripts/requirements.txt; then
	echo " + Successully Installed Modules"
	exit 0
fi
echo " E Pip Install Failed. Exiting."
exit 16

