from flask import Flask, render_template, url_for
import json

app = Flask(__name__)

@app.route("/")
def main_page():
    f = open('Calles_SS.geojson')
    streets = json.load(f)
    f.close()
    return render_template('homepage.html', geojson = streets)