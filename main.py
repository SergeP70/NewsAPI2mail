import requests
import mailer

api_key = '044315ef4a2e4f5784f982be3b6a15c4'
url = ('https://newsapi.org/v2/everything?q=apple'
       '&from=2025-01-05&to=2025-01-05&sortBy=popularity&apiKey=044315ef4a2e4f5784f982be3b6a15c4')

request = requests.get(url)
content = request.json()
receiver = "sergepille70@gmail.com"
subject = "News from Apple"
message = "This are the bullet points from Apple: \n\n"

for article in content['articles']:
    # print(article['description'])
    message = message + article['title'] + '\n' + str(article['description']) + '\n\n'


print(message)
mailer.send(receiver, subject, message)

