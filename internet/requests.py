import requests

res = requests.get("https://docs.python.org/3.5/")
print(res.status_code)
print(res.headers['Content-Type'])

print(res.content)  # контент страницы
print(res.text)  # текст данной страницы
