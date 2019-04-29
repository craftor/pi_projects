# -*- coding: utf-8 -*-
import time
import os
from camera import VideoCamera

from flask import Flask, render_template, Response, request
from flask import send_from_directory
from flask import url_for

from flask import Flask
app = Flask(__name__)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# mjpeg streaming
@app.route('/mjpeg')
def video_feed():
    return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

# checking status
@app.route("/check")
def checkstatus():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
