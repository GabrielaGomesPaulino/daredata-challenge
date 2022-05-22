# daredata-challenge

## Project setup instructions
``` bash
git clone https://github.com/GabrielaGomesPaulino/daredata-challenge.git

cd daredata-challenge
pip install -r requirements
python3 -m venv venv

#for windows
venv/Scripts/activate 
#for macOS/Linux
venv/bin/activate

export FLASK_APP=main
python -m flask run # if this does not work try flask run
