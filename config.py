import sys
bookId = 9267
firstChapterId = 188063
settingUrl = '~/Library/Application\ Support/Code/User/settings.json'

# 可以忽略的设置
chapter = 1
useChapter = int(sys.argv[1]) if len(sys.argv) > 1 else chapter
pageIndex = firstChapterId + useChapter
counter = pageIndex % firstChapterId
url = "https://www.zhonghuadiancang.com/waiguomingzhu/%d/%d.html" % (bookId, pageIndex)
tmpDir = '/tmp/settings.json'

print(url)