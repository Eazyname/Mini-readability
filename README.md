# Mini-readability
Тестовое задание Тензор

Данный код позволяет получить текст с практически любой новостной статьи. для запуска нужно указать в качестве параметра URL адрес на страницу. 
Отдельный файл "Help_teg" cлужит для настройки поиска по тегам/классам интересующий нам текст.


Проверенно на таких ссайтах как:
1) https://www.rbc.ru/economics/01/04/2022/62470fee9a79476ff43e090c?from=newsfeed
2) https://lenta.ru/news/2022/04/01/razminirovanie/
3) https://news.ru/world/axios-psaki-planiruet-pokinut-dolzhnost-press-sekretarya-belogo-doma/
4) https://ria.ru/20220401/ovoschi-1781299976.html
5) https://www.gazeta.ru/social/news/2022/04/01/17510491.shtml
6) https://www.vesti.ru/article/2696993
7) https://news.rambler.ru/incidents/48405024-ukraina-otkazalas-podtverdit-prichastnost-k-aviaudaru-po-neftebaze-v-belgorode/
8) https://www.interfax.ru/world/832683
9) https://smotrim.ru/article/2697608?utm_source=sidebar

Код вполне работоспособен на практически любом новостном сайте.

Результаты работы есть в папке Example


В дальнейшем для улучшении кода, стоит прописать больше проверок на валидность URL, лучше фильтровать. 
Некоторые сайты более хорошо перехватывают парсеры, нужно более продумать пути отхода. Например с помощью Selenium.
Можно заняться более глубоким редактирование текста: разный шрифт,размер и т.д

Также для улучшения кода, можно применять API, что будет более надежным решением, если на сайте будут какие-то изменения.
