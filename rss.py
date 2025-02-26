# read the feeds.opml file and return the list of feeds
# in the form of a dictionary
import feedparser
from datetime import datetime
import google.generativeai as genai
import os
import time
import xml.etree.ElementTree as ET
# Use sqlite3 to store the feed data

import sqlite3

def read_opml(opml_file):
    """
    Reads an OPML file and extracts the text attributes of outlines and their child outlines.

    Args:
        opml_file (str): The path to the OPML file.

    Returns:
        dict: A dictionary where keys are parent outline texts and values are lists of child outline texts.
    """
    tree = ET.parse(opml_file)
    root = tree.getroot()
    outlines = {}

    for parent_outline in root.findall('.//outlines'):
        parent_text = parent_outline.get('text')
        if parent_text:
            child_texts = []
            for child_outline in parent_outline.findall('./outline'):
                print(child_outline)
                child_text = child_outline.get('xmlUrl')
                child_title = child_outline.get('title')
                child_type = child_outline.get('type')
                if child_text:
                    child_texts.append([child_text, child_title, child_type])
            outlines[parent_text] = child_texts

    return outlines

opml_file = 'feeds.opml'
outlines = read_opml(opml_file)
# 获取当前时间
now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
for parent, children in outlines.items():
    print(f"Parent: {parent}")
    for child in children:
        url = child[0]
        title = child[1]
        type = child[2]
        print(f"Child: {url}")
        if(type != 'rss'):
            continue
        #exit()
        # use feedparser to get the feed data
        feed = feedparser.parse(url)
        # create a md file for each feed
        # get the feed title
        feed_title = feed.feed.title
        # get the feed updated time
        feed_updated = feed.feed.updated
        # get the feed entries
        feed_entries = feed.entries
        # create a md file
        # get the current time
        current_time = datetime.now()

        today = datetime.utcnow().strftime('%Y-%m-%d')

        # create a file name
        file_name = f"{feed_title} {today}.md"
        # create a file path
        file_path = os.path.join('source/_posts/rss', file_name)
        # open the file
        with open(file_path, 'w') as f:
            # f.write(f"# {feed_title}\n")
            # f.write(f"Last Updated: {feed_updated}\n")
            
            # nextjs-blog template
            f.write("---\n")
            f.write(f"title: {title} for {today}\n")
            f.write(f"date: {now}\n")
            f.write("lang: en\n")
            f.write("categories: {parent}\n")
            f.write("sitemap: true\n")
            f.write("comments: true\n")
            f.write("---\n\n")

            f.write(f"## {feed_title}\n")
            f.write(f"Last Updated: {feed_updated}\n")


            for entry in feed_entries:
                print(entry)
                entry_title = entry.title
                entry_link = entry.link
                entry_published = entry.published
                entry_content = entry.content[0].value
                entry_content = entry_content.encode('utf-8').decode('utf-8')
                f.write(f"## {entry_title}\n")
                f.write(f"Published: {entry_published}\n")
                f.write(f"{entry_content}\n")

                # entry_link add utm_source=feed&utm_medium=rss&utm_campaign=feed
                entry_link = entry_link + "?utm_source=models.net.cn&utm_medium=rss&utm_campaign=feed"

                f.write(f"[Read More]({entry_link})\n")
        exit()
