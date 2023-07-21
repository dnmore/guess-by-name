from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/guess")
def guess():
    name = request.args.get("name")
    genderize_url = f'https://api.genderize.io?name={name}'
    genderize_response = requests.get(genderize_url)
    genderize_data = genderize_response.json()
    gender = genderize_data['gender']

    agify_url = f'https://api.agify.io?name={name}'
    agify_response = requests.get(agify_url)
    agify_data = agify_response.json()
    age = agify_data['age']

    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
