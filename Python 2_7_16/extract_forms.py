#! /usr/bin/python
"""A simple script to extract HTML forms.
   Uses Python 2.7.16"""

from bs4 import BeautifulSoup
import requests
import urlparse2
import optparse


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-t', '--target', dest='target', help='Target URL.')

    (options, arguments) = parser.parse_args()

    return options


def requests(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


options = get_arguments()

target_url = options.target
response = requests(target_url)

parsed_html = BeautifulSoup(response.content)
forms_list = parsed_html.findAll("form")

for form in forms_list:
    action = form.get('action')
    post_url = urlparse2.urljoin(target_url, action)
    method = form.get("method")

    inputs_list = form.findAll('input')
    post_data = {}

    for input in inputs_list:
        input_name = input.get('name')
        input_type = input.get('type')
        input_value = input.get('value')

        if input_type == 'text':
            input_value = 'test'
        post_data[input_name] = input_value

    result = requests.post(post_url, data=post_data)
    print(result.content)
