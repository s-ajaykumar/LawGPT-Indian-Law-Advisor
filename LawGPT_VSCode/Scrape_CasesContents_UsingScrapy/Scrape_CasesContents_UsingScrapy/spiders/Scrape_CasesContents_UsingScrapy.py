import scrapy
class CaseDetails(scrapy.Spider):
    name = "CaseDetails"
    start_urls = ['https://indiankanoon.org/docfragment/52091592/?formInput=doctypes%3A%20chennai%20fromdate%3A%201-1-202%20todate%3A%2031-12-202']
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    
    def parse(self, response):
        
        p_tags_texts = response.xpath("//blockquote")
        print(p_tags_texts[:3])
        print("hi ")

"""'https://indiankanoon.org/docfragment/23969784/?formInput=doctypes%3A%20chennai%20fromdate%3A%201-1-202%20todate%3A%2031-12-202',
 'https://indiankanoon.org/docfragment/102815189/?formInput=doctypes%3A%20chennai%20fromdate%3A%201-1-202%20todate%3A%2031-12-202',
 'https://indiankanoon.org/docfragment/152517345/?formInput=doctypes%3A%20chennai%20fromdate%3A%201-1-206%20todate%3A%2031-12-206',
 'https://indiankanoon.org/docfragment/128046475/?formInput=doctypes%3A%20chennai%20fromdate%3A%201-1-680%20todate%3A%2031-12-680'"""

"""s = ''
        for p_tag_text in p_tags_texts:
            s += p_tag_text + '\n'
        
        yield {
            'input_ids' : s
        }"""