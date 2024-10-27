import scrapy

class ImdbspiderSpider(scrapy.Spider):
    name = "imdbspider"
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]
    page_count = 1
    max_pages = 10

    def parse(self, response):
        products = response.css('div.ui-search-result__wrapper.ui-search-result__wrapper')

        for product in products:
            prices = product.css('span.andes-money-amount__fraction::text').getall()
            cents = product.css('span.andes-money-amount__cents::text').getall()
            yield {
                'brand' : product.css('span.poly-component__brand::text').get(),
                'name' :  product.css('h2.poly-component__title a::text').get(),
                'reviews_rating_number' : product.css('span.poly-reviews__rating::text').get(),
                'review_amount' : product.css('span.poly-reviews__total::text').get(),
                'old_price': prices[0] if len(prices) > 0 else None,
                'old_price_cents': cents[0] if len(cents) > 0 else None,
                'new_price': prices[1] if len(prices) > 1 else prices[0] if prices else None,
                'new_price_cents': cents[1] if len(cents) > 1 else cents[0] if cents else None
            }
        
        if self.page_count < self.max_pages:
            next_page = response.css('li.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)

