# coding:utf8

from baike import url_manager, html_download, html_parser, html_outer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outer = html_outer.HtmlOuter()

    
    def craw(self, root_url):
        count = 1
        # 添加新的url
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                # 下载内容urllib2
                html_cont = self.downloader.download(new_url)
                # 解析网页beautifulSoup
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outer.collect_data(new_data)
                
                if count == 10:
                    break
                count = count + 1
            except BaseException, e:
                print 'craw failed'
                print e
        # 输出数据
        self.outer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    print 'done'