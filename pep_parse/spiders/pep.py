import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_all = response.css('a.pep::attr(href)')

        for pep_link in pep_all:
            yield (response.follow(pep_link, callback=self.parse_pep))

    def parse_pep(self, response):
        name = response.css('h1.page-title::text').get()
        data = {
            'number': int(name.split()[1]),
            'name': name,
            'status': response.css('dl abbr::text').get(),
        }
        yield PepParseItem(data)
