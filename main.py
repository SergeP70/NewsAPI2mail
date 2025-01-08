# Search for news articles that mention a specific topic or keyword
import requests
import mailer
from datetime import date
import os
from dotenv import load_dotenv
load_dotenv()

topic = "microsoft"
today = date.today()

# load only the first 15 and english topics:
api_key = '044315ef4a2e4f5784f982be3b6a15c4'
url = (f'https://newsapi.org/v2/everything?q={topic}'
       f'&from=2025-01-05&to={today}'
       '&sortBy=publishedAt'
       '&language=en'
       '&pageSize=15'
       '&apiKey=044315ef4a2e4f5784f982be3b6a15c4')

request = requests.get(url)
content = request.json()

# Compose email
receiver = os.getenv('USERNAME')
subject = f"News from {topic.title()}"
body = f"This are the bullet points from {topic}: \n\n"

for article in content['articles']:
    body = body + article['title'] + '\n' + str(article['description']) + '\n'
    body = body + article['url'] +'\n\n'

print(body)
mailer.send(receiver, subject, body)

