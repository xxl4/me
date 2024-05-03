---
title: Add Pest Testing Framework in your laravel project
tags:
  - Laravel
  - PHP
  - Pest
  - Phpunit
  - Tests
categories:
  - Technology
  - PHP
date: 2023-12-23 12:23:12
description: Add Pest Testing Framework in your laravel project
lang: en
comments: true
---

# Why Pest
When testing PHP code, you have access to a range of frameworks. Nevertheless, we believe that Pest is the most elegant and sophisticated testing framework in the world. It's designed to make the testing process enjoyable, and our goal is to make tests easy to read and understand, with a code syntax that closely resembles natural human language.
```
function sum($a, $b) {
    return $a + $b;
}
 
test('sum', function () {
  $result = sum(1, 2);
 
  expect($result)->toBe(3);
});
```
You can expect a smooth and efficient coding experience thanks to Pest's easy-to-use API inspired by Ruby's Rspec and Jest. In addition, the test reporting is well-organized, practical, and informative, with clear and concise error and stack trace displays for quick debugging. With Pest, you can obtain test reporting that is unmatched in its beauty, directly from the console!

![](https://pestphp.com/assets/img/failure.webp?1)


In addition to its exceptional test reporting, Pest also offers a range of other valuable features, including:

1、Built-in parallel features for faster test runs
2、Beautiful documentation that's easy to navigate
3、Native profiling tools to optimize slow-running tests
4、Out-of-the-box Architectural Testing to test application rules
5、Coverage report directly on the terminal to track code coverage
6、Dozens of optional plugins, such as Watch Mode and Snapshot testing, to customize Pest to fit your needs.

Whether you're engaged in a small personal project or a large-scale enterprise application, Pest has got you covered. So if you want to make the testing process enjoyable and efficient, give Pest a try. We're confident that you'll love it as much as we do.

# How to Installation  PEST
***Requirements: PHP 8.1+***

Installing Pest PHP Testing Framework is a simple process that can be completed in just a few steps. Before you begin, make sure you have PHP 8.1+ or higher installed on your system.

The first step is to require Pest as a "dev" dependency in your project by running the following command on your command line.

```
composer require pestphp/pest --dev --with-all-dependencies
```

Secondly, you'll need to initialize Pest in your current PHP project. This step will create a configuration file named Pest.php at the root level of your test suite, which will enable you to fine-tune your test suite later.

```
./vendor/bin/pest --init
```

Finally, you can run your tests by executing the pest command.

```
./vendor/bin/pest
```

Here is an example of the output displayed when running Pest in a new, fresh project.

![](https://pestphp.com/assets/img/pestinstall.webp?1)


Optionally, if you are migrating from PHPUnit, you can use the pest-plugin-drift package to automatically convert your PHPUnit tests to Pest. For more information, check out the [Migrating from PHPUnit guide](https://pestphp.com/docs/migrating-from-phpunit-guide).

# Referce
[Editor Setup](https://pestphp.com/docs/editor-setup)    
[Pest Github](https://github.com/pestphp/pest)  