if ./scripts/install_requirements.sh; then
	export FLASK_APP=predictor.py
	flask run --port 4096
else
	echo "Error installing requirements. Quitting"
	exit 1
fi
