from lxml import etree
import requests

req = requests.get("http://doc.python.org/3/")
print(req.status_code)
print(req.headers["content-Type"])

parser = etree.HTMLParser()
root = etree.fromstring(req.text, parser)

print(root)
for element in root.iter("a"):
    print(element, element.attrib)
