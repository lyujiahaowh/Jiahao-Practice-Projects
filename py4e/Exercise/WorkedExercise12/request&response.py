import requests

response = requests.get('http://data.pr4e.org/intro-short.txt')

print('Last-Modified:', response.headers.get('Last-Modified'))
print('ETag:', response.headers.get('ETag'))
print('Content-Length:', response.headers.get('Content-Length'))
print('Cache-Control:', response.headers.get('Cache-Control'))
print('Content-Type:', response.headers.get('Content-Type'))
