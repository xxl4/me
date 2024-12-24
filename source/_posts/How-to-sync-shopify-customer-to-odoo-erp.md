---
title: How to sync shopify customer to odoo erp
date: 2024-12-24 13:00:00
tags: [shopify, odoo, customer, erp, connector]
lang: en
description: How to sync shopify customer to odoo erp? This article will guide you on how to sync shopify customer to odoo erp.
sitemap:
  lastmod: 2024-12-24 13:00:00
  priority: 0.5
  changefreq: monthly
comments: true
cover: /images/en/2024/12/How-to-sync-shopify-customer-to-odoo-erp.jpg
---

![How to sync shopify customer to odoo erp](/images/en/2024/12/How-to-sync-shopify-customer-to-odoo-erp.jpg)

## About Shopify

Shopify is a popular e-commerce platform that allows you to create an online store and sell products online. It provides a wide range of features and tools to help you manage your store, including inventory management, order processing, and customer management.

## About Odoo ERP

Odoo is an open-source ERP software that provides a wide range of business applications, including CRM, e-commerce, accounting, and project management. It is a powerful and flexible platform that can help you streamline your business processes and improve efficiency.

## How to sync shopify customer to odoo erp

To sync shopify customer to odoo erp, you can use a connector that integrates the two platforms and allows you to transfer customer data between them. There are several connectors available that can help you sync shopify customer to odoo erp, such as the Odoo Shopify Connector.

The Odoo Shopify Connector is a powerful tool that allows you to sync customer data between shopify and odoo erp. It provides a wide range of features and tools to help you manage your customer data, including customer synchronization, order synchronization, and product synchronization.

To sync shopify customer to odoo erp using the Odoo Shopify Connector, follow these steps:

1. Install the Odoo Shopify Connector on your odoo erp instance.

2. Configure the connector to connect to your shopify store.

3. Set up the customer synchronization settings to sync customer data between shopify and odoo erp.

4. Run the synchronization process to transfer customer data between the two platforms.

By following these steps, you can easily sync shopify customer to odoo erp and streamline your business processes.

In conclusion, syncing shopify customer to odoo erp is a simple process that can help you improve efficiency and streamline your business processes. By using a connector like the Odoo Shopify Connector, you can easily transfer customer data between the two platforms and manage your customer data more effectively. 

To sync shopify customer to odoo erp, you can use shopify api and use odoo api to create customer in odoo erp. You can also use a connector like the Odoo Shopify Connector to automate the process and make it more efficient.

```python
# sync customer to odoo
import os
from dotenv import load_dotenv
import requests
import json
import xmlrpc.client
import time
from math import ceil
import redis
import shopify
from api_store import get_token
from odoo_api import OdooApi
from RedisEnums import RedisEnums
from time import sleep

# Load environment variables from .env file
load_dotenv()

def get_customers(limit=50, odoo=None, website_id=None):
    customers = []
    page_info = None

    while True:
        params = {'limit': limit}
        if page_info:
            params['page_info'] = page_info

        response = shopify.Customer.find(**params)
        customers.extend(response)

        for customer in response:
            customer_dict = customer.to_dict()
            if customer_dict['email'] == None:
                continue

            print(f"Checking customer: {customer_dict}")

            customer_id = r.get(customer_dict['email'])
            if customer_id:
                continue

            # check if the customer address is empty
            if customer_dict['addresses'].__len__() == 0:
                continue
            
            # check if the customer exists in odoo
            odoo_customer = odoo.get_customer_by_email(customer_dict['email'])
            if not odoo_customer:
                # create the customer
                print(f"Creating customer: {customer_dict}")
                customer_id = odoo.create_customer(customer_dict, website_id)
                r.set(customer_dict['email'], customer_id)
                sleep(1)




        if not response:
            break

        if response.next_page_url is None:
            break;

        page_info = response.next_page_url.split('page_info=')[1]

    return customers

if __name__ == "__main__":
    
    shop_url = os.getenv('USA_SHOPIFY_HOST')
    api_version = os.getenv('USA_SHOPIFY_API_VERSION')
    private_app_password = os.getenv('USA_SHOPIFY_ACCESS_TOKEN')
    session = shopify.Session(shop_url, api_version, private_app_password)
    shopify.ShopifyResource.activate_session(session)

    website_id = os.getenv('WEBSITE_ID')

    odoo = OdooApi(os.getenv('URL'), os.getenv('DB'), os.getenv('USERNAME'), os.getenv('API_KEY'))

    redis_host = os.getenv('REDIS_HOST')
    redis_port = os.getenv('REDIS_PORT')
    redis_db = os.getenv('REDIS_DB')
    redis_password = os.getenv('REDIS_PASSWORD')

    # create a connection to the redis server
    r = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)

    # get the last time the customer was synced
    customers = get_customers(limit=50, odoo=odoo, website_id=website_id)
    for customer in customers:
        customer_dict = customer.to_dict()
        print(customer_dict)
        exit()

```


I hope this article has helped you understand how to sync shopify customer to odoo erp. If you have any questions or comments, please feel free to leave them below.

## References

- [Shopify](https://www.shopify.com/)
- [Odoo ERP](https://www.odoo.com/)
- [Odoo Shopify Connector](https://github.com/NexaMerchant/OdooClient)
```
