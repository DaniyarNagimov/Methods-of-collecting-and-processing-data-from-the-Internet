import requests
from lxml import html

""" 
Написать приложение, которое собирает основные новости с сайтов mail.ru, lenta.ru, yandex-новости.
 Для парсинга использовать XPath. Структура данных должна содержать:
    название источника;
    наименование новости;
    ссылку на новость;
    дата публикации.
"""


def search_news():
    data = {}
    num = 0
    session = requests.session()
    url = 'https://lenta.ru/rubrics/economics/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.82 Safari/537.36', }
    request = session.get(url, headers=headers)
    root = html.fromstring(request.text)
    news_links = root.xpath("//div[@class='item article' or @class='item news b-tabloid__topic_news']/"
                            "a[@class='titles']/@href")
    news_names = root.xpath("//div[@class='item article' or @class='item news b-tabloid__topic_news']/"
                            "a[@class='titles']//h3[@class='rightcol' or @class='card-title']/text()")
    news_dates = root.xpath("//div[@class='item article' or @class='item news b-tabloid__topic_news']//"
                            "span[@class='g-date item__date']/text()")

    for name in news_names:
        data[name] = f'https://lenta.ru{news_links[num]}', news_dates[num]
        num += 1

    return data


for el in search_news():
    print(el)
    for item in search_news()[el]:
        print(item)
    print('-' * 30)
