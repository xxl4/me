---
title: How to write a module in Odoo
date: 2025-04-03 00:00:00
tags: [odoo, module, tutorial]
categories: [odoo, module]
description: This tutorial will guide you through the process of creating a custom module in Odoo, including the necessary files and structure.
image: /assets/images/odoo/how-to-write-a-module-in-odoo.png
imageAlt: Odoo Module Tutorial
comment: true
sitemap: true
keywords: [odoo, module, tutorial]
---

# How to write a module in Odoo

Odoo is a powerful open-source ERP system that allows developers to create custom modules to extend its functionality. In this tutorial, we will guide you through the process of creating a custom module in Odoo, including the necessary files and structure.
We will create a simple module that adds a new model to Odoo. This module will be named `my_module` and will contain a model called `my_model` with a few fields.


## Prerequisites
Before we start, make sure you have the following prerequisites installed on your system:
- Odoo (version 14 or later)
- Python 3.6 or later
- PostgreSQL
- Basic knowledge of Python and Odoo development


## Step 1: Create the Module Directory Structure
First, we need to create the directory structure for our module. Navigate to the Odoo addons directory and create a new folder for your module:

```bash
cd /path/to/odoo/addons
mkdir my_module
cd my_module
```

Now, create the following directory structure inside `my_module`:

```bash
mkdir -p models views security data
```
This structure will hold our Python models, XML views, security rules, and data files.


## Step 2: Create the Manifest File
The manifest file is a Python file named `__manifest__.py` that contains metadata about your module. Create this file in the `my_module` directory:

```bash
touch __manifest__.py
```

Open the `__manifest__.py` file and add the following content:

```python
{
    'name': 'My Module',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'A simple custom module for Odoo',
    'description': """
        This module adds a new model to Odoo.
    """,
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/my_model_views.xml',
        'data/my_model_data.xml',
    ],
    'installable': True,
    'application': True,
}
```
This file contains information about the module, such as its name, version, dependencies, and data files to load. Make sure to replace `Your Name` and `https://yourwebsite.com` with your actual name and website.


## Step 3: Create the Model

Next, we will create a new model in Odoo. Create a new Python file named `my_model.py` inside the `models` directory:

```bash
touch models/my_model.py
```

Open the `my_model.py` file and add the following content:

```python
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date_created = fields.Datetime(string='Date Created', default=fields.Datetime.now)
    active = fields.Boolean(string='Active', default=True)

    @api.constrains('name')
    def _check_name(self):
        for record in self:
            if not record.name:
                raise ValidationError("Name cannot be empty.")
```
This code defines a new model called `my.model` with four fields: `name`, `description`, `date_created`, and `active`. The `@api.constrains` decorator is used to enforce a constraint on the `name` field, ensuring it cannot be empty.


## Step 4: Create the Views
Next, we will create the XML views for our model. Create a new XML file named `my_model_views.xml` inside the `views` directory:

```bash
touch views/my_model_views.xml
```
Open the `my_model_views.xml` file and add the following content:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <data>
    <record id="view_my_model_tree" model="ir.ui.view">
        <field name="name">my.model.tree</field>
        <field name="model">my.model</field>
        <field name="arch" type="xml">
            <tree string="My Model">
                <field name="name"/>
                <field name="description"/>
                <field name="date_created"/>
                <field name="active"/>
            </tree>
        </field>
    </record>

    <record id="view_my_model_form" model="ir.ui.view">
        <field name="name">my.model.form</field>
        <field name="model">my.model</field>
        <field name="arch" type="xml">
            <form string="My Model">
                <sheet>
                    <group>
                        <group>
                            <field name="name"/>
                            <field name="description"/>
                        </group>
                        <group>
                            <field name="date_created" readonly="1"/>
                            <field name="active"/>
                        </group>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <record id="action_my_model" model="ir.actions.act_window">
        <field name="name">My Model</field>
        <field name="res_model">my.model</field>
        <field name="view_mode">tree,form</field>
    </record>

    <menuitem id="menu_my_model" name="My Model" action="action_my_model" parent="base.menu_custom"/>
    </data>
</odoo>
```

This XML file defines the tree and form views for our model, as well as an action to open the model and a menu item to access it. The `parent` attribute in the `menuitem` tag specifies the parent menu under which this menu item will be displayed. You can change `base.menu_custom` to any existing menu ID in your Odoo instance.
## Step 5: Create Security Rules

To allow users to access our model, we need to create security rules. Create a new CSV file named `ir.model.access.csv` inside the `security` directory:

```bash
touch security/ir.model.access.csv
```

Open the `ir.model.access.csv` file and add the following content:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_model,access_my_model,model_my_model,,1,1,1,1
```

This CSV file defines access rights for our model. The `perm_read`, `perm_write`, `perm_create`, and `perm_unlink` columns specify the permissions for reading, writing, creating, and deleting records, respectively. In this case, we are granting all permissions to the model.

## Step 6: Create Sample Data (Optional)

If you want to create some sample data for your model, you can create a new XML file named `my_model_data.xml` inside the `data` directory:

```bash
touch data/my_model_data.xml
```
Open the `my_model_data.xml` file and add the following content:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <data noupdate="1">
        <record id="my_model_1" model="my.model">
            <field name="name">Sample Model 1</field>
            <field name="description">This is a sample model.</field>
            <field name="active">True</field>
        </record>

        <record id="my_model_2" model="my.model">
            <field name="name">Sample Model 2</field>
            <field name="description">This is another sample model.</field>
            <field name="active">True</field>
        </record>
    </data>
</odoo>
```

This XML file creates two sample records for our model. The `noupdate="1"` attribute indicates that this data should not be updated if the module is installed again.
## Step 7: Install the Module

Now that we have created all the necessary files, we can install our module. Start your Odoo server and navigate to the Apps menu in the Odoo interface. Click on the "Update Apps List" button to refresh the list of available modules.
Once the list is updated, search for "My Module" and click on the "Install" button to install it.

## Step 8: Test the Module

After installing the module, you should see a new menu item called "My Model" in the Odoo interface. Click on it to access the model's tree view. You can create new records, edit existing ones, and test the functionality of your module.
You can also check the form view by clicking on any record in the tree view. The form view should display the fields we defined in the model.

## Conclusion
In this tutorial, we have created a simple custom module in Odoo that adds a new model with a few fields and views. We also defined security rules and created sample data for the model. This is just a basic example, and you can extend the functionality of your module by adding more features, such as workflows, reports, and custom business logic.

Feel free to explore the Odoo documentation and community resources to learn more about Odoo development and best practices. Happy coding!

### Additional Resources
- [Odoo Documentation](https://www.odoo.com/documentation/14.0/)
- [Odoo Community](https://www.odoo.com/forum/help-1)
- [odoo cookbook](https://github.com/iTranslateX/odoo-cookbook)
- [odoo hub](https://dev.odoohub.com.cn/upper/VIEWS.html)
- [Qweb Document](https://www.odooai.cn/documentation/16.0/zh_CN/developer/reference/frontend/qweb.html)