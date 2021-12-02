from flask.templating import render_template_string
import redis
from flask import Flask, render_template

app = Flask(__name__)

rconn = redis.Redis(host='127.0.0.1', port='6379', db=5, decode_responses=True)

country_list = ['CH', 'RU', 'NL']

@app.route("/<country>")
def start_page(country):
    to_web = []
    if country in country_list:
        urls = rconn.lrange(country, 0, -1)
        for url in urls:
            to_web.append(url)
    else:
        return render_template_string('<center><h1>Sorry, there is no such country</h1></center>')
    return render_template('main.html', urls=to_web, country=country)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
