---
title: How to Use Google GTM For Facebook Pixel
date: 2024-11-18 10:49:00
categories: [Google Tag Manager, Facebook Pixel, Analytics, Marketing, Tracking, GTM]
tags: [Google Tag Manager, Facebook Pixel, Analytics, Marketing, Tracking, GTM]
lang: en
comments: true
sitemap: true
description: How to use Google Tag Manager to install Facebook Pixel on your website.
cover: /images/en/2024/11/How-to-use-GTM-For-Facebook-pixel-cover.jpg
---

![How to Use Google GTM For Facebook Pixel](/images/en/2024/11/How-to-use-GTM-For-Facebook-pixel-cover.jpg)

# How to Use Google GTM For Facebook Pixel

In this article, I will show you how to use Google Tag Manager to install Facebook Pixel on your website.

## Step 1: Create a Facebook Pixel

First, you need to create a Facebook Pixel. Go to your Facebook Ads Manager and click on the hamburger menu in the top left corner. Then click on "Pixels" under the "Assets" section.


## Step 2: Copy the Pixel ID

Once you have created a Facebook Pixel, you will see a Pixel ID. Copy this ID as you will need it later.

## Step 3: Create a New Tag in Google Tag Manager

Go to your Google Tag Manager account and create a new tag. Choose "Custom HTML" as the tag type and paste the following code into the HTML field:

```html
<!-- Facebook Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'YOUR_PIXEL_ID');
fbq('track', 'PageView');
</script>
<noscript>
<img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=YOUR_PIXEL_ID&ev=PageView&noscript=1"/>
</noscript>
<!-- End Facebook Pixel Code -->
```

Replace `YOUR_PIXEL_ID` with the Pixel ID you copied in Step 2.

## Step 4: Trigger the Tag

Next, you need to create a trigger for the tag. You can trigger the tag on all pages by selecting the "All Pages" trigger.

## Step 5: Save and Publish

Save the tag and publish the changes in Google Tag Manager.

That's it! You have successfully installed Facebook Pixel on your website using Google Tag Manager. You can now track conversions, optimize ads, and create custom audiences based on the data collected by the Pixel.

I hope you found this article helpful. If you have any questions or comments, please leave them below.

