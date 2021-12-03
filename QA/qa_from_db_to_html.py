# importing necessary modules for working with flask, flask templates and database
from flask.templating import render_template_string
import redis
from flask import Flask, render_template

app = Flask(__name__)

# how we connecting to database
rconn = redis.Redis(host='127.0.0.1', port='6379', db=5, decode_responses=True)

# list of countries for our select from database
country_list = ['CH', 'RU', 'NL']

# decorator for our function with URL path determination. i.e. http:/127.0.0.1/RU in case of <coutry> is RU
@app.route("/<country>")
def start_page(country):
# creating empty list
    to_web = []
# appending an url to the list for each country from country list, gathered from database
    if country in country_list:
# get an country match from first to last (first from the end)
        urls = rconn.lrange(country, 0, -1)
# filling urls list
        for url in urls:
            to_web.append(url)
# if country not in our list, print message about wrong country selection
    else:
        return render_template_string('<center><h1>Sorry, there is no such country</h1></center>')
# otherwise output gathered data from database by flask to the web using prepared template
    return render_template('main.html', urls=to_web, country=country)

if __name__ == "__main__":
# bind flask application on any host for default port
    app.run(host='0.0.0.0')
