#!/bin/bash

# Activate Python virtual environment if exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install dependencies
pip install -r requirements.txt

# Run the scraper script
python src/main.py

# Deactivate virtual environment
if [ -d "venv" ]; then
    deactivate
fi
