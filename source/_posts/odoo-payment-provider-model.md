---
title: Odoo Payment Provider Model
date: 2024-12-01 00:00:00
tags: [Odoo, Payment, Provider, Model]
lang: en
comments: true
category: 
    - ERP
    - Odoo
description: Odoo Payment Provider Model
---

# Odoo Payment Provider Model

## Introduction

In this article, we will discuss the Odoo Payment Provider Model.

## Odoo Payment Provider Model

Odoo Payment Provider Model is a model that allows you to manage payment providers in Odoo. Payment providers are used to process payments in Odoo. You can configure payment providers in Odoo to accept payments from customers using different payment methods such as credit cards, PayPal, bank transfers, etc.

The Payment Provider Model in Odoo allows you to create, edit, and delete payment providers. You can also configure payment methods for each payment provider. Payment methods define the payment options available to customers when making a payment.

## Creating a Payment Provider

To create a payment provider in Odoo, follow these steps:

1. Go to the Invoicing app.

2. Click on the Configuration menu.

3. Select Payment Acquirers.

4. Click on the Create button to create a new payment provider.

5. Enter the required information for the payment provider, such as the name, provider type, and provider account.

6. Configure the payment methods for the payment provider.

7. Save the changes.

## Conclusion

In this article, we discussed the Odoo Payment Provider Model. We learned how to create a payment provider in Odoo and configure payment methods for the provider. Payment providers are essential for processing payments in Odoo, and you can use them to accept payments from customers using different payment methods.

