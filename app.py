from flask import Flask, request, render_template

app = Flask(__name__)

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
