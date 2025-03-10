---
title: How to use Google Public DNS to check domain status
date: 2025-03-10
tags: [DNS, Google, Domain]
description: How to use Google Public DNS to check domain status and troubleshoot DNS issues.
comment: true
sitemap: true
Author: Steve Liu
---

Google Public DNS is a free Domain Name System (DNS) service offered to Internet users worldwide by Google. It functions as a recursive name server providing domain name resolution for any host on the Internet. Google Public DNS was announced on 3 December 2009, in an effort described as "making the web faster and more secure". As of 2014, it is the largest public DNS service in the world, handling over 400 billion requests per day.

# Table of Contents

1. [About Dns](#about-dns)
2. [About Google Public DNS](#about-google-public-dns)
3. [How to use Google Public DNS to check domain status](#how-to-use-google-public-dns-to-check-domain-status)
4. [How to use Google Public DNS API to check domain status](#how-to-use-google-public-dns-api-to-check-domain-status)
5. [Conclusion](#conclusion)

# About Dns
DNS (Domain Name System) is a system that translates domain names into IP addresses. This allows you to access websites using domain names instead of IP addresses. For example, when you type www.google.com into your web browser, your computer uses DNS to translate the domain name into an IP address that it can use to connect to Google's servers.

Dns is the backbone of the internet, and without it, you wouldn't be able to access any websites. When you type a domain name into your web browser, your computer sends a request to a DNS server to translate the domain name into an IP address. The DNS server then sends the IP address back to your computer, allowing it to connect to the website you want to visit.

# About Google Public DNS

Google Public DNS is a free DNS service that anyone can use to translate domain names into IP addresses. It is fast, reliable, and secure, making it a popular choice for many internet users. Google Public DNS is easy to set up and can help you troubleshoot DNS issues on your network.

# How to use Google Public DNS to check domain status

To use Google Public DNS to check the status of a domain, you can use the `nslookup` command in the command prompt. Here's how you can do it:

1. Open the command prompt on your computer.
2. Type `nslookup` followed by the domain name you want to check. For example, to check the status of www.google.com, you would type `nslookup www.google.com`.
3. Press Enter to run the command.

The `nslookup` command will return the IP address of the domain you entered, as well as other information about the domain. If the domain is working correctly, you should see the IP address of the domain in the output. If the domain is not working correctly, you may see an error message or no output at all.

# How to use Google Public DNS API to check domain status

Google Public DNS also provides an API that you can use to check the status of a domain programmatically. You can use the API to query the status of a domain and get information about the domain's DNS records.

To use the Google Public DNS API, you will need to sign up for a Google Cloud Platform account and create a project. Once you have created a project, you can enable the Google Public DNS API and generate an API key that you can use to access the API.

Here's an example of how you can use the Google Public DNS API to check the status of a domain using Python:

```python
import requests

domain = 'www.google.com'

url = f'https://dns.google/resolve?name={domain}'
response = requests.get(url)
data = response.json()

print(data)
```

This code snippet sends a request to the Google Public DNS API to resolve the domain name `www.google.com`. The API will return information about the domain, including its IP address and DNS records.

# Conclusion
[Google Public DNS Docs](https://developers.google.com/speed/public-dns/docs/doh/json)

Google Public DNS is a powerful tool that can help you check the status of a domain and troubleshoot DNS issues. By using Google Public DNS, you can quickly determine if a domain is working correctly and get information about its DNS records. If you are experiencing DNS issues on your network, Google Public DNS can help you identify and resolve them quickly.
