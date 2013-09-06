# Scrapy baiduPipelineettings for newsbaidu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'newsbaidu'

SPIDER_MODULES = ['newsbaidu.spiders']
NEWSPIDER_MODULE = 'newsbaidu.spiders'

ITEM_PIPELINES = ['newsbaidu.pipelines.NewsbaiduPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newsbaidu (+http://www.yourdomain.com)'
