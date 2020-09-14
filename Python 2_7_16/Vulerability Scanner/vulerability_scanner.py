#! /usr/bin/python
"""A simple vulnerability scanner script.
   Uses Python 2.7.16"""

import optparse
import scanner


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-t', '--target', dest='target', help='Target URL.')

    (options, arguments) = parser.parse_args()

    return options

options = get_arguments()
target_url = options.target

vuln_scanner = scanner.Scanner(target_url)
vuln_scanner.crawl(target_url)
