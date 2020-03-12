if ./scripts/install_requirements.sh; then
	export PATH=$PATH:$HOME/.local/bin
	export FLASK_APP=predictor.py
	flask run --port 4096
else
	echo "Error installing requirements. Quitting"
	exit 1
fi
