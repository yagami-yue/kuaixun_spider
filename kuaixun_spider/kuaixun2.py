# _*_  coding:utf-8  _*_
# @ 功能描述：爬每个链接的内容
# @ Time： 2021/1/21 13:54
# @ 作者：yagami_yue
# @ 版本信息：0.0.1
import re
from urllib import request
from urllib.error import HTTPError
import pymysql


if __name__ == '__main__':
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',  # 用户名
        password='',  # 密码
        database='test',  # 数据库的名字
        charset='utf8')
    with open('url.txt', 'r') as f:
        for url in f.readlines():
            try:
                html = request.urlopen(url).read().decode('utf-8')
            except HTTPError:
                with open('error.txt', 'a') as f:
                    f.write(url)
                    f.write('\n')
            else:
                title_pat = re.compile(r'<h1>(.*?)</h1>')
                abstract_pat = re.compile(r'<div class="b-review">(.*?)</div>')
                content_pat = re.compile(u'<!--文章主体-->([\d\D]*)<!--责任编辑-->')
                publish_time_pat = re.compile(r'<div class="time">([\d\D]*?)</div>')
                content_clean_pat = re.compile(r'<[\d\D]*?>')
                title = title_pat.findall(html)[0]
                abstract = abstract_pat.findall(html)[0]
                publish_time = publish_time_pat.findall(html)[0]
                content = content_pat.findall(html)[0]
                content_clean = re.sub(content_clean_pat, '', content)
                content_clean = re.sub(r'[\s|\t]', '', content_clean)
                cursor = conn.cursor()
                # print(url)
                sql = "INSERT INTO kuaixun ( url, publish_time, title, abstract, content ) " \
                      "VALUES ( '{}', '{}', '{}', '{}', '{}' );".format(url, publish_time, title, abstract, content_clean)
                print(sql)
                cursor.execute(sql)  # 执行单条SQL语句
                print(url)
                print(publish_time)
                print(title)
                print(abstract)
                print(content_clean)
    conn.commit()  # 提交事务
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库游标
    # # print(html)
    # print(publish_time)


