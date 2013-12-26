# Scrapy settings for hn project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'hn'

SPIDER_MODULES = ['hn.spiders']
NEWSPIDER_MODULE = 'hn.spiders'

DATABASE = {'drivername': 'sqlite',
            'database': 'dev.db'}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hn (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'hn.pipelines.HnPipeline': 300
}
