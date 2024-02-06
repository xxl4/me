---
title: How to use paddle python on image OCR
tags:
  - Python
  - NLP
  - Paddle
  - OCR
categories:
  - Technology
  - Python
date: 2024-02-06 16:23:12
description: How to use paddle python on image OCR
lang: en
comments: true
---
Today, we have so many image need to OCR, So i will try use paddle for it.

config.py file

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

ocr.py file

```
import easyocr

import pathlib
import textwrap
import mysql.connector
from paddleocr import PaddleOCR, draw_ocr
import sys
import os
import google.generativeai as genai
import time
from config import import_env

from random import randint

import urllib.request

from PIL import Image

import shutil

import json

import_env()

from IPython.display import display
from IPython.display import Markdown

import redis

import os.path

# reader = easyocr.Reader(['en'], gpu=False)

ocr = PaddleOCR(use_angle_cls=True, lang="en", use_gpu=False )

genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))


def paddle_nlp_image(path):
  dst = path
  if os.path.exists(dst)==False:
    src = os.environ.get('OSS_HOST') + dst
    print("image src " + src)
    try:
       urllib.request.urlretrieve(src, dst)
    except:
       return False
  print("processing the images " + dst)
  result = ocr.ocr(dst, cls=True)
  lists = []
  for idx in range(len(result)):
    res = result[idx]
    try:
      for line in res:
          # print(line)
          print(line[1][0])
          lists.append(line[1][0])
    except:
       print("Error")
       return []
  return lists

def nlp_image(path):
  dst = path
  if os.path.exists(dst)==False:
    src = os.environ.get('OSS_HOST') + dst
    print("image src " + src)
    try:
      urllib.request.urlretrieve(src, dst)
    except ValueError:
       return False
  # shutil.copyfile(src, dst)
  result = reader.readtext(path, detail = 0)
  print(result)
  return result

def search_from_google_ai(path):
  model = genai.GenerativeModel('gemini-pro-vision')
  dst = path
  if os.path.exists(dst)==False:
    src = os.environ.get('OSS_HOST') + dst
    print("image src " + src)
    try:
      urllib.request.urlretrieve(src, dst)
    except:
       return False
  # shutil.copyfile(src, dst)
  img = Image.open(dst)
  try:
    response = model.generate_content(img)
    print(response.text)
    return response.text
  except ValueError:
     #print(response.text)
     # print(response.parts)
     return False
  print(response)
  print(response.text)
  print(response.parts)
  return response.text


db = mysql.connector.connect(
  host=os.environ.get('DB_HOST'),
  user=os.environ.get('DB_USERNAME'),
  password=os.environ.get('DB_PASSWORD'),
  database=os.environ.get('DB_DATABASE')
)

r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), db=os.environ.get('REDIS_DB'), password=os.environ.get('REDIS_PASSWORD'), decode_responses=True, protocol=3)
cursor = db.cursor()

cursor.execute("SELECT * from sd_goods_gallery where img_desc is null order by img_id desc limit 10000")

items = cursor.fetchall()

for item in items:
    print("start " + str(item[0]))
    # result = nlp_image(item[5])
    print("images " + item[5])
    result = paddle_nlp_image(item[5])
    cache_key = str(item[0])+"_gallery_ai_images"
    ai_result = r.get(cache_key)
    print(ai_result)
    if(r.exists(cache_key)==False):
        ai_result = search_from_google_ai(item[5])
        if(ai_result!=False):
          r.set(cache_key, ai_result)
    y = json.dumps(result)
    print(y)
    print(ai_result)
    if (y=='[]'):
       y = []
       y.append(ai_result)
       y = json.dumps(y)
    if(y!='[]'):
        cursor.execute(u'''Update sd_goods_gallery set img_desc=%s where img_id=%s;''', (y, item[0]))
        db.commit()

 # this needs to run only once to load the model into memory
# nlp_image()
```