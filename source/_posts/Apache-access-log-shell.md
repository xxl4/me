---
title: Apache Access Log Analyzer use Shell
tags:
  - Apache
  - shell
  - awk
categories:
  - Technology
  - DevOps
date: 2024-01-07 12:23:12
description: Apache Access Log Analyzer use Shell
lang: en
comments: true
---


View Server connection ip for max
```
netstat -ntu |awk '{print $5}' |sort | uniq -c| sort -nr
```
 

view access log file top 10 ip
```
cat access_log  |cut -d ' ' -f 1 |sort |uniq -c | sort -nr | awk '{print $0 }' | head -n 10 |less
```
 

View access log file more than 100 times ip
```
cat access_log  |cut -d ' ' -f 1 |sort |uniq -c | awk '{if ($1 > 100) print $0}'｜sort -nr |less
```

View access log file top visits file
```
cat access_log |tail -10000|awk '{print $7}'|sort|uniq -c|sort -nr|less
```
 
view access log file for more than 100 times page
```
cat access_log | cut -d ' ' -f 7 | sort |uniq -c |  awk '{if ($1 > 100) print $0}' | less
```

View access log for a url visits  count
#cat access_log|grep '12/Aug/2009'|grep '/images/index/e1.gif'|wc|awk '{print $1}'

 
View access log for top visits 
```
cat access_log|awk '{print $7}'|uniq -c |sort -n -r|head -20
```
 
View access log for a ip history
```
cat access_log | grep 218.66.36.119| awk '{print $1"\t"$7}' | sort | uniq -c | sort -nr | less
```
 
View more thant 30s page on access file
```
cat access_log|awk '($NF > 30){print $7}' |sort -n|uniq -c|sort -nr|head -20
```
 

View more thant 60s page on access file
```
cat access_log |awk  '($NF > 60 && $7~/\.php/){print $7}' |sort -n|uniq -c|sort -nr|head -100
```

