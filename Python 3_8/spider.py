


import urllib.parse as urlparse
import argparse
import requests
import re




def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target URL.')
    (options) = parser.parse_args()

    return options


def extract_links_from(url):
    response = requests(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors='ignore'))


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


options = get_arguments()                                                           # captures argument from terminal
target_url = options.target

target_links = []
crawl(target_url)