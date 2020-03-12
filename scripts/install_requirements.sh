#!/bin/bash

install_dep () {
    if python3 -c "import $1" >/dev/null 2>&1; then
	echo "   + $1 already installed."
    else
	echo "   + Installing $1 for Python 3"
	if pip3 install $1 --user; then
	    echo "   + Successfully installed $1!"
	else
	    echo "   E Pip3 failed to install $1. Exiting."
	    exit 1
	fi
    fi
}

echo " + Checking for Python 3"
if command -v python3 >/dev/null 2>&1; then
    echo "   + Found python3!"
else
    echo "   E No python 3 installed. Please install and retry!"
    exit 1
fi

echo " + Checking for dependencies"
for i in flask flask_wtf wtforms flask_sqlalchemy pymysql flask_migrate flask_login requests
do
    install_dep $i
done

exit 0
