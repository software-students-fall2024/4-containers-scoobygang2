"""
backend for html, should link pages and display results
"""
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    """Function rendering uploaded file"""
    return render_template('fileUpload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Function saving file and rendering it"""
    if 'files[]' in request.files:
        file = request.files['files[]']
        file.save(file.filename)
        return render_template('uploaded.html')
    return 'No file uploaded'

@app.route('/spoken')
def spoken():
    """Function dealing with spoken words"""
    return render_template('spoken.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
