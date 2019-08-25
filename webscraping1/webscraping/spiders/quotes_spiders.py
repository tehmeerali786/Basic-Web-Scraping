import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = [

        'https://www.forbes.com/sites/steveodland/2012/10/04/my-favorite-quotes/#5b829d5f3890'

    ]

    def parse(self, response):

        for quote in response.css('div'):
            yield {

                'quote':quote.css('p::text').extract(),
            }
