import urllib
import urllib2
url = 'http://api.site.com/method/'
values = {'argument1': 'value1',
          'argument2': 'value2'}
headers = {"User-Agent": 'python urllib2'}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
result = response.read()