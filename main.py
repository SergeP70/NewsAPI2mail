import requests

api_key = '044315ef4a2e4f5784f982be3b6a15c4'
url = ('https://newsapi.org/v2/everything?q=apple'
       '&from=2025-01-05&to=2025-01-05&sortBy=popularity&apiKey=044315ef4a2e4f5784f982be3b6a15c4')

request = requests.get(url)
content = request.json()

for article in content['articles']:
    print(article['title'])








