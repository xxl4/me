---
title: How to write a Magento 2 module in 30 minutes
date: 2024-09-23 17:45:00
tags: [magento2, module, tutorial, php, magento]
lang: en
category: tutorial
description: A quick guide to create a Magento 2 module in 30 minutes
comments: true
sitemap: true
---

# How to write a Magento 2 module in 30 minutes

In this tutorial, we will create a simple Magento 2 module that will display a message on the frontend. We will use the following steps:

1. Create the module directory structure

2. Create the module registration file

3. Create the module configuration file

4. Create the module block class

5. Create the module layout file

6. Create the module template file

7. Enable the module

Let's get started!

## Step 1: Create the module directory structure

First, we need to create the directory structure for our module. We will create a directory named `Vendor` in the `app/code` directory of our Magento 2 installation. Inside the `Vendor` directory, we will create a directory named `Module`.

```bash
mkdir -p app/code/Vendor/Module
```

## Step 2: Create the module registration file

Next, we need to create the module registration file. This file will register our module with Magento 2. Create a file named `registration.php` in the `app/code/Vendor/Module` directory with the following content:

```php
<?php

\Magento\Framework\Component\ComponentRegistrar::register(
    \Magento\Framework\Component\ComponentRegistrar::MODULE,
    'Vendor_Module',
    __DIR__
);
```

## Step 3: Create the module configuration file

Now, we need to create the module configuration file. Create a file named `module.xml` in the `app/code/Vendor/Module/etc` directory with the following content:

```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="Vendor_Module" setup_version="1.0.0"/>
</config>
```

## Step 4: Create the module block class

Next, we need to create the module block class. Create a file named `Message.php` in the `app/code/Vendor/Module/Block` directory with the following content:

```php
<?php

namespace Vendor\Module\Block;

use Magento\Framework\View\Element\Template;

class Message extends Template
{
    public function getMessage()
    {
        return 'Hello, Magento 2!';
    }
}
```

## Step 5: Create the module layout file

Now, we need to create the module layout file. Create a file named `default.xml` in the `app/code/Vendor/Module/view/frontend/layout` directory with the following content:

```xml
<?xml version="1.0"?>
<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <body>
        <referenceContainer name="content">
            <block class="Vendor\Module\Block\Message" name="message" template="Vendor_Module::message.phtml"/>
        </referenceContainer>
    </body>
</page>
```

## Step 6: Create the module template file

Finally, we need to create the module template file. Create a file named `message.phtml` in the `app/code/Vendor/Module/view/frontend/templates` directory with the following content:

```html

<h1><?php echo $block->getMessage(); ?></h1>
```

## Step 7: Enable the module

Now that we have created all the necessary files for our module, we need to enable it. Run the following commands in the root directory of your Magento 2 installation:

```bash
php bin/magento module:enable Vendor_Module

php bin/magento setup:upgrade
```

That's it! You have successfully created a Magento 2 module that will display a message on the frontend. You can now visit your Magento 2 store and see the message displayed on the homepage.

I hope you found this tutorial helpful. If you have any questions or comments, please leave them below.

Happy coding!
```

