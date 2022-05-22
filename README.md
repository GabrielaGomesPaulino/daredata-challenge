# daredata-challenge

## Overview
The project is divided in three main components:
- A bash script `script.sh` that creates a csv file
- A python script `calculations.py` that reads the ouput from the previous bash script
- A flask application that bootstraps from `main.py`

## Project setup instructions
``` bash
git clone https://github.com/GabrielaGomesPaulino/daredata-challenge.git

cd daredata-challenge
pip install -r requirements.txt
python3 -m venv venv

#for windows
venv/Scripts/activate 
#for macOS/Linux
venv/bin/activate

export FLASK_APP=main
python -m flask run # if this does not work try flask run
```

## Testing instructions
#### HTTP
- Make a HTTP request with a POST Method for `localhost:5000/upload` where HTTP body must be a "multipart/form-data" containing a  key value pair , where the key is "file" and the value is a valid zip file.
#### BASH
- Create a folder with the name "files" in the root of the project containing the files that you wish to process
- Run script.sh <br>
`.\script.sh`
- Run test.py to visualize the calculations output <br>
`python test.py`
