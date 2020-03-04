echo " + Checking for Python 3"
if command -v python3 >/dev/null 2>&1; then
	echo "   Found python3!"
else
	echo " ! No python 3 installed. Please install and retry!"
	exit 1
fi

echo " + Installing Flask for Python 3"
if pip3 install flask --user; then
	echo "   Successfully installed flask!"
else
	echo " ! Pip3 failed to install flask. Exiting."
	exit 1
fi

exit 0