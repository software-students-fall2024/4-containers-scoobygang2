from flask import Flask, render_template, request, session
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from speech_to_text import audio_to_text

app = Flask(__name__)


@app.route('/')
def index():
    if 'files[]' in request.files:
        file = request.files['files[]']
        file.save(file.filename)
        session['audiofile'] = file
        return redirect(url_for('uploaded'))
        # return render_template('uploaded.html')
    return render_template('fileUpload.html')

@app.route('/uploaded', methods=['POST'])
def upload_file():
    action=request.form.get('action')
    if action=='microphone':
        # result=audio_to_text(1000)
        return render_template('uploaded.html', transcript=result)
                           
@app.route('/spoken')
def spoken():
    return render_template('spoken.html', "The transcript is here.")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)