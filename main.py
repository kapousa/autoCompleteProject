from flask import Flask, request, render_template
import pandas
import csv
from sys import argv

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        languages = [["C++", "Python", "PHP", "Java", "C", "Ruby",
                     "R", "C#", "Dart", "Fortran", "Pascal", "Javascript"], ['usa','uae','uk']]
        return render_template("index.html", languages=languages)


if __name__ == '__main__':
    app.run(debug=True)
