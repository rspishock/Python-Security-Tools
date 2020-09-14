#! /usr/bin/python
"""A class for the vulnerability scanner script.
   Uses Python 2.7.16"""

import requests
import urlparse2
import re

class Scanner:
    def __init__(self, url):
        self.target_url = url
        self.target_links = []

    def extract_links_from(self, url):
        response = requests.get(url)
        return re.findall('(?:href=")(.*?)"', response.content)

    def crawl(self, url):
        href_links = self.extract_links_from(self, url)

        for link in href_links:
            link = urlparse2.urljoin(url, link)  # will append target_url if missing from link

            if '#' in link:
                link = link.split('#')[0]

            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)  # recursively searches links
