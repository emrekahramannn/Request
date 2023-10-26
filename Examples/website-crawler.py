# HTML PARSING
import requests
from requests.exceptions import HTTPError, ConnectionError
from bs4 import BeautifulSoup   # html / xml parsing library


# Making a map of a website
"""
when we make a request to a website it returns us HTML codes
All HTML tags (link, a, etc. tag) has a attribute called href
"""

target_url = "https://atilsamancioglu.com"

def make_request(url):

    response = requests.get(url)
    # print(response.text)      returns HTML codes in a string format

    soup = BeautifulSoup(response.text, "html.parser")
    return soup


# HTML PARSING
# HTML Sayfası İçerisinden Linkleri Almak (<a href=""></a>) 
# Read -> how to extract urls from html code python (bs4, BeautifulSoup)

# soup = BeautifulSoup(response.text, "html.parser") # features="lxml" de verilebilir

# Parse ile edinilen aynı bilgileri (aynı linkleri) tekrar göstermemesi için:
foundLinks = []

def crawl(url):
    links = make_request(url)
    for link in links.find_all("a"):
        found_link = link.get("href")
        if found_link:
            if "#" in found_link:
            # to handle page-in links
                found_link = found_link.split("#")[0]
            if target_url in found_link and found_link not in foundLinks:
                foundLinks.append(found_link)
                print(found_link)
                # recursive call: to get other links found in this link's page
                crawl(found_link)


crawl(target_url)