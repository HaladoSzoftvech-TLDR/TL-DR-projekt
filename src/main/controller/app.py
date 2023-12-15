import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from flask import Flask, request, render_template
from main.logic.model import summarize as model_summarize

# Get the path of the directory where app.py is located
dir_path = os.path.dirname(os.path.realpath(__file__))

# Use this path to construct the path of the 'view' directory
template_dir = os.path.join(dir_path, '..', 'view')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['inputText']
    summarized_text = model_summarize(text)
    return render_template('index.html', outputText=summarized_text)

if __name__ == '__main__':
    app.run(debug=True)
