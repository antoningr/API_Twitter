import tweepy
import pandas as pd
import matplotlib.pyplot as plt
import config

# Définition des clés d'API de Twitter
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

# Authentification avec l'API Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Création de l'objet API
api = tweepy.API(auth)

# Paramètres de recherche
query = 'covid OR coronavirus'
max_tweets = 1000

# Récupération des tweets à partir de l'API Twitter
tweets = tweepy.Cursor(api.search_tweets, q=query, lang='fr').items(max_tweets)

# Conversion des tweets en un DataFrame pandas
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

# Affichage des 10 premiers tweets
print(data.head(10))

# Affichage du nombre de tweets récupérés
print('Nombre de tweets récupérés :', len(data))

# Création d'un graphique à barres pour visualiser les tweets par langue
langs = data.apply(lambda x: x[0].lang, axis=1)
langs_count = langs.value_counts()
plt.bar(langs_count.index, langs_count)
plt.title('Répartition des tweets par langue')
plt.xlabel('Langue')
plt.ylabel('Nombre de tweets')
plt.show()
