import sys
import requests
from bs4 import BeautifulSoup


class PhilosophyFinder:

    def __init__(self):
        self.titles = []

    def find_philosophy(self, title_str: str):
        url = f'https://en.wikipedia.org/{title_str}'
        try:
            r = requests.get(url)
            r.raise_for_status()
        except Exception as e:
            if r.status_code == 404:
                print("It\'s a dead end !")
                return
            print(e)
            return
        parser = BeautifulSoup(r.text, 'html.parser')
        title = parser.find(id='firstHeading').text
        if title in self.titles:
            print("It will become an infinite loop!")
            return
        self.titles.append(title)
        print(title)
        # print(self.titles)
        if title == 'Philosophy' and len(self.titles) > 1:
            print(f'{len(self.titles) - 1} roads from {sys.argv[1]} to philosophy')
            return
        content = parser.find(id='mw-content-text')
        all_links = content.select('p > a')
        for link in all_links:
            if link.get('href') is not None and link['href'].startswith('/wiki/') \
                    and not link['href'].startswith('/wiki/Wikipedia:') and not link['href'].startswith('/wiki/Help:'):
                self.find_philosophy(link['href'])
                return
        print("It\'s a dead end !")


def main():
    if len(sys.argv) != 2:
        print('You need one argument: title')
        return
    PhilosophyFinder().find_philosophy('/wiki/' + sys.argv[1])


if __name__ == '__main__':
    main()
