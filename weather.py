import requests
import json


api_key = 'ed23fe201918a116bdd04e5f14143601'


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
    
def display_weather(data):
    if data:
        print(f"miasto :{data['name']}")
        print(f"Temperatura: {data['main']['temp']}°C")
        print(f"warunki pogodowe: {data['weather'][0]['description']}")
    else:
        print("nie mozna pobrac danych pogodowych")



if __name__ == "__main__":
    city = input("Podaj miasto: ")
    weather_data = get_weather(city)
    display_weather(weather_data)