#!/Users/michael/.pyenv/shims/python
# https://zhuanlan.zhihu.com/p/32675668
import os
import requests
import codecs
from bs4 import BeautifulSoup
from config import url, counter, settingUrl, tmpDir

# 读取网页并解析
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
headers = {'User-Agent':user_agent}
r = requests.get(url, headers = headers)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')

# 找到文章标题，内容
header = soup.find('h1')
content = soup.find('div', { 'id': 'content' })

# 写入文件
fileName = '0' + str(counter) if counter < 10 else str(counter)
dest = fileName + '.txt'

f = codecs.open(dest, 'w', encoding='utf-8')
fc = codecs.open('00.txt', 'w+', encoding='utf-8')
tailShell = ' && '.join(['cd "%s"' % (os.getcwd()), "python ./next.py " + str(counter + 1)])
txt = '\n'.join([
  header.text,
  content.text,
  header.text + '结束',
  tailShell
])
f.write(txt)
fc.write(txt)
f.close()
fc.close()

# 将页码切换到第1页

shell = 'jq --indent 4 \'setpath(["thiefBook.currPageNumber"]; 1)\' {0} > {1} && mv {1} {0}'.format(settingUrl, tmpDir)
os.system(shell)

# 复制命令到命令行中
print(tailShell)

# 展示当前存在的章节
os.system('ls *.txt')