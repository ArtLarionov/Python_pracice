import requests

film_name = str(input('Enter the film name: '))
api_url = 'http://www.omdbapi.com/?'

params = {
    't': film_name
}

res = requests.get(api_url, params=params)

# print(res.status_code)
# print(res.headers["Content-Type"])
# print(res.json())

data = res.json()
print()
title = 'Title: {}'
awards = 'Awards: {}'
print(title.format(data['Title']))
print(awards.format(data['Awards']))
