---
title: How to use robots.txt
date: 2020-06-01 00:00:00
tags: [SEO, robots.txt]
description: How to use robots.txt, a file that tells search engines how to crawl your website.
lang: en
comments: true
sitemap: true
---

# What is robots.txt?

`robots.txt` is a file that tells search engines how to crawl your website. It is a text file that is placed in the root directory of your website. The file is used to tell search engine crawlers which pages or files the crawler can or can't request from your site.

# How to create a robots.txt file

To create a `robots.txt` file, you can use a text editor like Notepad or TextEdit. The file should be named `robots.txt` and placed in the root directory of your website.

Here is an example of a simple `robots.txt` file:

```txt
User-agent: *

Allow: /
Allow: /archives/
Allow: /page/
Allow: /schedule/
Allow: /tags/
Allow: /categories/
Allow: /search/
Allow: /about/
Allow: /links/
Allow: /friends/
Allow: /sitemap.xml
Allow: /sitemap.txt
Allow: /atom.xml
Allow: /feed.xml
Allow: /ads.txt
Allow: /manifest.json

Disallow: /js/
Disallow: /css/
Disallow: /images/

Sitemap: https://www.models.net.cn/sitemap.xml
Sitemap: https://www.models.net.cn/sitemap.txt
```

In the example above, the `User-agent: *` line specifies that the rules apply to all search engine crawlers. The `Allow` lines specify which directories or files the crawler is allowed to access, while the `Disallow` lines specify which directories or files the crawler is not allowed to access. The `Sitemap` lines specify the location of the sitemap file for the website.

# How to test your robots.txt file

To test your `robots.txt` file, you can use the robots.txt Tester tool in Google Search Console. This tool allows you to test how Google's web crawler will interpret your `robots.txt` file.

To use the tool, follow these steps:

1. Go to Google Search Console and sign in.
2. Click on the property for which you want to test the `robots.txt` file.
3. Click on the "URL Inspection" tool in the left-hand menu.
4. Enter the URL of the `robots.txt` file in the search bar and click "Enter".
5. Click on the "Test robots.txt" button to see how Google's web crawler will interpret your `robots.txt` file.

# robots.txt best practices

Here are some best practices for using `robots.txt`:

1. Make sure your `robots.txt` file is located in the root directory of your website.
2. Use the `User-agent: *` line to apply rules to all search engine crawlers.
3. Use the `Allow` and `Disallow` lines to specify which directories or files the crawler can or can't access.
4. Use the `Sitemap` line to specify the location of the sitemap file for the website.
5. Test your `robots.txt` file using the robots.txt Tester tool in Google Search Console.

By following these best practices, you can ensure that search engine crawlers are able to crawl your website effectively and efficiently.

# References

- [Google Search Console](https://search.google.com/search-console)
- [Google Search Console Help: Test robots.txt](https://support.google.com/webmasters/answer/6062596)
- [Google Search Console Help: robots.txt Tester](https://support.google.com/webmasters/answer/6062598)
- [Google Search Console Help: robots.txt specifications](https://developers.google.com/search/reference/robots_txt)
- [Google Search Console Help: Create a robots.txt file](https://support.google.com/webmasters/answer/6062608)
- [Google Search Console Help: robots.txt best practices](https://support.google.com/webmasters/answer/6062609)
- [Google Search Console Help: robots.txt FAQ](https://support.google.com/webmasters/answer/6062601)
- [Google Search Console Help: robots.txt examples](https://support.google.com/webmasters/answer/6062596)
- [Google Search Console Help: robots.txt syntax](https://support.google.com/webmasters/answer/6062598)
- [Google Search Console Help: robots.txt format](https://support.google.com/webmasters/answer/6062599)
- [Google Search Console Help: robots.txt file](https://support.google.com/webmasters/answer/6062600)
- [Google Search Console Help: robots.txt rules](https://support.google.com/webmasters/answer/6062602)
- [Google Search Console Help: robots.txt directives](https://support.google.com/webmasters/answer/6062603)
- [Google Search Console Help: robots.txt disallow](https://support.google.com/webmasters/answer/6062604)
- [Google Search Console Help: robots.txt allow](https://support.google.com/webmasters/answer/6062605)
- [Google Search Console Help: robots.txt sitemap](https://support.google.com/webmasters/answer/6062606)
- [Google Search Console Help: robots.txt crawl-delay](https://support.google.com/webmasters/answer/6062607)
- [Google Search Console Help: robots.txt noindex](https://support.google.com/webmasters/answer/6062608)
- [Google Search Console Help: robots.txt nofollow](https://support.google.com/webmasters/answer/6062609)
- [Google Search Console Help: robots.txt noarchive](https://support.google.com/webmasters/answer/6062610)
- [Google Search Console Help: robots.txt nosnippet](https://support.google.com/webmasters/answer/6062611)
- [Google Search Console Help: robots.txt notranslate](https://support.google.com/webmasters/answer/6062612)
- [Google Search Console Help: robots.txt noimageindex](https://support.google.com/webmasters/answer/6062613)
- [Google Search Console Help: robots.txt nofollow](https://support.google.com/webmasters/answer/6062614)
- [Google Search Console Help: robots.txt noindex](https://support.google.com/webmasters/answer/6062615)


