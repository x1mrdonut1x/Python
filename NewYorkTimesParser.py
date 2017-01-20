import requests
import datetime 
from bs4 import BeautifulSoup


def setup():
    """
    Requests url and returns the HTML as text
    """
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    r_html = r.text

    return r_html



def print_info():
    """
    Prints date, number of articles and all their titles
    """
    num = 0

    r_html = setup()

    soup = BeautifulSoup(r_html, "html.parser")
    divtag = soup.find_all("div", class_="page")
    
    for heading in divtag:
        headings = heading.find_all('h2', attrs={"class": "story-heading"})
        for title in headings:
            for string in title.stripped_strings:
                num += 1

        print(datetime.date.today())
        print("There are " + str(num) + " articles on the main page of The New York Times today.\n\n")

        for title in headings:
            for string in title.stripped_strings:
                print(string)

print_info()