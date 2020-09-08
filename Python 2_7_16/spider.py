#! /usr/bin/python
"""A simple reverse backdoor script.
   Uses Python 2.7.16"""


import requests
import optparse
import urlparse
import re


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-t', '--target', dest='target', help='Target URL.')

    (options, arguments) = parser.parse_args()

    return options




def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)


def crawl(url):
    href_links = extract_links_from(url)

    for link in href_links:
        link = urlparse.urljoin(url, link) # will append target_url if missing from link

        if '#' in link:
            link = link.split('#')[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link) # recursively searches links


options = get_arguments()

target_url = options.target
target_links = []
crawl(target_url)