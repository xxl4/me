---
title: How to add testsing in your bagisto packages
tags:
  - Laravel
  - PHP
  - Bagisto
  - ecommerce
  - Packages
  - pets
  - PhpUnit
categories:
  - Technology
  - Laravel
date: 2023-12-22 11:23:12
description: How to add testsing in your bagisto packages
lang: en
comments: true
---

When you add a package, you should your testing case into Bagisto, and you can use this step for it.

phpunit.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<phpunit
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="./vendor/phpunit/phpunit/phpunit.xsd"
    bootstrap="vendor/autoload.php"
    colors="true"
>
    <testsuites>
        <!-- Admin package testsuites. -->
        <testsuite name="Admin Unit Test">
            <directory suffix="Test.php">./packages/Webkul/Admin/tests/Unit</directory>
        </testsuite>
        <testsuite name="Admin Feature Test">
            <directory suffix="Test.php">./packages/Webkul/Admin/tests/Feature</directory>
        </testsuite>

        <!-- DataGrid package testsuites. -->
        <testsuite name="DataGrid Unit Test">
            <directory suffix="Test.php">./packages/Webkul/DataGrid/tests/Unit</directory>
        </testsuite>
        <testsuite name="DataGrid Feature Test">
            <directory suffix="Test.php">./packages/Webkul/DataGrid/tests/Feature</directory>
        </testsuite>

        <!-- Shop package testsuites. -->
        <testsuite name="Shop Unit Test">
            <directory suffix="Test.php">./packages/Webkul/Shop/tests/Unit</directory>
        </testsuite>
        <testsuite name="Shop Feature Test">
            <directory suffix="Test.php">./packages/Webkul/Shop/tests/Feature</directory>
        </testsuite>

        <!-- Shopify package testsuites. -->
        <testsuite name="Shopify Unit Test">
            <directory suffix="Test.php">./packages/Webkul/Shopify/tests/Feature</directory>
        </testsuite>
    </testsuites>
    <source>
        <include>
            <directory suffix=".php">./app</directory>
        </include>
    </source>
    <php>
        <env name="APP_ENV" value="testing"/>
        <env name="BCRYPT_ROUNDS" value="4"/>
        <env name="CACHE_DRIVER" value="array"/>
        <!-- <env name="DB_CONNECTION" value="sqlite"/> -->
        <!-- <env name="DB_DATABASE" value=":memory:"/> -->
        <env name="MAIL_MAILER" value="array"/>
        <env name="QUEUE_CONNECTION" value="sync"/>
        <env name="SESSION_DRIVER" value="array"/>
        <env name="TELESCOPE_ENABLED" value="false"/>
    </php>
</phpunit>

```
composer.json
```
"autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/",
            "Webkul\\Admin\\Tests\\": "packages/Webkul/Admin/tests",
            "Webkul\\DataGrid\\Tests\\": "packages/Webkul/DataGrid/tests",
            "Webkul\\Shop\\Tests\\": "packages/Webkul/Shop/tests",
            "Nicelizhi\\Shopify\\Tests\\": "packages/Webkul/Shopify/tests"
        }
    }
```
Pest.php
```
uses(Webkul\Admin\Tests\AdminTestCase::class)->in('../packages/Webkul/Admin/tests');
uses(Webkul\DataGrid\Tests\DataGridTestCase::class)->in('../packages/Webkul/DataGrid/tests');
uses(Webkul\Shop\Tests\ShopTestCase::class)->in('../packages/Webkul/Shop/tests');

uses(Nicelizhi\Shopify\Tests\ShopifyTestCase::class)->in('../packages/Webkul/Shopify/tests');
```

finally, you can run it, and check the testing case info.

```
./vendor/bin/pest
```