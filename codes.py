# 通过 xpath 获取豆瓣电影的信息

import requests
from lxml import etree

url = 'https://movie.douban.com/cinema/nowplaying/ningde/'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Referer': 'https://movie.douban.com/'
}

response = requests.get(url, headers=head)
response.encoding = 'utf-8'

resp_xp = etree.HTML(response.text)
# print(etree.tostring(resp_xp, encoding='utf-8').decode('utf-8'))
ul = resp_xp.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul, encoding='utf-8').decode('utf-8'))
lis = ul.xpath('./li')
# print(len(lis))  # 15个 说明都获取到了
result = []
for each in lis:
    movie_name = each.xpath('@data-title')
    movie_actors = each.xpath('@data-actors')
    movie_score = each.xpath('@data-score')
    movie_pic_src = each.xpath('./ul/li/a/img/@src')
    movie_info = {
        'movie_name': movie_name[0],
        'movie_actors': movie_actors[0],
        'movie_score': movie_score[0],
        'movie_pic_src': movie_pic_src[0]
    }
    result.append(movie_info)

for i in result:
    print(i)
