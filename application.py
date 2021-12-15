from flask import Flask, flash, redirect, render_template, request, url_for, send_from_directory, sessions
import flask
from werkzeug.utils import secure_filename
import os
import sys
import time
import pyscreenshot as ImageGrab
#import wx
from PIL import Image
import shutil

application = Flask(__name__)

#링크들
@application.route("/")
def hello():
    return render_template("hello.html")

@application.route("/apply")
def apply():
    global age, sex, itch, pain, grow, area, accept
    age = request.args.get("age")
    sex = request.args.get("sex")
    itch = request.args.get("itch")
    pain = request.args.get("pain")
    grow = request.args.get("grow")
    area = request.args.get("area")
    accept = request.args.get("accept")
    #mylist = [age, sex, itch, pain, grow, area, accept]
    return render_template("apply.html")


@application.route("/us")
def us():
    return render_template("us.html")

@application.route("/skin")
def skin():
    return render_template("skin.html")

@application.route("/agree")
def agree():
    return render_template("agree.html")

@application.route("/applyPhoto")
def applyPhoto():
    return render_template("applyPhoto.html")

@application.route("/result")
def result():
    return render_template("result.html", age=age, sex=sex, itch=itch, pain=pain, grow=grow, area=area, accept=accept)


@application.route("/fileUpload", methods=['GET', 'POST'])
def fileUpload():
    if request.method == "POST":
        f = request.files['file']
        f.save("./uploads/" + secure_filename(f.filename))

        src = os.path.join("./uploads/" + f.filename)
        dst = os.path.join("./static/" + f.filename)
        shutil.copyfile(src,dst)

        return render_template('result.html', image_file = f.filename)
    else:
        return render_template('applyPhoto.html')

@application.route("/download")
def download():
    global time
    now = time.localtime()
    time = "%04d-%02d-%02d-%02dh-%02dm-%02ds" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    img=ImageGrab.grab()
    saveas="{}{}".format(time,'.png')
    img.save(saveas)
    return flask.send_file(saveas, as_attachment=True)

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0')