from flask import Flask, send_file
import random

app = Flask(__name__)

@app.route('/')
def webcam():
    randint = random.randint(0,2)
    if randint == 0:
        filename = 'gifs/bird_scream.gif'
    elif randint == 1:
        filename = 'gifs/meerkat.gif'
    else:
        filename = 'gifs/giraffe.gif'
    return send_file(filename, mimetype='image/gif')
