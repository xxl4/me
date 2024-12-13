---
title: How to use docker build a email service
date: 2024-12-06 10:00:00
tags: [docker, email, smtp]
categories: [docker]
description: How to use docker build a email service
lang: en
comments: true
sitemap:
  lastmod: 2024-12-06 10:00:00
  priority: 0.8
  changefreq: weekly
cover: /images/en/2024/12/2024-12-06-How-to-use-docker-build-a-email-service.jpg
---

![How to use docker build a email service](/images/en/2024/12/2024-12-06-How-to-use-docker-build-a-email-service.jpg)

## How to use docker build a email service

### 1. Create a new directory

```bash
mkdir email-service
cd email-service
```

### 2. Create a new file named `Dockerfile`

```bash
touch Dockerfile
```

### 3. Edit the `Dockerfile`

```Dockerfile
FROM alpine:3.14

RUN apk add --no-cache \
    ssmtp

COPY ssmtp.conf /etc/ssmtp/ssmtp.conf

CMD ["ssmtp", "