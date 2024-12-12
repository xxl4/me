---
title: How to use curl command for api testing and debug
tags:
  - Api
  - Json
  - Curl
categories:
  - Technology
  - Curl
date: 2023-12-27 09:23:12
description: How to use curl command for api testing and debug
lang: en
comments: true
---
When you are write some api interface, maybe you should use postman tool do it better, but now, my computer is so low, 
I need use Vs for anything project do it, so i need use curl for my api interface manual do it.

```
curl -X POST https://127.0.0.1/api/airwallex/webhook -H "Content-Type: application/json" -d @payment_intent.successed.json
```

payment_intent.successed.json

```
{"id":"evt_hkdmkwnjkgrw2fs4str_evqoqo","name":"payment_intent.succeeded","account_id":"acct_2DRXqPIFPd2G-O1KDJ_7gA","accountId":"acct_2DRXqPIFPd2G-O1KDJ_7gA","data":{"object":{"amount":14.99,"base_amount":14.99,"base_currency":"USD","captured_amount":14.99,"created_at":"2023-12-27T01:56:20+0000","currency":"USD","customer":{"address":{"city":"\u5927\u6f6d","country_code":"HK","postcode":"200000","state":"\u5927\u6f6d","street":"HuaShang Road,000000"},"email":"aaa@aaa.com","first_name":"Kevin","last_name":"OneBuy","phone_number":"135 2408 4051"},"descriptor":"Pa Test","id":"int_hkdm6z95kgrw2evqoqo","latest_payment_attempt":{"amount":14.99,"authentication_data":{"avs_result":"U","cvc_code":"M","cvc_result":"Y","ds_data":{"retry_count_for_auth_decline":0},"fraud_data":{"action":"ACCEPT","score":"0"}},"authorization_code":"689538","captured_amount":0,"created_at":"2023-12-27T01:57:13+0000","currency":"USD","id":"att_hkdmkwnjkgrw2fr6rii_evqoqo","merchant_order_id":"orderid_105","payment_intent_id":"int_hkdm6z95kgrw2evqoqo","payment_method":{"card":{"billing":{"address":{"city":"\u5927\u6f6d","country_code":"HK","postcode":"","state":"Kowloon","street":"HuaShang Road,000000"},"email":"aaa@aaa.com","first_name":"Kevin","last_name":"OneBuy","phone_number":"1-3650447"},"bin":"40355010","brand":"visa","card_type":"DEBIT","cvc_check":"pass","expiry_month":"12","expiry_year":"2023","fingerprint":"KxdcR5awfqROiLGflcSIjnB1vUM=","is_commercial":false,"issuer_country_code":"US","issuer_name":"SOCIETE GENERALE","last4":"0008","name":"Kevin OneBuy","number_type":"PAN"},"type":"card"},"payment_method_options":{"card":[]},"provider_original_response_code":"00","provider_transaction_id":"124132981408_618455789993947","refunded_amount":0,"settle_via":"airwallex","status":"AUTHORIZED","updated_at":"2023-12-27T01:57:15+0000"},"merchant_order_id":"orderid_105","metadata":{"my_test_metadata_id":"my_test_metadata_id_105"},"order":{"products":[{"code":"11111","desc":"11111","name":"11111","quantity":1,"sku":"11111","type":"11111","unit_price":14.99,"url":"https:\/\/www.baidu.com\/"}],"shipping":{"address":{"city":"\u5927\u6f6d","country_code":"HK","postcode":"200000","state":"\u5927\u6f6d","street":"HuaShang Road,000000"},"first_name":"Kevin","last_name":"OneBuy","phone_number":"135 2408 4051"},"type":"Online Mobile Phone Purchases"},"request_id":"105_1703642180","status":"SUCCEEDED","updated_at":"2023-12-27T01:57:15+0000"}},"created_at":"2023-12-27T01:57:15+0000","createdAt":"2023-12-27T01:57:15+0000","version":"2023-10-01","sourceId":"int_hkdm6z95kgrw2evqoqo"}
```

Curl have many function for http and other protectl, you can use  curl --help to view

```
curl --help

Usage: curl [options...] <url>
 -d, --data <data>          HTTP POST data
 -f, --fail                 Fail fast with no output on HTTP errors
 -h, --help <category>      Get help for commands
 -i, --include              Include protocol response headers in the output
 -o, --output <file>        Write to file instead of stdout
 -O, --remote-name          Write output to a file named as the remote file
 -s, --silent               Silent mode
 -T, --upload-file <file>   Transfer local FILE to destination
 -u, --user <user:password> Server user and password
 -A, --user-agent <name>    Send User-Agent <name> to server
 -v, --verbose              Make the operation more talkative
 -V, --version              Show version number and quit

This is not the full help, this menu is stripped into categories.
Use "--help category" to get an overview of all categories.
For all options use the manual or "--help all".

```