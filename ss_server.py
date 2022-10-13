from flask import Flask, render_template, url_for
import json

app = Flask(__name__)

@app.route("/ss_streets")
def streets_endpoint():
    f = open('Calles_SS.geojson')
    streets = json.load(f)
    f.close()
    return streets

@app.route("/")
def main_page():
    return render_template('homepage.html')