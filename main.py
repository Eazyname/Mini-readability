import sys
import os
from bs4 import BeautifulSoup as bs4
from fake_useragent import UserAgent
import requests
from help_teg import Rus_News
from textwrap import wrap


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


def link_replace(link):
    if "http" not in link:
        domen_news = url.split("/")
        return "//".join(domen_news[0:3:2]) + link
    return link


class Cleaning:
    def clear_article_text(self):
        for i, elem in enumerate(self.clean_article_text()):
            if hyperlinks := elem.find_all('a'):
                for links in hyperlinks:
                    href_url = link_replace(links.get('href'))
                    total = f"{links.text} [{href_url}]"
                    self.clean_article[i] = \
                        self.clean_article[i].replace(links.text, total)


class Article(Cleaning):
    def __init__(self, parse):
        self.parse = bs4(parse.text, 'html.parser')
        self.name = url.split("/")[2]
        self.headline = self.parse.h1.text.strip()

    def article_text(self):
        if Rus_News[self.name] == "p":
            return self.parse.find_all(Rus_News[self.name])
        else:
            return self.parse.select(Rus_News[self.name])

    def clean_article_text(self):
        article = []
        for elem in self.article_text():
            if len(elem.text) > 10:
                article.append(elem)
        return article

    def convert_to_text(self):
        to_text = []
        for elem in self.clean_article_text():
            to_text.append(elem.text)
        self.clean_article = to_text


NEWS = Article(response)
NEWS.convert_to_text()
NEWS.clear_article_text()

file_name = "-".join(url.split("/")[2:-1]) + ".txt"
surent_dir = os.getcwd()

with open(file_name, "w", encoding=encoding) as file:
    file.write(NEWS.headline + "\n" + "\n")
    for lines in NEWS.clean_article:
        texts = wrap(lines, 80)
        for word in texts:
            file.write(word+"\n")
        else:
            file.write("\n")


print("Запись в файл прошла успешна")
print(f"Дирректория: {surent_dir}")
print(f"Имя файла: {file_name}")
