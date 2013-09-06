# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from newsbaidu.common import NewsItemInfo
import time


class NewsbaiduPipeline(object):
    
    item_filename = 'item.out.%s' %(time.strftime('%Y%m%d%H%M', time.localtime(time.time())))

    def process_item(self, item, spider):
        
        outfd = open(self.item_filename, 'ab')
        for info in item['item_list']:
  	        outfd.write(info.info_to_str() + '\n')
  	    
        outfd.close()
        #return item
