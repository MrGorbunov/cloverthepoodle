from flask import Flask, flash, render_template
from flask import Markup
app = Flask(__name__)



@app.route('/')
def hello_world():
  return render_template("index.html")
