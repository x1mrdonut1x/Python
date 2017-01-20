import requests
import datetime 
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
divTag = soup.find_all("div", class_="page")



def print_Info():
    num = 0

    for heading in divTag:
        headings = heading.find_all('h2', attrs={"class": "story-heading"})
        for title in headings:
            for string in title.stripped_strings:
                num += 1

        print(datetime.date.today())
        print("There are " + str(num) + " articles on the main page of The New York Times today.\n\n")

        for title in headings:
            for string in title.stripped_strings:
                print (string)


print_Info()