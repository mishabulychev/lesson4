import requests

def get_weather(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("Что-то пошло не так")

if __name__ == "__main__":
    data = get_weather("http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=7d003ffb0fa86d1c17cf04b90092673f&units=metric")
    print(data)