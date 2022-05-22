# daredata-challenge

## Overview
The project is divided into three main components:
- A bash script `script.sh` that creates a csv file
- A python script `calculations.py` that reads the output from the previous bash script
- A flask application that bootstraps from `main.py`
- Note: I also added a folder resouces containing a postman collection and a zip with files to help with the testing.
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
- Make a HTTP request with a POST Method for `localhost:5000/upload` where HTTP body must be a "multipart/form-data" containing a  key-value pair , where the key is "file" and the value is a valid zip file.
#### BASH
- Create a folder with the name "files" at the root of the project containing the files that you wish to process
- Run script.sh <br>
`./script.sh`
- Run test.py to visualize the calculations output <br>
`python test.py` 
- If you wish to visualize the histogram uncomment line 26 of `calculations.py`


## Issues and improvements
- I did not consider input validations (for instance I didn't check if the key "file" is set on the "/upload" endpoint, neither I validated the size or the content of the zip file.
- I did not handle the specific case of the zip being empty
- I didn't implement any authentication which means that the API is public
- I did not use HTTPS (I used the flask development server)
- I didn't consider deleting the input zips or the outputs from the script
