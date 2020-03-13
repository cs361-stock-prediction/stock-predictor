# If requirements successfully installed, print, else fail
if ./scripts/install_requirements.sh; then
	echo " + Successful Install of Requirements."
else
	echo " E Error installing requirements. Quitting"
	exit 1
fi

# Get arguments
while getopts ":c" arg; do
	case $arg in
		c) CHECK=1;;
	esac
done

# If argument -c passed, check is needed. 
#	Quit before starting server -- right now this just tests the 
#	installation of deps went well, for CI
if [[ $CHECK -eq 1 ]]; then
	exit 0
else
	# Run server otherwise
	export PATH=$PATH:$HOME/.local/bin
	export FLASK_APP=predictor.py
	flask run --host 0.0.0.0 --port 4096
fi