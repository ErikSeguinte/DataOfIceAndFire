import scrapy

class BookSpider(scrapy.Spider):
    name = "books"
    start_urls = ['https://towerofthehand.com/books/guide.html']

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)