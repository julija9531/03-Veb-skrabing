import requests
# from bs4 import BeautifulSoup

import re
from pprint import pprint

if __name__ == '__main__':
    # определяем список ключевых слов
    KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'IT']

    #TODO 1: Скачивание HTML кода страницы

    url = 'https://habr.com/ru/all/'  # Адрес сайта для парсинга
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
    response = requests.get(url, timeout=30, headers=headers)
    html_text = response.text

    #TODO 2: Получаем список кодов статей

    post_list = re.findall('<article id=([\s\S.]*?)</article>', html_text, re.U)

    for post in post_list:


        #TODO 3: Получаем список тегов статьи

        # <div class=\"tm-article-snippet__hubs\">(.*?)</div>
        tags_html = re.findall('<div class=\"tm-article-snippet__hubs\">(.*?)</div>', post, re.U)


        # with open("03_html_tags.txt", "w", encoding='utf-8') as f:
        #     f.write(tags_html[0])
        tags_list = re.findall('<span>(.*?)</span>', tags_html[0], re.U)

        #TODO 4: Проверка наличия ключевых слов в тегах

        ind = False
        tag_text = ' '.join(tags_list)
        for keyword in KEYWORDS:
            if keyword in tag_text: ind = True

        #TODO 5: Определение даты публикации поста

        post_date = re.findall('<time datetime=\"(.*?)</time>', post, re.U)[0][:10]

        #TODO 6: Определение ссылки на пост

        post_link_html = re.findall('<h2 class=\"tm-article-snippet__title tm-article-snippet__title_h2\">(.*?)</h2>', post, re.U)[0]
        post_link = 'https://habr.com' + re.findall('<a href=\"(.*?)\"', post_link_html, re.U)[0]

        #TODO 7: Определение заголовка статьи

        post_name = re.findall('<span>(.*?)</span>', post, re.U)[0]

        #TODO 8: Вывод в консоль подходящих по тегам статей

        if ind: print(post_date + ' - ' + post_name + ' - ' + post_link)

        else:
        # TODO 9: Получаем ссылку на пост

            post_url = 'https://habr.com' + re.findall('<h2 class=\"tm-article-snippet__title tm-article-snippet__title_h2\"><a href=\"(.*?)\"', post, re.U)[0]

        # TODO 10: Скачивание HTML кода страницы поста

            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
            response2 = requests.get(post_url, timeout=30, headers=headers)
            post_html_text = response2.text

        # TODO 11: получение текста поста

            post_text_predv = re.findall('<div class=\"article-formatted-body([\s\S.]*?)<div class=', post_html_text, re.U)[0]

            ind2 = False
            for keyword in KEYWORDS:
                if (keyword) in post_text_predv:
                    ind2 = True

        # TODO 12: Вывод в консоль подходящих по содержанию статей

            if ind2: print(post_date + ' - ' + post_name + ' - ' + post_link)


