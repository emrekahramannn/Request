# Intro CyberSecurity
import requests
from requests.exceptions import HTTPError, ConnectionError 

# domain -> google.com      subdomain -> images.google.com / mail.google.com etc.

target_input = input("Enter your target website (domanin_name.extension): ")


def make_request(url):
    """
    try:
        response = requests.get(url)
    except HTTPError as http_err:
        print(f"HTTP ERROR: {http_err}")
    except ConnectionError as connect_err:
        print(f"CONNECTION ERROR: {connect_err}")
    except Exception as err:
        print(f"ERROR: {err}")
    else:
        print(response)
    """

    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


with open(file="subdomainlist.txt", encoding="utf-8", mode="r") as fhandle:
    for line in fhandle:            
        # line -> subdomain (word)
        subdomain = line.rstrip()
        # update url with input and subdomain
        url = "https://" +subdomain + "." + target_input
        # make a get request
        response = make_request(url)
        
        if response:    # -> if response is not None
            print("Found Subdomain ---> " + url)


txt = "test"
with open("facebook-subdomain.txt", "a") as fhandle:
    for i in range(500):
        fhandle.write(txt + str(i) +"\n")

with open("facebook-subdomain.txt", "r") as subdomain:
    for line in subdomain:
        sub = line.strip()
        url = "http://" + sub + ".facebook.com"

        response = make_request(url)

        if response:
            print("Successful request -->> " + url)