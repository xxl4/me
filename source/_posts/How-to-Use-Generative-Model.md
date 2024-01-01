---
title: How to Use Generative Model in Python
tags:
  - Generative
  - Python
  - Rest
  - Google
  - MySQL
  - Redis
categories:
  - Technology
  - Python
date: 2024-01-01 09:23:12
description: How to Use Generative Model in Python
lang: en
comments: true
---
Today, i will use python language to use Google Generative AI. I will use mysql and redis for data storage.

.env
```
DB_CONNECTION = mysql
DB_HOST = 
DB_PORT = 3306
DB_DATABASE = 
DB_USERNAME = 
DB_PASSWORD = 
DB_PREFIX = 

REDIS_HOST = 
REDIS_PASSWORD = 
REDIS_PORT = 
REDIS_DB = 

GOOGLE_API_KEY = 

OSS_HOST = 
```

Config.py
```
import os
def import_env():
    if os.path.exists('.env'):
        print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            key, value = var[0].strip(), var[1].strip()
            os.environ[key] = value
```

Text Case
```

import pathlib
import textwrap
import mysql.connector
import sys
import os
import google.generativeai as genai
import time
from config import import_env

from random import randint

import_env()

# Used to securely store your API key
# from google.colab import userdata

from IPython.display import display
from IPython.display import Markdown

import redis

genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

def search_from_google_ai(text):
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content(text)
  print(response.text)
  return response.text

db = mysql.connector.connect(
  host=os.environ.get('DB_HOST'),
  user=os.environ.get('DB_USERNAME'),
  password=os.environ.get('DB_PASSWORD'),
  database=os.environ.get('DB_DATABASE')
)

r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), db=os.environ.get('REDIS_DB'), password=os.environ.get('REDIS_PASSWORD'), decode_responses=True, protocol=3)


# r.connection_pool.disconnect()

cursor = db.cursor()

cursor.execute("SELECT name,isbn FROM fetchobj where repeated > 0 order by update_time desc limit 100")

myresult = cursor.fetchall()

for x in myresult:
  redisCache = r.get(x[1]+"_ai")
  if(r.exists(x[1]+"_ai")==False):
    text = "书名："+ x[0] +"，isbn："+ x[1] +"，请把书名翻译成中文,并帮我找出这本书的作者及作者介绍，Genres,系列书名及系列名对应isbn号，详细内容同时告知这本书主题思想，适合几岁阅读，蓝思指数，妈妈通过阅读知识点更好的帮助孩子阅读，是否有音频链接,请有序输出"
    print(text)
    result = search_from_google_ai(text)
    r.set(x[1]+"_ai", result)
    time.sleep(randint(10,100))

#sys.exit(0)



def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# model = genai.GenerativeModel('gemini-pro')

# models/gemini-pro
# models/gemini-pro-vision
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

# response = model.generate_content("书名：Houghton Mifflin Reading，isbn：9720618089587，请把书名翻译成中文,并帮我找出这本书的作者及作者介绍，Genres,系列书名及系列名对应isbn号，详细内容同时告知这本书主题思想，适合几岁阅读，蓝思指数，妈妈通过阅读知识点更好的帮助孩子阅读，是否有音频链接。")

# print(response.text)

```

Image Case
```
import pathlib
import textwrap
import mysql.connector
import sys
import os
import google.generativeai as genai
import time
from config import import_env

from random import randint

import urllib.request

from PIL import Image

import shutil

import_env()

# Used to securely store your API key
# from google.colab import userdata

from IPython.display import display
from IPython.display import Markdown

import redis

genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

def search_from_google_ai(isbn):
  model = genai.GenerativeModel('gemini-pro-vision')
  
  dst = "covers/"+isbn+".jpg"
  src = os.environ.get('OSS_HOST') + dst
  urllib.request.urlretrieve(src, dst)
  # shutil.copyfile(src, dst)
  img = Image.open(dst)
  response = model.generate_content(img)
  print(response.text)
  return response.text


db = mysql.connector.connect(
  host=os.environ.get('DB_HOST'),
  user=os.environ.get('DB_USERNAME'),
  password=os.environ.get('DB_PASSWORD'),
  database=os.environ.get('DB_DATABASE')
)

r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), db=os.environ.get('REDIS_DB'), password=os.environ.get('REDIS_PASSWORD'), decode_responses=True, protocol=3)

# r.connection_pool.disconnect()

cursor = db.cursor()

cursor.execute("SELECT name,isbn FROM fetchobj where repeated > 0 order by update_time desc limit 1")

myresult = cursor.fetchall()

for x in myresult:
  cache_key = x[1]+"_ai_images"
  redisCache = r.get(cache_key)
  print(cache_key)
  if(r.exists(cache_key)==False):
    isbn = x[1]
    print(isbn)
    result = search_from_google_ai(isbn)
    r.set(cache_key, result)
    time.sleep(randint(10,100))
```