import requests
template = "Response from {0.url} with code {0.status_code}"

res = requests.get("https://docs.python.org/3.5/")
print(template.format(res))

res = requests.get("https://docs.python.org/3.5/random")
print(template.format(res))