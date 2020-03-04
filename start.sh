if ./scripts/install_requirements.sh; then
	python3 server/server.py
else
	echo "Error installing requirements. Quitting"
	exit 1
fi
