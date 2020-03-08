echo " + Checking for Python 3"
if command -v python3 >/dev/null 2>&1; then
	echo " + Found python3!"
else
	echo " E No python 3 installed. Please install and retry!"
	exit 1
fi

if python3 -c "import flask" >/dev/null 2>&1; then
	echo " + Flask already installed."
else
	echo " + Installing Flask for Python 3"
	if pip3 install flask --user; then
		echo " + Successfully installed flask!"
	else
		echo " E Pip3 failed to install flask. Exiting."
		exit 1
	fi
fi

if python3 -c "import pymongo" >/dev/null 2>&1; then
    echo " + PyMongo already installed."
else
    echo " + Installing PyMongo for Python 3"
    if pip3 install pymongo --user; then
        echo " + Successfully installed pymongo!"
    else
        echo " E Pip3 failed to install pymongo. Exiting."
        exit 1
    fi
fi


exit 0
