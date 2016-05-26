import scrapy

class ScrapeYelpSpider(scrapy.Spider):
    name = 'yelp'
    start_urls = []

    skip_flag = True

    def get_sub(self, string, sub):
        idx = string.find(sub)
        if idx != -1:
            return string[idx+len(sub):idx+len(sub)+12]

    with open('businesses.txt', 'r') as myfile:
        for line in myfile.readlines():
            items = line.split(',')
            url = items[3].strip()
            start_urls.append('https://www.yelp.com/biz/' + url + '?sort_by=date_asc')
            start_urls.append('https://www.yelp.com/biz/' + url + '?sort_by=date_desc')

    def parse(self, response):
        filename = 'data/' + response.url.split('/')[-1].split('?')[0] + '.txt'
        if self.skip_flag:
            price_range = response.xpath('//span[@class="business-attribute price-range"]/text()').extract()
            business_info = response.xpath('//div[@class="short-def-list"]/dl/*[self::dt or self::dd]/text()').extract()
            cuisine_type = response.xpath("//div[@class='biz-page-header clearfix']/div[@class='biz-page-header-left']/div[@class='biz-main-info embossed-text-white']/div[@class='price-category']/span[@class='category-str-list']//text()").extract()
            oldest_review = response.xpath("//ul[@class='ylist ylist-bordered reviews']/li[2]/div[@class='review review--with-sidebar']/div[@class='review-wrapper']/div[@class='review-content']/div[@class='biz-rating biz-rating-very-large clearfix']/span[@class='rating-qualifier']").extract()

            #clean up cuisine_type 
            cuisines = [t.strip(' \n,') for t in cuisine_type if t.strip(' \n,')]

            #clean up review date
            rev = self.get_sub(oldest_review[0], 'content=').strip('"')

            #clean up business info
            business_info = [x.strip(' \n') for x in business_info]


            with open(filename, 'wb') as myfile:
                myfile.write(price_range[0])
                myfile.write('\n')
                for c in cuisines:
                    myfile.write(c + ' ')
                myfile.write('\n')
                it = iter(business_info)
                for prop, info in zip(it, it):
                    myfile.write(prop + ": " + info + "\n")
                myfile.write(rev + '\n')
            self.skip_flag = not self.skip_flag
        else:
            newest_review = response.xpath("//ul[@class='ylist ylist-bordered reviews']/li[2]/div[@class='review review--with-sidebar']/div[@class='review-wrapper']/div[@class='review-content']/div[@class='biz-rating biz-rating-very-large clearfix']/span[@class='rating-qualifier']").extract()

            rev = self.get_sub(newest_review[0], 'content=').strip('"')
            
            with open(filename, 'a') as f:
                f.write(rev + '\n')

            self.skip_flag = not self.skip_flag
