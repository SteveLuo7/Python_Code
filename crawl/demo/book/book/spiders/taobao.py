# Importing necessary modules
import scrapy

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['s.taobao.com']
    start_urls = ['https://s.taobao.com/search?commend=all&ie=utf8&imgfile=&initiative_id=tbindexz_20170306&q=%E7%94%B7%E9%9E%8B&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201867-main.5.5af92a89AiAhCA&ssid=s5-e']

    def parse(self, response):
        # Extracting price information
        products = response.css('div.g-i-tile-i-box')
        for product in products:
            title = product.css('p.title::text').extract_first()
            price = product.css('strong.price::text').extract_first()

            yield {
                'title': title,
                'price': price,
            }

        # Follow pagination links
        next_page = response.css('a.J_Ajax:not([style*="none"])::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
