# -*- coding: utf-8 -*-

BOT_NAME = 'weibo'
SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'
COOKIES_ENABLED = False
LOG_LEVEL = 'ERROR'
# 访问完一个页面再访问下一个时需要等待的时间，默认为10秒
DOWNLOAD_DELAY = 10
DEFAULT_REQUEST_HEADERS = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cookie': 'SINAGLOBAL=6062109431611.069.1579247546940; '
              'UM_distinctid=16fbca0c85f2cb-0ad4b7b87f07f3-c383f64-1fa400-16fbca0c860287; '
              '_ga=GA1.2.1550551947.1584069331; UOR=,,www.baidu.com; wvr=6; '
              'login_sid_t=906e7d82e1351ba18d351a722bdee0ce; cross_origin_proto=SSL; _s_tentry=www.baidu.com; '
              'appkey=; Apache=9183487901430.918.1591776474799; '
              'ULV=1591776474888:69:3:2:9183487901430.918.1591776474799:1591603643696; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFuh7ccw65g5WTqVCzWOf7q5JpX5K2hUgL'
              '.Foq7e0zfeon7Sh22dJLoI7_F9PijIg42dNiDdntt; ALF=1623313593; SSOLoginState=1591777594; '
              'SCF=Al_-BjbprkAqAGufVLb3eivgXkku-onh-CxZoMYmZM2mZY30f1TsLsEcbn8I7u8i0goQ2iNeoybZx7oVBCLzG94.; '
              'SUB=_2A25z5OlqDeRhGeBO6FAU8ibMzz2IHXVQkF2irDV8PUNbmtANLVnWkW9NSgJ4015oqg0O9z-LrG_QcljCNbPMIrcs; '
              'SUHB=0nluCALL8t2Fu-; un=15652578277; '
              'webim_unReadCount=%7B%22time%22%3A1591777631051%2C%22dm_pub_total%22%3A5%2C%22chat_group_client%22'
              '%3A999%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A1047%2C%22msgbox%22%3A0%7D'
}
ITEM_PIPELINES = {
    'weibo.pipelines.DuplicatesPipeline': 300,
    'weibo.pipelines.CsvPipeline': 301,
    # 'weibo.pipelines.MysqlPipeline': 302,
    # 'weibo.pipelines.MongoPipeline': 303,
    # 'weibo.pipelines.MyImagesPipeline': 304,
    # 'weibo.pipelines.MyVideoPipeline': 305
}
# 要搜索的关键词列表，可写多个
KEYWORD_LIST = ['滑坡']
# 要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博
WEIBO_TYPE = 1
# 筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博
CONTAIN_TYPE = 0
# 筛选微博的发布地区，精确到省或直辖市，值不应包含“省”或“市”等字，如想筛选北京市的微博请用“北京”而不是“北京市”，想要筛选安徽省的微博请用“安徽”而不是“安徽省”，可以写多个地区，
# 具体支持的地名见region.py文件，注意只支持省或直辖市的名字，省下面的市名及直辖市下面的区县名不支持，不筛选请用”全部“
REGION = ['全部']
# 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期
START_DATE = '2020-03-01'
# 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期
END_DATE = '2020-03-02'
# 图片文件存储路径
IMAGES_STORE = './'
# 视频文件存储路径
FILES_STORE = './'
# 配置MongoDB数据库
# MONGO_URI = 'localhost'
# 配置MySQL数据库，以下为默认配置，可以根据实际情况更改，程序会自动生成一个名为weibo的数据库，如果想换其它名字请更改MYSQL_DATABASE值
# MYSQL_HOST = 'localhost'
# MYSQL_PORT = 3306
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = '123456'
# MYSQL_DATABASE = 'weibo'
