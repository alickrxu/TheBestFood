import scrapy
import pickle

class ScrapeYelpSpider(scrapy.Spider):
    name = 'yelp'
    start_urls = []
    with open('businesses.txt', 'r') as myfile:
        for line in myfile.readlines():
            items = line.split(',')
            url = items[3].strip()
            start_urls.append('https://www.yelp.com/biz/' + url + '?sort_by=date_asc')

    def parse(self, response):
        filename = 'data/' + response.url.split('/')[-1].split('?')[0] + '.txt'
        price_range = response.xpath('//span[@class="business-attribute price-range"]/text()').extract()
        business_info = response.xpath('//div[@class="short-def-list"]/dl/*[self::dt or self::dd]/text()').extract()
        oldest_review = response.xpath("//ul[@class='ylist ylist-bordered reviews']/li[2]/div[@class='review review--with-sidebar']/div[@class='review-wrapper']/div[@class='review-content']/div[@class='biz-rating biz-rating-very-large clearfix']/span[@class='rating-qualifier']").extract()

        print oldest_review

        business_info = [x.strip(' \n') for x in business_info]

        #TODO pickle
        #data = {'price_range': price_range, 'business_info' : business_info, 'oldest_review' : oldest_review}

        with open(filename, 'wb') as myfile:
            myfile.write(price_range[0])
            myfile.write('\n')
            it = iter(business_info)
            for prop, info in zip(it, it):
                myfile.write(prop + ": " + info + "\n")
            myfile.write(oldest_review[0])
