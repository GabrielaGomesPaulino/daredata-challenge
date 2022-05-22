from flask import Flask, request
import zipfile
import subprocess
import calculations

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Welcome"}

@app.route('/upload', methods=['POST'])
def upload():
    # Read file from http body
    uploaded_file = request.files['file']
    # Save uploaded file into working directory
    uploaded_file.save('tmp_uploaded.zip')
    # Unzip file
    with zipfile.ZipFile('tmp_uploaded.zip', 'r') as zip_ref:
        zip_ref.extractall()
    # Run bash script
    subprocess.call("sh script.sh", shell=True)
    # Run calculations
    data = calculations.run_calculate()

    return data