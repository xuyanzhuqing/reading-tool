#!/Users/michael/.pyenv/shims/python
# https://zhuanlan.zhihu.com/p/32675668
import os
import requests
import codecs
from bs4 import BeautifulSoup

from config import url, counter

fileName = '0' + str(counter) if counter < 10 else str(counter)
dest = fileName + '.txt'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
headers = {'User-Agent':user_agent}
r = requests.get(url, headers = headers)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')

header = soup.find('h1')
content = soup.find('div', { 'id': 'content' })

f = codecs.open(dest, 'w', encoding='utf-8')
fc = codecs.open('00.txt', 'w+', encoding='utf-8')

txt = '\n'.join([header.text, content.text, header.text + '结束'])
f.write(txt)
fc.write(txt)

f.close()
fc.close()

os.system('ls *.txt')