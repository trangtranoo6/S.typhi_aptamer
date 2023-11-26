import os
from flask import Flask, render_template, url_for, request, redirect,flash
from werkzeug.utils import secure_filename
from pseb.clustering import kami 
from pseb.samples import generate_samples, peptide_length
from pseb.pseb import validatePeptide

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1000000

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'fasta'}

def process_values(request):
    flash_array, samples = [],[]
    assert request.form.get("typ") in {"upload","sample"}
    upload = request.form.get("typ") == "upload"
    sample_num, knum, lamda = request.form.get("num"), request.form.get("knum"), request.form.get("lambda")
    if (upload or sample_num.isnumeric()) and knum.isnumeric() and lamda.isnumeric():
        knum, lamda = int(knum), int(lamda)
    else:
        flash_array.append("Invalid input (not a number)")
        return False, flash_array, None, None, None , None
    if upload:
        if 'file' not in request.files:
            flash_array.append('No file selected.')
        file = request.files['file']
        if file.filename == '':
            flash_array.append('No file was selected.')
        if file and allowed_file(file.filename):
            file = file.read().decode().split('\n')
            samples = validatePeptide(file, lamda)
        elif file and not allowed_file(file.filename):
            flash_array.append('Please select proper .fasta file')
    else:
        sample_num = int(sample_num)
        if peptide_length <= lamda:
            flash_array.append('Not a valid lamda value (choose less than 15)')
        samples = generate_samples(sample_num)
    if len(samples) == 0:
        flash_array.append('No valid inputs found')
    return len(flash_array)==0, flash_array, sample_num, knum, lamda, samples

@app.route('/', methods=['GET', 'POST'])
def form_process():
    if request.method == 'POST':
        success, messages, sample_num, k_num, lamda, samples = process_values(request)
        if success:
            kami(samples, lamda, k_num)
            #uploaded page
            return render_template('uploaded.html')
        else:
            for message in messages:
                flash(message)
            return render_template('index.html')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
