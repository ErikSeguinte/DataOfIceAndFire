import scrapy

class BookSpider(scrapy.Spider):
    name = "books"
    start_urls = ['https://towerofthehand.com/books/guide.html']

    def parse(self, response):
        # Follow links to books
        for title in response.css('.postmeta li:nth-child(3) a'):
            yield response.follow(title, self.parse_chapters)

    def parse_chapters(self, response):
        yield {
            'chapters' : response.css("h3 a::text").getall(),
            'scores' : response.css('.rightend a::text').getall()
        }