```
Field: name
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  manual: False
  name: name
  readonly: False
  required: True
  searchable: True
  sortable: True
  store: True
  string: Name
  translate: True
  trim: True
  type: char
Field: sequence
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: Define the display order
  manual: False
  name: sequence
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: Sequence
  type: integer
Field: code
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: The technical code of this payment provider.
  manual: False
  name: code
  readonly: False
  required: True
  searchable: True
  selection: [['none', 'No Provider Set'], ['authorize', 'Authorize.Net'], ['paypal', 'PayPal'], ['aps', 'Amazon Payment Services']]
  sortable: True
  store: True
  string: Code
  type: selection
Field: state
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: In test mode, a fake payment is processed through a test payment interface.
This mode is advised when setting up the provider.
  manual: False
  name: state
  readonly: False
  required: True
  searchable: True
  selection: [['disabled', 'Disabled'], ['enabled', 'Enabled'], ['test', 'Test Mode']]
  sortable: True
  store: True
  string: State
  type: selection
Field: is_published
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: Whether the provider is visible on the website or not. Tokens remain functional but are only visible on manage forms.
  manual: False
  name: is_published
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: Published
  type: boolean
Field: company_id
  change_default: False
  company_dependent: False
  context: {}
  default_export_compatible: False
  depends: []
  domain: []
  exportable: True
  groupable: True
  manual: False
  name: company_id
  readonly: False
  relation: res.company
  required: True
  searchable: True
  sortable: True
  store: True
  string: Company
  type: many2one
Field: main_currency_id
  change_default: False
  company_dependent: False
  context: {}
  default_export_compatible: False
  depends: ['company_id.currency_id']
  domain: []
  exportable: True
  groupable: True
  help: The main currency of the company, used to display monetary fields.
  manual: False
  name: main_currency_id
  readonly: True
  related: company_id.currency_id
  relation: res.currency
  required: False
  searchable: True
  sortable: True
  store: False
  string: Currency
  type: many2one
Field: payment_method_ids
  change_default: False
  company_dependent: False
  context: {}
  default_export_compatible: False
  depends: []
  domain: []
  exportable: True
  groupable: True
  manual: False
  name: payment_method_ids
  readonly: False
  relation: payment.method
  required: False
  searchable: True
  sortable: False
  store: True
  string: Supported Payment Methods
  type: many2many
Field: allow_tokenization
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: This controls whether customers can save their payment methods as payment tokens.
A payment token is an anonymous link to the payment method details saved in the
provider's database, allowing the customer to reuse it for a next purchase.
  manual: False
  name: allow_tokenization
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: Allow Saving Payment Methods
  type: boolean
Field: capture_manually
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: Capture the amount from Odoo, when the delivery is completed.
Use this if you want to charge your customers cards only when
you are sure you can ship the goods to them.
  manual: False
  name: capture_manually
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: Capture Amount Manually
  type: boolean
Field: allow_express_checkout
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: This controls whether customers can use express payment methods. Express checkout enables customers to pay with Google Pay and Apple Pay from which address information is collected at payment.
  manual: False
  name: allow_express_checkout
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: Allow Express Checkout
  type: boolean
Field: redirect_form_view_id
  change_default: False
  company_dependent: False
  context: {}
  default_export_compatible: False
  depends: []
  domain: [['type', '=', 'qweb']]
  exportable: True
  groupable: True
  help: The template rendering a form submitted to redirect the user when making a payment
  manual: False
  name: redirect_form_view_id
  readonly: False
  relation: ir.ui.view
  required: False
  searchable: True
  sortable: True
  store: True
  string: Redirect Form Template
  type: many2one
Field: inline_form_view_id
  change_default: False
  company_dependent: False
  context: {}
  default_export_compatible: False
  depends: []
  domain: [['type', '=', 'qweb']]
  exportable: True
  groupable: True
  help: The template rendering the inline payment form when making a direct payment
  manual: False
  name: inline_form_view_id
  readonly: False
  relation: ir.ui.view
  required: False
  searchable: True
  sortable: True
  store: True
  string: Inline Form Template
  type: many2one
Field: token_inline_form_view_id
  change_default: False
  company_dependent: False
  context: {}
  default_export_compatible: False
  depends: []
  domain: [['type', '=', 'qweb']]
  exportable: True
  groupable: True
  help: The template rendering the inline payment form when making a payment by token.
  manual: False
  name: token_inline_form_view_id
  readonly: False
  relation: ir.ui.view
  required: False
  searchable: True
  sortable: True
  store: True
  string: Token Inline Form Template
  type: many2one
Field: express_checkout_form_view_id
  change_default: False
  company_dependent: False
  context: {}
  default_export_compatible: False
  depends: []
  domain: [['type', '=', 'qweb']]
  exportable: True
  groupable: True
  help: The template rendering the express payment methods' form.
  manual: False
  name: express_checkout_form_view_id
  readonly: False
  relation: ir.ui.view
  required: False
  searchable: True
  sortable: True
  store: True
  string: Express Checkout Form Template
  type: many2one
Field: available_country_ids
  change_default: False
  company_dependent: False
  context: {}
  default_export_compatible: False
  depends: []
  domain: []
  exportable: True
  groupable: True
  help: The countries in which this payment provider is available. Leave blank to make it available in all countries.
  manual: False
  name: available_country_ids
  readonly: False
  relation: res.country
  required: False
  searchable: True
  sortable: False
  store: True
  string: Countries
  type: many2many
Field: available_currency_ids
  change_default: False
  company_dependent: False
  context: {'active_test': False}
  default_export_compatible: False
  depends: ['code']
  domain: []
  exportable: True
  groupable: True
  help: The currencies available with this payment provider. Leave empty not to restrict any.
  manual: False
  name: available_currency_ids
  readonly: False
  relation: res.currency
  required: False
  searchable: True
  sortable: False
  store: True
  string: Currencies
  type: many2many
Field: maximum_amount
  aggregator: sum
  change_default: False
  company_dependent: False
  currency_field: main_currency_id
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: The maximum payment amount that this payment provider is available for. Leave blank to make it available for any payment amount.
  manual: False
  name: maximum_amount
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: Maximum Amount
  type: monetary
Field: pre_msg
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: The message displayed to explain and help the payment process
  manual: False
  name: pre_msg
  readonly: False
  required: False
  sanitize: True
  sanitize_attributes: True
  sanitize_style: False
  sanitize_tags: True
  searchable: True
  sortable: True
  store: True
  string: Help Message
  strip_classes: False
  strip_style: False
  translate: True
  type: html
Field: pending_msg
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: The message displayed if the order pending after the payment process
  manual: False
  name: pending_msg
  readonly: False
  required: False
  sanitize: True
  sanitize_attributes: True
  sanitize_style: False
  sanitize_tags: True
  searchable: True
  sortable: True
  store: True
  string: Pending Message
  strip_classes: False
  strip_style: False
  translate: True
  type: html
Field: auth_msg
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: The message displayed if payment is authorized
  manual: False
  name: auth_msg
  readonly: False
  required: False
  sanitize: True
  sanitize_attributes: True
  sanitize_style: False
  sanitize_tags: True
  searchable: True
  sortable: True
  store: True
  string: Authorize Message
  strip_classes: False
  strip_style: False
  translate: True
  type: html
Field: done_msg
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: The message displayed if the order is successfully done after the payment process
  manual: False
  name: done_msg
  readonly: False
  required: False
  sanitize: True
  sanitize_attributes: True
  sanitize_style: False
  sanitize_tags: True
  searchable: True
  sortable: True
  store: True
  string: Done Message
  strip_classes: False
  strip_style: False
  translate: True
  type: html
Field: cancel_msg
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: The message displayed if the order is cancelled during the payment process
  manual: False
  name: cancel_msg
  readonly: False
  required: False
  sanitize: True
  sanitize_attributes: True
  sanitize_style: False
  sanitize_tags: True
  searchable: True
  sortable: True
  store: True
  string: Cancelled Message
  strip_classes: False
  strip_style: False
  translate: True
  type: html
Field: support_tokenization
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: ['code']
  exportable: True
  groupable: False
  manual: False
  name: support_tokenization
  readonly: True
  required: False
  searchable: False
  sortable: False
  store: False
  string: Tokenization
  type: boolean
Field: support_manual_capture
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: ['code']
  exportable: True
  groupable: False
  manual: False
  name: support_manual_capture
  readonly: True
  required: False
  searchable: False
  selection: [['full_only', 'Full Only'], ['partial', 'Partial']]
  sortable: False
  store: False
  string: Manual Capture Supported
  type: selection
Field: support_express_checkout
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: ['code']
  exportable: True
  groupable: False
  manual: False
  name: support_express_checkout
  readonly: True
  required: False
  searchable: False
  sortable: False
  store: False
  string: Express Checkout
  type: boolean
Field: support_refund
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: ['code']
  exportable: True
  groupable: False
  help: Refund is a feature allowing to refund customers directly from the payment in Odoo.
  manual: False
  name: support_refund
  readonly: True
  required: False
  searchable: False
  selection: [['none', 'Unsupported'], ['full_only', 'Full Only'], ['partial', 'Full & Partial']]
  sortable: False
  store: False
  string: Refund
  type: selection
Field: image_128
  attachment: True
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: False
  manual: False
  name: image_128
  readonly: False
  required: False
  searchable: True
  sortable: False
  store: True
  string: Image
  type: binary
Field: color
  aggregator: sum
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: ['state', 'module_state']
  exportable: True
  groupable: True
  help: The color of the card in kanban view
  manual: False
  name: color
  readonly: True
  required: False
  searchable: True
  sortable: True
  store: True
  string: Color
  type: integer
Field: module_id
  change_default: False
  company_dependent: False
  context: {}
  default_export_compatible: False
  depends: []
  domain: []
  exportable: True
  groupable: True
  manual: False
  name: module_id
  readonly: False
  relation: ir.module.module
  required: False
  searchable: True
  sortable: True
  store: True
  string: Corresponding Module
  type: many2one
Field: module_state
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: ['module_id.state']
  exportable: True
  groupable: True
  manual: False
  name: module_state
  readonly: True
  related: module_id.state
  required: False
  searchable: True
  selection: [['uninstallable', 'Uninstallable'], ['uninstalled', 'Not Installed'], ['installed', 'Installed'], ['to upgrade', 'To be upgraded'], ['to remove', 'To be removed'], ['to install', 'To be installed']]
  sortable: True
  store: False
  string: Installation State
  type: selection
Field: module_to_buy
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: ['module_id.to_buy']
  exportable: True
  groupable: True
  manual: False
  name: module_to_buy
  readonly: True
  related: module_id.to_buy
  required: False
  searchable: True
  sortable: True
  store: False
  string: Odoo Enterprise Module
  type: boolean
Field: id
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  manual: False
  name: id
  readonly: True
  required: False
  searchable: True
  sortable: True
  store: True
  string: ID
  type: integer
Field: display_name
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: ['name']
  exportable: True
  groupable: False
  manual: False
  name: display_name
  readonly: True
  required: False
  searchable: True
  sortable: False
  store: False
  string: Display Name
  translate: False
  trim: True
  type: char
Field: create_uid
  change_default: False
  company_dependent: False
  context: {}
  default_export_compatible: False
  depends: []
  domain: []
  exportable: True
  groupable: True
  manual: False
  name: create_uid
  readonly: True
  relation: res.users
  required: False
  searchable: True
  sortable: True
  store: True
  string: Created by
  type: many2one
Field: create_date
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  manual: False
  name: create_date
  readonly: True
  required: False
  searchable: True
  sortable: True
  store: True
  string: Created on
  type: datetime
Field: write_uid
  change_default: False
  company_dependent: False
  context: {}
  default_export_compatible: False
  depends: []
  domain: []
  exportable: True
  groupable: True
  manual: False
  name: write_uid
  readonly: True
  relation: res.users
  required: False
  searchable: True
  sortable: True
  store: True
  string: Last Updated by
  type: many2one
Field: write_date
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  manual: False
  name: write_date
  readonly: True
  required: False
  searchable: True
  sortable: True
  store: True
  string: Last Updated on
  type: datetime
Field: authorize_login
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: The ID solely used to identify the account with Authorize.Net
  manual: False
  name: authorize_login
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: API Login ID
  translate: False
  trim: True
  type: char
Field: authorize_transaction_key
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  groups: base.group_system
  manual: False
  name: authorize_transaction_key
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: API Transaction Key
  translate: False
  trim: True
  type: char
Field: authorize_signature_key
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  groups: base.group_system
  manual: False
  name: authorize_signature_key
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: API Signature Key
  translate: False
  trim: True
  type: char
Field: authorize_client_key
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: The public client key. To generate directly from Odoo or from Authorize.Net backend.
  manual: False
  name: authorize_client_key
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: API Client Key
  translate: False
  trim: True
  type: char
Field: paypal_email_account
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: The public business email solely used to identify the account with PayPal
  manual: False
  name: paypal_email_account
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: Email
  translate: False
  trim: True
  type: char
Field: paypal_client_id
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  manual: False
  name: paypal_client_id
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: PayPal Client ID
  translate: False
  trim: True
  type: char
Field: paypal_client_secret
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  groups: base.group_system
  manual: False
  name: paypal_client_secret
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: PayPal Client Secret
  translate: False
  trim: True
  type: char
Field: paypal_access_token
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  groups: base.group_system
  help: The short-lived token used to access Paypal APIs
  manual: False
  name: paypal_access_token
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: PayPal Access Token
  translate: False
  trim: True
  type: char
Field: paypal_access_token_expiry
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  groups: base.group_system
  help: The moment at which the access token becomes invalid.
  manual: False
  name: paypal_access_token_expiry
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: PayPal Access Token Expiry
  type: datetime
Field: paypal_webhook_id
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  manual: False
  name: paypal_webhook_id
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: PayPal Webhook ID
  translate: False
  trim: True
  type: char
Field: journal_id
  change_default: False
  company_dependent: False
  context: {}
  default_export_compatible: False
  depends: ['code', 'state', 'company_id']
  domain: (company_id and ['|', ('company_id', '=', False), ('company_id', 'parent_of', [company_id])] or ['|', ('company_id', '=', False), ('company_id', 'parent_of', '')]) + ([("type", "=", "bank")])
  exportable: True
  groupable: False
  help: The journal in which the successful transactions are posted.
  manual: False
  name: journal_id
  readonly: False
  relation: account.journal
  required: False
  searchable: False
  sortable: False
  store: False
  string: Payment Journal
  type: many2one
Field: so_reference_type
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: You can set here the communication type that will appear on sales orders.The communication will be given to the customer when they choose the payment method.
  manual: False
  name: so_reference_type
  readonly: False
  required: False
  searchable: True
  selection: [['so_name', 'Based on Document Reference'], ['partner', 'Based on Customer ID']]
  sortable: True
  store: True
  string: Communication
  type: selection
Field: website_id
  change_default: False
  company_dependent: False
  context: {}
  default_export_compatible: False
  depends: []
  domain: (company_id and [('company_id', 'in', [company_id] + [False])] or [('company_id', '=', False)]) + ([])
  exportable: True
  groupable: True
  manual: False
  name: website_id
  readonly: False
  relation: website
  required: False
  searchable: True
  sortable: True
  store: True
  string: Website
  type: many2one
Field: aps_merchant_identifier
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  help: The code of the merchant account to use with this provider.
  manual: False
  name: aps_merchant_identifier
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: APS Merchant Identifier
  translate: False
  trim: True
  type: char
Field: aps_access_code
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  groups: base.group_system
  help: The access code associated with the merchant account.
  manual: False
  name: aps_access_code
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: APS Access Code
  translate: False
  trim: True
  type: char
Field: aps_sha_request
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  groups: base.group_system
  manual: False
  name: aps_sha_request
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: APS SHA Request Phrase
  translate: False
  trim: True
  type: char
Field: aps_sha_response
  change_default: False
  company_dependent: False
  default_export_compatible: False
  depends: []
  exportable: True
  groupable: True
  groups: base.group_system
  manual: False
  name: aps_sha_response
  readonly: False
  required: False
  searchable: True
  sortable: True
  store: True
  string: APS SHA Response Phrase
  translate: False
  trim: True
  type: char
```