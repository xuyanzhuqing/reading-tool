### 目的
本地查看中华典藏网书籍

### 功能
1. 爬取电子书到本地
2. 更新本地 thief-book 配置

### 准备工作
```bash

pip install requests
pip install beautifulsoup4
pip install lxml
```

### 配置
首选项 - 扩展 - thief-book - file-path(绝对路径)

### 使用
```bash
chmod 770 ./next.py
python .next.py # 查看第一章
python ./next.py [n] # 查看指定章节
```


