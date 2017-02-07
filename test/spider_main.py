# -*- encoding=UTF-8 -*-
from test import html_downloader
from test import html_outputer
from test import html_parser
from test import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' %(count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                count = count+1

                if count == 1000:
                    break
            except Exception as e:
                print 'craw failed'
                print e



        self.outputer.output_html()




if __name__ == "__main__":
    root_url = "http://baike.baidu.com/link?url=h1sYMJBXI7GZjuUOORYE9xZoJzq_ntRVoHHnFyqDYAqN_2GroibZ3FYMNl0v_9l6l7pmKjGe_3RFXaPsa3n87K"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)