import requests
from flask import Flask, render_template

app = Flask(__name__)

city = 'London'
api = ''
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"


def get_raw_weather():
    resp = requests.get(url)
    if resp.status_code == 200:
        weather = resp.json()
    else:
        print('We have some issues')
    return weather


def pre_weather(raw_data):
    weather_desc = raw_data['weather'][0]['description']
    temp = raw_data['main']['temp']
    feels_like = raw_data['main']['feels_like']
    return weather_desc, temp, feels_like


# using decorator for function to run tiny web-server with
# page, generated from template
@app.route("/")
def start_page():
    forecast = pre_weather(get_raw_weather())
    weather = forecast[0]
    main_temp = forecast[1]
    feels = forecast[2]
    return render_template('main.html', temp=main_temp, feels_like=feels, main_weather=weather, city_weather=city)

# running web-server on any host
if __name__ == "__main__":
    app.run(host='0.0.0.0')

# print raw data
#print(get_raw_weather())

# print formatted data
#print(pre_weather(get_raw_weather()))