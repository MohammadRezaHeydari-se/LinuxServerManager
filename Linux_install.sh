#!/bin/bash

echo ">>> Setting up virtual environment..."
python3 -m venv venv

echo ">>> Activating virtual environment..."
source venv/bin/activate

echo ">>> Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

echo ">>> Done. To start, run: "
echo "source venv/bin/activate && python main.py"
