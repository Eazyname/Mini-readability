import sys
from bs4 import BeautifulSoup as bs4
from fake_useragent import UserAgent
import requests


if len(sys.argv) == 1:
    sys.exit("URL не указан")
else:
    url = sys.argv[1]

print(f"работаю над {url}")


ua = UserAgent(verify_ssl=True)
try:
    response = requests.get(url, headers={'User-Agent': ua.chrome})
    encoding = response.encoding  # Кодировка страницы
    if response.status_code == 200:
        print("Подключение успешно")
except ConnectionError:
    print("Сервер не отвечает")
    sys.exit("Повторите попытку позднее")



parser = bs4(response.text, 'html.parser')
body = parser.body
headline = body.h1.text  # Заголов статьи


def link_replace(link):
    if "http" not in link:
        domen_news = url.split("/")
        return "//".join(domen_news[0:3:2]) + link
    return link


class Cleaning():
    def clear_article_text(self):
        for i, elem in enumerate(self.clean_article_text()):
            hyperlinks = elem.find_all('a')
            if hyperlinks:
                for links in hyperlinks:
                    href_url = link_replace(links.get('href'))
                    hrew_text = links.text
                    total = f"{hrew_text} [{href_url}]"
                    self.clean_article[i] = \
                        self.clean_article[i].replace(hrew_text, total)


class Article(Cleaning):
    def __init__(self, url):
        self.url = url

    def article_text(self):
        return self.url.find_all('p')

    def clean_article_text(self):
        article = []
        for elem in self.article_text():
            if len(elem.text) > 80:
                article.append(elem)
        return article

    def convert_to_text(self):
        to_text = []
        for elem in self.clean_article_text():
                to_text.append(elem.text)
        self.clean_article = to_text


NEW = Article(parser)
NEW.convert_to_text()
NEW.clear_article_text()


with open("texst"+".txt", "w", encoding='utf-8') as file:
    #head = headline.center(len(headline) + 80-len(headline)//2, ' ')
    file.write(headline+"\n" + "\n")
    for i in NEW.clean_article:
        print(i)
        numer_word = 0
        word_list = []
        obz = []
        for sur,elem in enumerate(i.split()):
            if numer_word + len(elem) <= 80:
                word_list.append(elem)
                numer_word += len(elem)
                if len(i.split()) == sur+1:
                    obz.append(" ".join(word_list) + "\n")
            else:
                word_list.append(elem)
                obz.append(" ".join(word_list) + "\n")
                numer_word = 0
                word_list = []
        else:
            obz.append("\n")
        for ids in obz:
            file.write(ids)
