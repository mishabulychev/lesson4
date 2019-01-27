from datetime import datetime

from flask import Flask

from req import get_weather

city_id = 524901
apikey = '7d003ffb0fa86d1c17cf04b90092673f'

app = Flask(__name__)


@app.route("/")
def index():
    url = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric&lang=ru" % (city_id, apikey)
    weather = get_weather(url)
    cur_date = datetime.now().strftime('%d.%m.%Y')

    result = "<p><b>Температура:</b> %s</p>" % weather['main'] ['temp']
    result += "<p>Город %s</p>" % weather ['name']
    result += "<p><b>Дата: </b>%s</p>" % cur_date
    return result

if __name__ == "__main__":
    app.run(port=3000)