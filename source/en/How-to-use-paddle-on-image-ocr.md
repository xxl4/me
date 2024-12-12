---
title: How to use paddle python on image OCR
tags:
  - Python
  - NLP
  - OCR
  - PaddleOCR
  - Baidu
  - Google
categories:
  - Technology
  - Python
date: 2024-02-06 16:23:12
description: How to use paddle python on image OCR
lang: en
comments: true
---
Today, we have so many image need to OCR, So i will try use [PaddleOCR](https://github.com/xxl4/PaddleOCR) for it.

# .env file

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

# config.py file

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

# ocr.py file

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

# requirements.txt

```
APScheduler==3.10.4
asttokens==2.4.1
async-timeout==4.0.3
cachetools==5.3.2
certifi==2023.11.17
charset-normalizer==3.3.2
click==8.1.7
decorator==5.1.1
easyocr==1.7.1
exceptiongroup==1.2.0
executing==2.0.1
filelock==3.13.1
fsspec==2023.12.2
google-ai-generativelanguage==0.4.0
google-api-core==2.15.0
google-auth==2.25.2
google-generativeai==0.3.2
googleapis-common-protos==1.62.0
grpcio==1.60.0
grpcio-status==1.60.0
idna==3.6
imageio==2.33.1
ipython==8.18.1
jedi==0.19.1
Jinja2==3.1.3
lazy_loader==0.3
MarkupSafe==2.1.4
matplotlib-inline==0.1.6
mpmath==1.3.0
mysql==0.0.3
mysql-connector==2.2.9
mysqlclient==2.2.3
networkx==3.2.1
ninja==1.11.1.1
numpy==1.26.3
nvidia-cublas-cu12==12.1.3.1
nvidia-cuda-cupti-cu12==12.1.105
nvidia-cuda-nvrtc-cu12==12.1.105
nvidia-cuda-runtime-cu12==12.1.105
nvidia-cudnn-cu12==8.9.2.26
nvidia-cufft-cu12==11.0.2.54
nvidia-curand-cu12==10.3.2.106
nvidia-cusolver-cu12==11.4.5.107
nvidia-cusparse-cu12==12.1.0.106
nvidia-nccl-cu12==2.18.1
nvidia-nvjitlink-cu12==12.3.101
nvidia-nvtx-cu12==12.1.105
opencv-python-headless==4.9.0.80
packaging==23.2
parso==0.8.3
pexpect==4.9.0
Pillow==10.1.0
prompt-toolkit==3.0.43
proto-plus==1.23.0
protobuf==4.25.1
ptyprocess==0.7.0
pure-eval==0.2.2
pyasn1==0.5.1
pyasn1-modules==0.3.0
pyclipper==1.3.0.post5
Pygments==2.17.2
python-bidi==0.4.2
pytz==2023.3.post1
PyYAML==6.0.1
redis==5.0.1
requests==2.31.0
rq==1.15.1
rsa==4.9
scikit-image==0.22.0
scipy==1.12.0
shapely==2.0.2
six==1.16.0
stack-data==0.6.3
sympy==1.12
tifffile==2023.12.9
torch==2.1.2
torchvision==0.16.2
tqdm==4.66.1
traitlets==5.14.1
triton==2.1.0
typing_extensions==4.9.0
tzlocal==5.2
urllib3==2.1.0
wcwidth==0.2.13
```

# Referce
[PaddleOCR](https://github.com/xxl4/PaddleOCR) 