from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os
import requests

load_dotenv()

agent = os.getenv('agent')
url = os.getenv('url')

file = os.path.expanduser('~/Desktop/play_around/Projects/Affections/affections.txt')


def quote_scraper(url_, header_agent, file_):
    """Scrapes and formats quotes from the net"""

    header = {'User-Agent': header_agent}
    page = requests.get(url_, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')
    my_divs = soup.findAll("div", {"class": "quoteText"})

    with open(file_, 'w+') as f:
        for tags in my_divs:
            text = tags.get_text()
            text = text.strip().split()
            text = ' '.join(text).replace('“', '')
            text = text.replace('”', '')

            # write to file
            f.write(text + '\n')

    print('Finished writing to file')


if __name__ == '__main__':
    quote_scraper(url, agent, file)
