---
title: How to create a new module in odoo
date: 2024-12-27 13:59:59
tags: [Odoo, Module, Erp, Python]
category: Erp
lang: en
comments: true
sitemap: true
description: How to create a new module in odoo, odoo module development, odoo module creation, odoo module structure, odoo module tutorial, odoo module example, odoo module installation, odoo module development tutorial, odoo module development example, odoo module development structure, odoo module development installation, odoo module development tutorial example, odoo module development example structure installation, odoo module development tutorial example structure installation.
---

# How to create a new module in odoo

## 1. Create a new module

```shell
$ odoo scaffold shipping_cne /www/odoo/addons
```

## 2. Create a new model

```python
# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ShippingCne(models.Model):
    _name = 'shipping.cne'
    _description = 'Shipping CNE'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
```

## 3. Create a new view

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <record id="view_shipping_cne_form" model="ir.ui.view">
            <field name="name">shipping.cne.form</field>
            <field name="model">shipping.cne</field>
            <field name="arch" type="xml">
                <form string="Shipping CNE">
                    <sheet>
                        <group>
                            <field name="name"/>
                            <field name="code"/>
                            <field name="description"/>
                            <field name="active"/>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>

        <record id="view_shipping_cne_tree" model="ir.ui.view">
            <field name="name">shipping.cne.tree</field>
            <field name="model">shipping.cne</field>
            <field name="arch" type="xml">
                <tree string="Shipping CNE">
                    <field name="name"/>
                    <field name="code"/>
                    <field name="description"/>
                    <field name="active"/>
                </tree>
            </field>
        </record>

        <record id="action_shipping_cne" model="ir.actions.act_window">
            <field name="name">Shipping CNE</field>
            <field name="res_model">shipping.cne</field>
            <field name="view_mode">tree,form</field>
        </record>

        <menuitem id="menu_shipping_cne" name="Shipping CNE" parent="base.menu_sales" action="action_shipping_cne"/>
    </data>
</odoo>
```

## 4. Update the manifest file

```python
{
    'name': 'Shipping CNE',
    'version': '1.0',
    'author': 'Steve Liu',
    'website': 'https://www.modeles.net.cn',
    'category': 'Sales',
    'depends': ['base'],
    'data': [
        'views/shipping_cne_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
```

## 5. Update the security file

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_shipping_cne,shipping.cne,model_shipping_cne,base.group_user,1,1,1,1
```

## 6. Update the `__init__.py` file

```python
from . import models
```

## 7. Update the `__manifest__.py` file

```python
{
    'name': 'Shipping CNE',
    'version': '1.0',
    'author': 'Steve Liu',
    'website': 'https://www.modeles.net.cn',
    'category': 'Sales',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/shipping_cne_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
``` 

## 8. Install the module

```shell
$ odoo -d odoo -i shipping_cne
```

## 9. Check the module

```shell
$ odoo -d odoo -u shipping_cne
```

# Conclusion

In this article, we have learned how to create a new module in odoo. We have learned how to create a new model, how to create a new view, how to update the manifest file, how to update the security file, how to update the `__init__.py` file, how to update the `__manifest__.py` file, how to install the module, how to check the module. I hope this article will help you to create a new module in odoo.



# Reference
[Server framework 101 Odoo](https://www.odoo.com/documentation/18.0/zh_CN/developer/tutorials/server_framework_101.html)