from flask import Flask,render_template,request, redirect, url_for, session
import csv
import pandas as pd
import numpy as np
import time

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("request_approval.html")

@app.route("/view_page")
def view_page():
    return render_template("view_page.html")

## 実行
if __name__ == "__main__":
    app.run(debug=True)