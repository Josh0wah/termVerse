import requests
from bs4 import BeautifulSoup

def fetchContent(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Could not fetch from ", url, "\n")
    return requests.get(url)

def getVerse(url):
    content = fetchContent(url).text
    soup = BeautifulSoup(content, features = "html.parser")
    verse = soup.find("div", class_ = "bilingual-left").text

    return verse

def main():
    url = "https://www.verseoftheday.com/"
    verse = getVerse(url)
    print("Verse of the day: ", verse, "\n")

if __name__ == "__main__":
    main()
