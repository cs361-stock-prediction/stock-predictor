if ./scripts/install_requirements.sh; then
	echo " + Successful Install of Requirements."
else
	echo " E Error installing requirements. Quitting"
	exit 1
fi

while getopts ":c" arg; do
	case $arg in
		c) CHECK=1;;
	esac
done

if [[ $CHECK -eq 1 ]]; then
	exit 0
fi

export PATH=$PATH:$HOME/.local/bin
export FLASK_APP=predictor.py
flask run --host 0.0.0.0 --port 4096
