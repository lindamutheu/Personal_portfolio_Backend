#!/usr/bin/env bash
set -o errexit

# Install from the root
pip install -r requirements.txt

# Run commands by pointing to the subfolder's manage.py
python personal_portfolio/manage.py collectstatic --no-input
python personal_portfolio/manage.py migrate