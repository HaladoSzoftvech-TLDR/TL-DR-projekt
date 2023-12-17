import csv
import os
import sys
from PyPDF2 import PdfReader
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from main.logic.model import summarize as model_summarize

# Get the path of the directory where app.py is located
dir_path = os.path.dirname(os.path.realpath(__file__))

# Use this path to construct the path of the 'view' directory
template_dir = os.path.join(dir_path, '..', 'view')

upload_dir = os.path.join(dir_path, '..', 'tools', 'uploads')
feedback_dir = os.path.join(dir_path, '..', 'tools', 'feedback')

app = Flask(__name__, template_folder=template_dir)

# Set the path for the uploaded files to be stored
app.config['UPLOAD_FOLDER'] = upload_dir
app.config['FEEDBACK_FOLDER'] = feedback_dir

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if 'file' in request.files and request.files['file'].filename != '':
        file = request.files['file']
        filename = secure_filename(file.filename)
        if not filename.endswith('.pdf'):
            return 'Please upload a PDF file only'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        pdf = PdfReader(pdf_path)
        text = " ".join(page.extract_text() for page in pdf.pages)
        os.remove(pdf_path)
    elif 'inputText' in request.form and request.form['inputText'].strip() != '':
        text = request.form['inputText']
    else:
        return 'No file or text provided'
    summarized_text = model_summarize(text)
    return render_template('index.html', outputText=summarized_text)

@app.route('/send_feedback', methods=['POST'])
def send_feedback():
    feedback_file_path = os.path.join(feedback_dir, 'feedback.csv')
    name = request.form['fullName'] if request.form['fullName'] != "" else 'Anon'

    email = request.form['emailAddress'] if request.form['emailAddress'] != "" else '-'

    feedback_text = request.form['feedbackText']

    with open(feedback_file_path, 'a') as f:
        line = f'{name},{email},{feedback_text}\n'
        f.write(line)

    return render_template('index.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
