import numpy as np
import os
from flask import Flask, render_template, flash, request, redirect
from werkzeug.utils import secure_filename
from sklearn.feature_extraction.text import CountVectorizer
import joblib


# Base path to directory with data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
vectorizer = os.path.join(DATA_DIR, 'vectorizer.joblib')
model = os.path.join(DATA_DIR, 'vectorizer.joblib')

ALLOWED_EXTENSIONS = ['txt']
def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)


@app.route('/api/check', methods=['POST'])
def kiddies ():
  if request.method == 'POST':
    # check if the post request has the file part
    if 'story' not in request.files:
      print('No file part')
      return redirect(request.url)
    file = request.files['story']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
      flash('No selected file')
      return redirect(request.url)
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config[DATA_DIR],filename))
      with open(DATA_DIR, filename, encoding='utf-8', errors='ignore') as f:
            text = f.readlines()
      return text


def _get_profane_prob(prob):
    return prob[1]
      
def predict(kiddies):
    #print(text)
    return model.predict(vectorizer.transform(kiddies))

def predict_prob(kiddies):
    return np.apply_along_axis(_get_profane_prob, 1, model.predict_proba(vectorizer.transform(kiddies)))
    

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)