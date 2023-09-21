from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

api_key = 'ed23fe201918a116bdd04e5f14143601'

@app.route("/", methods=["GET", "POST"])
def weather():
    weather_data = None
    if request.method =="POST":
        city = request.form["city"]
        weather_data = get_weather(city)

    return render_template("weath.html", weather_data=weather_data)

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    try:
        response = requests.get(url)
        if response.status_code ==200:
            data = json.loads(response.text)
            return data
        else:
            print("blad http:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("blad podczas zadania http:",e)
        return None
    
if __name__ == "__main__":
    app.run(debug=True)