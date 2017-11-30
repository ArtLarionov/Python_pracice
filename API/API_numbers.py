import requests

with open('/Users/Artem/Desktop/dataset_24476_3.txt') as read_file, \
        open('/Users/Artem/Desktop/result_file.txt', 'w') as result_file:
    numbers = read_file.read().strip().split('\n')
    for number in numbers:
        api_url = 'http://numbersapi.com/{}/math?json=true'.format(number)

        req = requests.get(api_url)
        print(req.status_code)
        print(req.headers["Content-Type"])
        data = req.json()

        if data["found"] is True:
            result_file.write("Interesting\n")
        else:
            result_file.write("Boring\n")
