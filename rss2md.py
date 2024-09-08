import feedparser
from datetime import datetime

# RSS feed URL
RSS_FEED_URL = "https://www.computerweekly.com/rss/IT-security.xml"

# 解析 RSS feed
feed = feedparser.parse(RSS_FEED_URL)

# 获取当前日期import feedparser
from datetime import datetime
import os


# 获取当前日期
today = datetime.utcnow().strftime('%Y-%m-%d')

# Markdown 文件名
md_filename = f"source/_posts/IT-security_{today}.md"

# 确保目标目录存在
os.makedirs(os.path.dirname(md_filename), exist_ok=True)

# 打开 Markdown 文件进行写入
with open(md_filename, 'w', encoding='utf-8') as md_file:
    # 写入标题
    md_file.write(f"# RSS Feed for {today}\n\n")
    
    # 遍历 RSS feed 条目
    for entry in feed.entries:
        # 写入条目标题
        md_file.write(f"## {entry.title}\n")
        # 写入条目链接
        md_file.write(f"[Read more]({entry.link})\n\n")
        # 写入日期
        md_file.write(f"Published: {entry.pubDate}\n\n")
        # 写入条目摘要
        # md_file.write(f"{entry.summary}\n\n")

print(f"RSS feed has been converted to Markdown and saved as {md_filename}")
today = datetime.utcnow().strftime('%Y-%m-%d')

# Markdown 文件名
md_filename = f"IT-security_{today}.md"

# 打开 Markdown 文件进行写入
with open(md_filename, 'w', encoding='utf-8') as md_file:
    # 写入标题
    md_file.write(f"# RSS Feed for {today}\n\n")
    
    # 遍历 RSS feed 条目
    for entry in feed.entries:
        # 写入条目标题
        md_file.write(f"## {entry.title}\n")
        # 写入条目链接
        md_file.write(f"[Read more]({entry.link})\n\n")
        # 写入日期
        md_file.write(f"Published: {entry.pubDate}\n\n")
        # 写入条目摘要
        #md_file.write(f"{entry.summary}\n\n")

print(f"RSS feed has been converted to Markdown and saved as {md_filename}")