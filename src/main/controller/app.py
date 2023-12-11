from flask import Flask, request, render_template
import os

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
    # For now, just return the same text received from the user
    return render_template('index.html', outputText=text)

if __name__ == '__main__':
    app.run(debug=True)
