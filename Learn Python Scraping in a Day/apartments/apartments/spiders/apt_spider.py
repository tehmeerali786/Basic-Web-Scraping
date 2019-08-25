from bs4 import BeautifulSoup

import scrapy
from apartments.items import City

class AptSpider(scrapy.Spider):
    name = "apts"
    start_urls = ['https://www.craigslist.org/about/sites']

    def parse(self, request):
        soup = BeautifulSoup(response.body, 'html.parser')

        for country_heading in soup.findAll('h1'):
            country_name = country_heading.text
            country_content = country_heading.find_next_sibling('div')
            region_heading = country_content.findAll('h4')

            for region_heading in region_headings:
                ul = region_heading.find_next_sibling('ul')
                links = ul.findChildren('a')

                for link in links:
                    city = City(


                        country = country_heading.text,
                        region = region_heading.text,
                        name = link.text,
                        url = link.attrs['href']

                            )

                    request = scrapy.Request(link.attrs['href'], callback= self.parse_city)

                    request.meta['item'] = extra
                    yield request

        def parse_city(self, response):

            soup = BeautifulSoup(response.body, 'html.parser')
            housing = soup.find('div', attrs = {'class' : 'housing'})
            all_apts = soup.find('a', text='all apartments')

            if housing:

                url = housing.findChild('a', attrs={'class' : 'apa'}).attrs['href']

                full_url = response.urljoin(url)
                request = scrapy.Request(full_url, callback = self.parse_listings)

            elif all_apts:

                full_url = response.urljoin(all_apts.attrs['href'])
                request = scrapy.Request(full_url, callback = self.parse_listings)

            else:

                option = soup.find('option', text = 'english')
                full_url = response.urljoin(option.attrs['value'])
                request = scrapy.Request(full_url, callback = self.parse_city)

            request.meta['item'] = response.meta['item']
            request.meta['item']['url'] = full_url
            yield request

        def parse_listings(self, response):

            soup = BeautifulSoup(response.body, 'html.parser')
            city = response.meta('item')

            price_spans = soup.select('span.price')
            prices = [int(span.text[1:]) for span in price_spans]
            city['prices'] = filter(lambda x: 100 < x < 1000, prices)

            yield data
