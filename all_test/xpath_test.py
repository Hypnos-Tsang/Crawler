from scrapy import Selector
from all_test.request_test import Test


if __name__ == '__main__':
    url = "https://www.baidu.com/"
    params = {}
    test = Test(url, params)
    text = test.get_text()
    sel = Selector(text=text)
    name_xpath = "//*[@id='wrapper']//div//text()"
    tag_texts = sel.xpath(name_xpath).extract()
    for i in [i.strip() for i in tag_texts if not i.isspace()]:
        print(i)