---
title: Odoo Payment Airwallex Modules
date: 2024-12-18 16:00:00
categories: [odoo]
tags: [odoo, payment, airwallex, modules, payment gateway]
lang: en
comments: true
description: Odoo 18.0 Payment Airwallex Modules
sitemap: 
    lastmod: 2024-12-18 16:00:00
    priority: 0.5
    changefreq: monthly
---

# Odoo Payment Airwallex Modules

Airwallex is a global payment gateway that allows you to accept payments in multiple currencies. This module integrates Airwallex with Odoo to provide a seamless payment experience for your customers.

## Features

- Accept payments in multiple currencies
- Process payments securely using Airwallex
- Automatically update payment status in Odoo
- Generate invoices and receipts for successful payments

## Installation

To install the Odoo Payment Airwallex Modules, follow these steps:

1. Download the module from the Odoo Apps Store
2. Upload the module to your Odoo instance
3. Activate the module in the Odoo Apps menu
4. Configure your Airwallex account settings in Odoo
5. Start accepting payments with Airwallex

## Configuration

To configure the Odoo Payment Airwallex Modules, follow these steps:

1. Go to the Payments menu in Odoo
2. Click on the Configuration tab
3. Select Airwallex as the payment provider
4. Enter your Airwallex API key and other settings
5. Save your changes and start accepting payments

## Usage

To use the Odoo Payment Airwallex Modules, follow these steps:

1. Go to the Sales menu in Odoo
2. Create a new order or select an existing order
3. Choose Airwallex as the payment method
4. Enter the customer's payment details
5. Click on the Pay Now button to process the payment
6. Once the payment is successful, an invoice will be generated automatically

## Conclusion

The Odoo Payment Airwallex Modules provide a convenient way to accept payments in multiple currencies using Airwallex. With this integration, you can offer a seamless payment experience for your customers and streamline your payment processing workflow. Try out the Odoo Payment Airwallex Modules today and start accepting payments with ease.

For more information about the Odoo Payment Airwallex Modules, visit the [Github Airwllex Odoo](https://github.com/xxl4/payment_airwallex).

```
{
    'name': 'Payment Provider: Airwallex',
    'version': '1.0',
    'category': 'Accounting/Payment Providers',
    'summary': "An Airwallex payment provider for online payments all over the world.",
    'author': "Steve Liu",
    'sequence': 5000,
    'description': " ",  # Non-empty string to avoid loading the README file.
    'depends': ['payment'],
    'data': [
        'views/payment_form_templates.xml',
        'views/payment_provider_views.xml',
        'views/payment_transaction_views.xml',
        'data/payment_provider_data.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'assets': {
        'web.assets_frontend': [
            'payment_airwallex/static/src/**/*',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
}
```
