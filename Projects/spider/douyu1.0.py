import requests

url='https://www.douyu.com/directory/all'
html=requests.get(url)
print(html.text)