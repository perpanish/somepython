import requests

# proxies = {"https": "https://203.198.105.252:28899", "http": "http://203.198.105.252:28899",}
r = requests.get('http://www.javlibrary.com/cn/')
print(r.status_code)
