#!/bin/bash
# Script used to update the locked package versions in requirements.in

if pip show pip-tools &> /dev/null; then
	echo 'Pip tools is installed; skipping installation'
else
	echo 'Pip tools is not installed; installing package'
	pip install pip-tools
fi

pip-compile -o requirements.in requirements.txt
