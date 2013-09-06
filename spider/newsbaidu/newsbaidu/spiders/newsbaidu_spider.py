
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from newsbaidu.items import NewsbaiduItem
from newsbaidu.common import NewsItemInfo
from newsbaidu.common import md5
from time import sleep
import urlparse

class NewsBaiduSpider(CrawlSpider):
    name = "newsbaidu"
    allowed_domains = ["news.baidu.com"]
    pageNum = 10
    # tagclass = [	mil, finannews, internet, housenews, autonews, sportnews, enternews, gamenews, edunews, healthnews,   	technnews, socianews   ]

    start_urls = [
        "http://news.baidu.com/n?cmd=4&class=finannews&pn=1"
    ]


    rules = (
        Rule(SgmlLinkExtractor(allow='n\?cmd=4&class=(socianews|mil|finannews|internet|housenews|autonews|sportnews|enternews|gamenews|edunews|healthnews|technnews|socianews)&pn=\d+', tags='a'),
            callback='parse_list',follow=True
            ),
        )

    def get_tag_from_url(self, url):
        result = urlparse.urlparse(url)  
        params = urlparse.parse_qs(result.query,True) 
        return self.get_text_content(params['class'])

    def get_text_content(self, list):
        rstr = ''
        for item in list:
            rstr += item.strip()

        return rstr

    def parse_list(self,response):

        refer_url = response.url
        item = NewsbaiduItem()
        item['url'] = response.url
        item['contType'] = 'NewsItems'
        item['item_list'] = []
        tag = self.get_tag_from_url(refer_url)

        hxs = HtmlXPathSelector(response)

        newsCluster = hxs.select('//div/div/a[@mon]')
        for itr in newsCluster:
            nii = NewsItemInfo(refer_url)
            nii.url = self.get_text_content(itr.select('@href').extract())
            nii.title = self.get_text_content(itr.select('text()').extract())
            nii.id = md5(nii.url)
            nii.tag = tag


            item['item_list'].append(nii)
        

        return item

    
