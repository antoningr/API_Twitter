# Projet : Twitter API


## Introduction

### Description : Projet
Le but de ce projet est de fournir une introduction à l'utilisation de l'API Twitter en récupérant des données comme les tweets en temps réel et en effectuant des analyses simples à l'aide de Python.

### Description : API Twitter
L'API Twitter est une interface de programmation qui permet aux développeurs d'accéder aux données et aux fonctionnalités de la plateforme de Twitter, tels que les tweets, les utilisateurs, les hashtags, les mentions, les listes, etc. L'API est conçue pour être utilisée par les développeurs d'applications tierces afin de créer des services et des applications qui utilisent les données de Twitter.

Il existe plusieurs versions de l'API Twitter, qui sont régulièrement mises à jour et améliorées. La version actuelle de l'API est la version 2, qui a été publiée en 2020. Cette version inclut de nouvelles fonctionnalités, telles que la possibilité de récupérer des conversations de tweet, de filtrer les tweets en fonction de leur engagement, d'obtenir des statistiques sur les médias et les tweets, et d'accéder aux informations de profil utilisateur.

L'utilisation de l'API Twitter nécessite la création d'un compte développeur Twitter et la création d'une application. L'application doit être associée à des clés et des jetons d'authentification pour accéder aux données de Twitter. Les développeurs doivent également se conformer aux règles et aux limites d'utilisation de l'API Twitter, telles que les limites de taux d'appels et les restrictions sur l'utilisation des données de Twitter.

L'API Twitter est utilisée dans de nombreuses applications et services, tels que les outils de gestion de réseaux sociaux, les applications de veille et de surveillance, les services d'analyse et de visualisation de données, les bots de conversation, etc.


![](img/twitter_api.jpg)



## Information du projet

- Contributeur du projet : Antonin
- Date de la dernière mise à jour : 04 mars 2023


## Installation

### Prérequis du projet
- Création d'un compte développeur Twitter et obtenir des clés d'API pour accéder à l'API Twitter.
- [Python 3.6 ou supérieur](https://www.python.org/downloads/)
- Tweepy
- NLTK


### Créer un compte développeur Twitter et obtenir des clés d'API pour accéder à l'API Twitter.
Pour récupérer les clés et les jetons d'authentification de l'API Twitter, vous devez suivre les étapes suivantes :
- Créez un compte développeur Twitter si vous n'en avez pas déjà un. Vous pouvez le faire en allant sur le site [https://developer.twitter.com/en/apps](https://developer.twitter.com/en/app) et cliquez sur "Create an app" puis sur "Apply".
- Remplissez les informations demandées pour votre compte de développeur et cliquez sur "Let's do this".
- Acceptez les conditions d'utilisation et cliquez sur "Submit".

### Projet sur Git
Le projet est disponible sur le site [Github](https://github.com/) sur le lien : [https://github.com/antoningr/API_Twitter](https://github.com/antoningr/API_Twitter). 


### Téléchargement du projet
- Ouvrez votre terminal ou invite de commandes.
- Allez dans le répertoire où vous souhaitez enregistrer le projet.
- Tapez la commande suivante pour cloner le projet depuis le dépôt Git :
```
git clone https://github.com/antoningr/API_Twitter.git
```
- Appuyez sur "Entrée" pour lancer la commande. Git va alors télécharger le projet dans le répertoire actuel.


### Configuration du projet
Modifier le fichier de configuration config.py dans le répertoire principal du projet et ajoutez-y les clés d'API de Twitter sous la forme suivante :
```
consumer_key = "votre_consumer_key"
consumer_secret = "votre_consumer_secret"
access_token = "votre_access_token"
access_token_secret = "votre_access_token_secret"
```

### Exécution du projet
- Ouvrez une invite de commande ou une fenêtre de terminal.
- Naviguez vers le répertoire racine de l'application où se trouve le fichier main.py.
- Exécutez la commande suivante pour démarrer l'application web :
```
python main.py
```

![](img/logo_twitter.png)
