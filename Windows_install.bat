@echo off
echo Setting up virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing requirements...
pip install --upgrade pip
pip install -r requirements.txt

echo Done!
echo To start, run:
echo venv\Scripts\activate && python main.py
