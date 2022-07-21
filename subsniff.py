# Subdomain Enumeration

import requests
import sys

subdomain_list = open("subdomains.txt").read()
subdomain = subdomain_list.splitlines()

for sub in subdomain:
    sub_domains = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domains)

    except requests.ConnectionError:
        pass

    else:
        print("Valid domain: ", subdomains)
