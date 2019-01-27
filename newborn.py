import requests

def get_new_born(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("Что-то пошло не так")

if __name__ == "__main__":
    data = get_new_born("http://api.data.mos.ru/v1/datasets/2009/rows?api_key=931d898e389ed7d74755c4ca9ff7e64d")
    print(data)