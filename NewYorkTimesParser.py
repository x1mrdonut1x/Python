import requests
import datetime 
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
headings = soup.find_all('h2', attrs={"class": "story-heading"})


def print_Info():
    num = 0

    for title in headings:
        for string in title.stripped_strings:
            num += 1

    print(datetime.date.today())
    print("There are " + str(num) + " articles on The New York Times today.\n\n")

    for title in headings:
        for string in title.stripped_strings:
            print (string)


print_Info()