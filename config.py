import sys
bookId = 9267
chapter = 1
useChapter = int(sys.argv[1]) if len(sys.argv) > 1 else chapter
pageIndex = 188063 + useChapter
counter = pageIndex % 188063
url = "https://www.zhonghuadiancang.com/waiguomingzhu/%d/%d.html" % (bookId, pageIndex)

print(url)