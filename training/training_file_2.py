import requests

count = 0
r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/699991.txt")
s = "https://stepic.org/media/attachments/course67/3.6.3/"
f = (requests.get(s+r.text)).text
while f != "We":
    f = requests.get(s+f).text
    count += 1
    print(count), print(f)
print(requests.get(s+f).text)
