import requests
from bs4 import BeautifulSoup


def get_definition(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.p.get_text()

def term_to_wiki_url(term: str) -> str:
    return "https://ru.wikipedia.org/wiki/" + term.replace(' ', '_')
