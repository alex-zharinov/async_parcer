import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep_link in response.css('a.pep::attr(href)'):
            yield (response.follow(pep_link, callback=self.parse_pep))

    def parse_pep(self, response):
        name = response.css('h1.page-title::text').get()
        yield PepParseItem(
            {
                'number': int(name.split()[1]),
                'name': name,
                'status': response.css('dl abbr::text').get(),
            }
        )
