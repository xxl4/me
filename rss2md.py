import feedparser
from datetime import datetime
import google.generativeai as genai
import os


genai.configure(api_key = os.environ['GOOGLE_AI_KEY'])

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print("AI generated content:")
print(response.text)
print("AI generated content:")


# RSS feed URL
RSS_FEED_URL = "https://www.computerweekly.com/rss/IT-security.xml"

# 解析 RSS feed
feed = feedparser.parse(RSS_FEED_URL)

# 获取当前日期import feedparser
from datetime import datetime
import os


# 获取当前日期
today = datetime.utcnow().strftime('%Y-%m-%d')

# 获取当前时间
now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# Markdown 文件名
md_filename = f"source/_posts/IT-security-{today}.md"

# 确保目标目录存在
os.makedirs(os.path.dirname(md_filename), exist_ok=True)

# 打开 Markdown 文件进行写入
with open(md_filename, 'w', encoding='utf-8') as md_file:

    # nextjs-blog template
    md_file.write("---\n")
    md_file.write(f"title: IT Security RSS Feed for {today}\n")
    md_file.write(f"date: {now}\n")
    md_file.write("tags: [RSS, ComputerWeekly, IT Security]\n")
    md_file.write("author: ComputerWeekly\n")
    md_file.write("summary: IT Security RSS Feed\n")
    md_file.write("lang: en\n")
    md_file.write("categories: IT Security\n")
    md_file.write("sitemap: true\n")
    md_file.write("comments: true\n")
    md_file.write("---\n\n")

    # 写入标题
    md_file.write(f"# IT Security RSS Feed for {today}\n\n")


    
    # 遍历 RSS feed 条目
    for entry in feed.entries:
        # 写入条目标题
        md_file.write(f"## {entry.title}\n")
        # 写入条目链接
        md_file.write(f"[Read more]({entry.link})\n\n")
        # 写入日期

        #print(entry.published)

        md_file.write(f"Published: {entry.published}\n\n")
        # 写入条目摘要
        # md_file.write(f"{entry.summary}\n\n")

print(f"RSS feed has been converted to Markdown and saved as {md_filename}")

RSS_FEED_URL = "https://www.techtarget.com/searchcio/rss/Schooled-in-AI-Podcast-Feed.xml"

feed = feedparser.parse(RSS_FEED_URL)

md_filename = f"source/_posts/Schooled-in-AI-Podcast-Feed-{today}.md"

os.makedirs(os.path.dirname(md_filename), exist_ok=True)

with open(md_filename, 'w', encoding='utf-8') as md_file:
    
        md_file.write("---\n")
        md_file.write(f"title: Schooled in AI Podcast Feed for {today}\n")
        md_file.write(f"date: {now}\n")
        # Multiple tags
        md_file.write("tags: [AI, Podcast, RSS, TechTarget]\n")
        md_file.write("author: TechTarget\n")
        md_file.write("summary: Schooled in AI Podcast Feed\n")
        md_file.write("lang: en\n")
        md_file.write("categories: AI\n")
        md_file.write("sitemap: true\n")
        md_file.write("comments: true\n")
        md_file.write("---\n\n")
    
        md_file.write(f"# Schooled in AI Podcast Feed for {today}\n\n")
    
        for entry in feed.entries:
            md_file.write(f"## {entry.title}\n")
            md_file.write(f"[Read more]({entry.link})\n\n")
            md_file.write(f"Published: {entry.published}\n\n")
            md_file.write(f"Author: {entry.author}\n\n")
            md_file.write(f" > {entry.description}\n\n")
        
print(f"RSS feed has been converted to Markdown and saved as {md_filename}")

# read the feeds.opml file and extract the feed urls and make every feed to a markdown file

RSS_FEED_URL = "https://models.com/mdcdb/rss/output.xml"

feed = feedparser.parse(RSS_FEED_URL)


# Markdown 文件名
md_filename = f"source/_posts/Models.com-{today}.md"

# 确保目标目录存在
os.makedirs(os.path.dirname(md_filename), exist_ok=True)

# 打开 Markdown 文件进行写入
with open(md_filename, 'w', encoding='utf-8') as md_file:

    # nextjs-blog template
    md_file.write("---\n")
    md_file.write(f"title: Models.com {today}\n")
    md_file.write(f"date: {now}\n")
    md_file.write("tags: [RSS, Models, Art, Brand]\n")
    md_file.write("author: Models.com\n")
    md_file.write("summary: Models.com RSS Feed\n")
    md_file.write("lang: en\n")
    md_file.write("categories: Models\n")
    md_file.write("sitemap: true\n")
    md_file.write("comments: true\n")
    md_file.write("---\n\n")

    # 写入标题
    md_file.write(f"# Models.com for {today}\n\n")


    
    # 遍历 RSS feed 条目
    for entry in feed.entries:
        # 写入条目标题
        md_file.write(f"## {entry.title}\n")
        # 写入条目链接
        md_file.write(f"[Read more]({entry.link})\n\n")
        # 写入日期
        print(entry.published)
        md_file.write(f"Published: {entry.published}\n\n")
        # 写入条目摘要
        md_file.write(f"{entry.description}\n\n")

print(f"RSS feed has been converted to Markdown and saved as {md_filename}")
