import feedparser
from datetime import datetime
import google.generativeai as genai
import os
import time
# Use sqlite3 to store the feed data

import sqlite3

# Connect to the database

conn = sqlite3.connect('rss.db')

# configure the sqlite password

# Create a cursor

c = conn.cursor()

# Create a table
# if the table exists, it will not create the table again
if c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='rss'").fetchone() is None:
    c.execute("""CREATE TABLE rss (
        title text,
        link text,
        published text,
        ai_generated_content text
    )""")
    conn.commit()
    print("Table created")


# Use the Google AI API to generate content for the feed


genai.configure(api_key = os.environ['GOOGLE_AI_KEY'])

# @link https://ai.google.dev/gemini-api/docs/quickstart?lang=python
# model = genai.GenerativeModel("gemini-1.5-flash")
# use 1.0 pro model
model = genai.GenerativeModel("gemini-1.0-pro")

# response = model.generate_content("Write a story about a magic backpack.")
# print("AI generated content:")
# print(response.text)
# print("AI generated content:")


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
md_filename = f"source/_posts/rss/IT-security-{today}.md"

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

    # Rss Ai generated content only 1 article

    
    # 遍历 RSS feed 条目
    for entry in feed.entries:

        # 写入条目标题
        md_file.write(f"## {entry.title}\n")
        # 写入条目链接
        md_file.write(f"[Read more]({entry.link})\n\n")
        # 写入日期

        # check the database if the entry exists use link as the key
        res = c.execute("SELECT * FROM rss WHERE link = ?", (entry.link,))

        print("item from the database" + str(res))
        print(res)
        
        #print(entry.published)

        md_file.write(f"Published: {entry.published}\n\n")
        # 写入条目摘要
        # md_file.write(f"{entry.summary}\n\n")

        # Ai generated content by Google use the title as the prompt
        try:
            # if the entry does not exist sqlite db by the link
            if res.fetchone() is None:
                # when the ai_generated_content is None, generate the content
                response = model.generate_content(entry.title)
                md_file.write(f"{response.text}\n\n")
                # if the entry does not exist, insert it into the database

                # c.execute("INSERT INTO rss VALUES (`title`, `link`, `published`, `ai_generated_content`)", (entry.title, entry.link, entry.published, response.text))
                # conn.commit()

                # generate the content and save it to a new md file
                #write_md(md_filename, entry.title, today, now)
                time.sleep(3)
            else:
                if res.ai_generated_content is None:

                    print("AI generated content is None")
                    print("Generating content" + entry.title)
                    response = model.generate_content(entry.title)
                    print("AI generated content:")
                    print(response.text)

                    md_file.write(f"{response.text}\n\n")
                    # if the entry does not exist, insert it into the database
                    # update the ai_generated_content
                    # c.execute("UPDATE rss SET ai_generated_content = ? WHERE link = ?", (response.text, entry.link))
                    # # c.execute("INSERT INTO rss VALUES (?, ?, ?, ?)", (entry.title, entry.link, entry.published, response.text))
                    # conn.commit()
                    
                    time.sleep(3)
                else:
                    md_file.write(f"{res.ai_generated_content}\n\n")
                    time.sleep(3)
                # md_file.write(f"{res.ai_generated_content}\n\n")
            #datetime.sleep(3)
        except Exception as e:
            print("Error in generating content")
            print(e)


print(f"RSS feed has been converted to Markdown and saved as {md_filename}")

RSS_FEED_URL = "https://www.techtarget.com/searchcio/rss/Schooled-in-AI-Podcast-Feed.xml"

feed = feedparser.parse(RSS_FEED_URL)

md_filename = f"source/_posts/rss/Schooled-in-AI-Podcast-Feed-{today}.md"

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

            res = c.execute("SELECT * FROM rss WHERE link = ?", (entry.link,))

            # if res.fetchone() is None:
            #     c.execute("INSERT INTO rss VALUES (`title`, `link`, `published`, `ai_generated_content`)", (entry.title, entry.link, entry.published, None ))
            #     conn.commit()


            

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
md_filename = f"source/_posts/rss/Models.com-{today}.md"

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

        res = c.execute("SELECT * FROM rss WHERE link = ?", (entry.link,))

        # if res.fetchone() is not None:
        #     c.execute("INSERT INTO rss VALUES (`title`, `link`, `published`, `ai_generated_content`)", (entry.title, entry.link, entry.published, None ))
        #     conn.commit()

        # 写入条目标题
        md_file.write(f"## {entry.title}\n")
        # 写入条目链接
        md_file.write(f"[Read more]({entry.link})\n\n")
        # 写入日期
        # print(entry.published)
        md_file.write(f"Published: {entry.published}\n\n")
        # 写入条目摘要

        entry.description = entry.description.replace("500w.jpg", "800w.jpg")

        md_file.write(f"{entry.description}\n\n")

print(f"RSS feed has been converted to Markdown and saved as {md_filename}")

# write the feed to a markdown file
def write_md(filename, title, today, now):
    with open (filename, "w", encoding="utf-8") as md_file:
        md_file.write("---\n")
        md_file.write(f"title: {title}\n")
        md_file.write(f"date: {now}\n")
        md_file.write("tags: [RSS, Models, Art, Brand]\n")
        md_file.write("lang: en\n")
        md_file.write("sitemap: true\n")
        md_file.write("comments: true\n")
        md_file.write("---\n\n")
    
        md_file.write(f"# {title}\n\n")
    
        for entry in feed.entries:
            md_file.write(f"## {entry.title}\n")
            md_file.write(f"[Read more]({entry.link})\n\n")

            # replace the description image url with 500w.jpg to 800w.jpg
            entry.description = entry.description.replace("500w.jpg", "800w.jpg")


            md_file.write(f"Published: {entry.published}\n\n")
            md_file.write(f"{entry.description}\n\n")


# https://wiki.swarma.org/api.php?hidebots=1&urlversion=1&days=30&limit=500&action=feedrecentchanges&feedformat=atom
RSS_FEED_URL = "https://wiki.swarma.org/api.php?hidebots=1&urlversion=1&days=30&limit=500&action=feedrecentchanges&feedformat=atom"

feed = feedparser.parse(RSS_FEED_URL)

md_filename = f"source/_posts/zh-CN/rss/Swarma-Wiki-{today}.md"

os.makedirs(os.path.dirname(md_filename), exist_ok=True)

with open(md_filename, 'w', encoding='utf-8') as md_file:
    md_file.write("---\n")
    md_file.write(f"title: Swarma Wiki for {today}\n")
    md_file.write(f"date: {now}\n")
    md_file.write("tags: [RSS, Swarma, Wiki, Knowledge]\n")
    md_file.write("author: Swarma\n")
    md_file.write("summary: Swarma Wiki RSS Feed\n")
    md_file.write("lang: zh-CN\n")
    md_file.write("categories: Swarma\n")
    md_file.write("sitemap: true\n")
    md_file.write("comments: true\n")
    md_file.write("---\n\n")

    md_file.write(f"# Swarma Wiki for {today}\n\n")

    for entry in feed.entries:

        res = c.execute("SELECT * FROM rss WHERE link = ?", (entry.link,))

        md_file.write(f"## {entry.title}\n")
        md_file.write(f"[Read more]({entry.link})\n\n")
        md_file.write(f"Updated: {entry.updated}\n\n")
        md_file.write(f"{entry.summary}\n\n")


# Close the connection
conn.close()