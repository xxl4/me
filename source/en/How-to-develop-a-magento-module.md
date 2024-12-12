---
title: How to develop a Magento module
date: 2024-12-08 21:00:00
tags: [magento, module, development]
lang: en
comments: true
permalink: how-to-develop-a-magento-module
sitemap:
  lastmod: 2024-12-08 21:00:00
  priority: 0.8
  changefreq: monthly
description: A step-by-step guide to develop a Magento module.
cover: /images/en/2024/12/online-magento-module-development.png
---

![How to develop a Magento module](https://img2023.cnblogs.com/blog/94707/202412/94707-20241208214413862-1516604353.png)

# How to develop a Magento module

In this article, we will learn how to develop a Magento module. We will create a simple module that will display a message on the frontend.

## Step 1: Create the module directory

Create a directory for your module in the `app/code` directory of your Magento installation. For example, if your module is named `MyModule`, create the directory `app/code/MyModule`.

## Step 2: Create the module configuration file

Create a file named `module.xml` in the `app/code/MyModule/etc` directory. This file will contain the configuration of your module.

```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="MyModule" setup_version="1.0.0"/>
</config>
```

## Step 3: Create the registration file

Create a file named `registration.php` in the `app/code/MyModule` directory. This file will register your module with Magento.

```php
<?php
\Magento\Framework\Component\ComponentRegistrar::register(
    \Magento\Framework\Component\ComponentRegistrar::MODULE,
    'MyModule',
    __DIR__
);
```

## Step 4: Create the module configuration file

Create a file named `di.xml` in the `app/code/MyModule/etc` directory. This file will contain the configuration of your module.

```xml
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:ObjectManager/etc/config.xsd">
    <type name="Magento\Framework\View\Element\Template">
        <arguments>
            <argument name="data" xsi:type="array">
                <item name="my_module_message" xsi:type="string">Hello, world!</item>
            </argument>
        </arguments>
    </type>
</config>
```

## Step 5: Create the block class

Create a file named `Message.php` in the `app/code/MyModule/Block` directory. This file will contain the block class that will display the message on the frontend.

```php
<?php
namespace MyModule\Block;

class Message extends \Magento\Framework\View\Element\Template
{
    public function getMessage()
    {
        return $this->_getData('my_module_message');
    }
}
``` 

## Step 6: Create the template file

Create a file named `message.phtml` in the `app/code/MyModule/view/frontend/templates` directory. This file will contain the template that will display the message on the frontend.

```html
<p><?php echo $block->getMessage(); ?></p>
```

## Step 7: Create the layout file

Create a file named `default.xml` in the `app/code/MyModule/view/frontend/layout` directory. This file will contain the layout configuration for your module.

```xml
<?xml version="1.0"?>
<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <body>
        <referenceContainer name="content">
            <block class="MyModule\Block\Message" name="my_module_message" template="MyModule::message.phtml"/>
        </referenceContainer>
    </body>
</page>
```

## Step 8: Enable the module

Run the following command to enable the module:

```bash
php bin/magento module:enable MyModule
```

## Step 9: Register the module

Run the following command to register the module:

```bash
php bin/magento setup:upgrade
```

## Step 10: Clear the cache

Run the following command to clear the cache:

```bash
php bin/magento cache:clean
```

## Step 11: View the message

Visit your Magento store frontend to view the message displayed by your module.

That's it! You have successfully developed a Magento module.

Happy coding!

## References

- [Magento DevDocs](https://devdocs.magento.com/)
- [Magento Community Forums](https://community.magento.com/)
- [Magento Stack Exchange](https://magento.stackexchange.com/)
- [Magento GitHub Repository](https://github.com/magento/magento2)
- [Magento Marketplace](https://marketplace.magento.com/)
- [Magento Blog](https://magento.com/blog)
- [Magento Twitter](https://twitter.com/magento)
- [Magento Facebook](https://www.facebook.com/magento)
- [Magento YouTube](https://www.youtube.com/user/magentocommerce)
- [Magento LinkedIn](https://www.linkedin.com/company/magento)


