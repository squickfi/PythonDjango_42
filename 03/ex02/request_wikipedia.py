import requests
import json
import dewiki
import sys


def request_wiki(page: str):
    url = 'https://en.wikipedia.org/w/api.php'
    parameters = {
        'action': 'parse',
        'page': page,
        'prop': 'wikitext',
        'format': 'json',
        'redirects': 'true',
        "formatversion": 2
    }
    try:
        r = requests.get(url=url, params=parameters)
        r.raise_for_status()
        page_data = json.loads(r.text)
        if page_data.get('error'):
            raise Exception(page_data['error']['info'])
    except Exception as e:
        raise e
    return dewiki.from_string(page_data['parse']['wikitext'])


def get_page():
    if len(sys.argv) != 2:
        print('You need one argument: title')
        return
    try:
        page_data = request_wiki(sys.argv[1])
        file = open(sys.argv[1] + '.wiki', 'w')
        file.write(page_data)
        file.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_page()
