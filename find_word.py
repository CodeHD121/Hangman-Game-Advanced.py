import requests
from bs4 import BeautifulSoup


# Scraping a random word from a website designed for that in either German or English
def find_word(lang):
    def soupify_and_find(site):
        response = requests.get(site)
        soup = BeautifulSoup(response.content, 'html.parser')
        word = soup.find("div", style="font-size:3em; color:#6200C5;").text.strip()
        return word

    if lang == 1:
        wordSiteGer = "https://www.palabrasaleatorias.com/zufallige-worter.php"
        w = soupify_and_find(wordSiteGer)
        return w
    elif lang == 2:
        wordSiteEng = "https://www.palabrasaleatorias.com/random-words.php"
        w = soupify_and_find(wordSiteEng)
        return w