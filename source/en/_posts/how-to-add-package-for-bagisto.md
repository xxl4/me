---
title: How to add your own package into Bagisto ecommerce
tags:
  - Laravel
  - PHP
  - Bagisto
  - ecommerce
  - Packages
categories:
  - Technology
  - Laravel
date: 2023-12-15 09:23:12
description: How to add your own package into Bagisto ecommerce
lang: en
comments: true
---
Bagisto is an Open source Laravel eCommerce platform for building marketplaces, mobile apps, blockchain, and headless commerce. She is from beautiful Indian, Use Laravel 10 for build.
```
.
└── Webkul
    ├── Admin
    ├── Attribute
    ├── CartRule
    ├── CatalogRule
    ├── Category
    ├── Checkout
    ├── CMS
    ├── Core
    ├── Customer
    ├── DataGrid
    ├── DebugBar
    ├── FPC
    ├── Installer
    ├── Inventory
    ├── Marketing
    ├── Notification
    ├── OneBuy
    ├── Payment
    ├── Paypal
    ├── Product
    ├── Rule
    ├── Sales
    ├── Shipping
    ├── Shop
    ├── Sitemap
    ├── SocialLogin
    ├── SocialShare
    ├── Tax
    ├── Theme
    └── User
```
This is the Bagisto main packages directory tree info.

# Manual Setup of Files
if you perfer to set up your package manually,follow these steps assuming you are familiar with package directory structures and workflows. We'll use the default package folder in Bagisto as an example

## Create Package Directory
1、Inside the ***packages/Webkul*** folder,create a folder withd your package name. 
2、In your package folder, create a folder named as src. This is where you will put all your package-related files. Your updated structure will look like this:

```
./Webkul/OneBuy/
└── src
    ├── composer.json
    ├── Config
    ├── Http
    ├── Providers
    ├── Resources
    └── Routes
```

# Create Service Provider
1、In the ***src*** folder, creat a folder named as ***Providers***. Inside that folder, create a file named as ***OneBuyServiceProvider.php***. Your structure should look like this:
```
./Webkul/OneBuy/
└── src
    ├── composer.json
    ├── Config
    ├── Http
    │   ├── Controllers
    │   └── routes.php
    ├── Providers
    │   └── OneBuyServiceProvider.php
    ├── Resources
    │   ├── assets
    │   └── views
    └── Routes
```
2、Copy the following code and paste it into ***OneBuyServiceProvider.php***
```
<?php

namespace Nicelizhi\OneBuy\Providers;

use Illuminate\Pagination\Paginator;
use Illuminate\Routing\Router;
use Illuminate\Support\Facades\Blade;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\ServiceProvider;
use Webkul\Shop\Http\Middleware\AuthenticateCustomer;
use Webkul\Shop\Http\Middleware\Currency;
use Webkul\Shop\Http\Middleware\Locale;
use Webkul\Shop\Http\Middleware\Theme;

class OneBuyServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap services.
     *
     * @return void
     */
    public function boot(Router $router)
    {
        
        include __DIR__ . '/../Http/routes.php';

        $this->loadViewsFrom(__DIR__ . '/../Resources/views', 'onebuy');

        /* aliases */
        $router->aliasMiddleware('currency', Currency::class);
        $router->aliasMiddleware('locale', Locale::class);
        $router->aliasMiddleware('customer', AuthenticateCustomer::class);
        $router->aliasMiddleware('theme', Theme::class);

        /* View Composers */
        //$this->composeView();

        /* Paginator */
        Paginator::defaultView('shop::partials.pagination');
        Paginator::defaultSimpleView('shop::partials.pagination');

        Blade::anonymousComponentPath(__DIR__ . '/../Resources/views/components', 'onebuy');

        /*
        $this->app->register(EventServiceProvider::class);
        */
    }

    /**
     * Register services.
     *
     * @return void
     */
    public function register()
    {
        $this->registerConfig();
    }

    /**
     * Register package config.
     *
     * @return void
     */
    protected function registerConfig()
    {
        /*
        $this->mergeConfigFrom(
            dirname(__DIR__) . '/Config/paymentmethods.php', 'payment_methods'
        );
        */
    }
}
```
# Register Your Package
1、Add your package's namespace to the psr-4 section in the composer.json file located in the root directory of your Bagisto application. Update it as follows:
```
"autoload": {
    ...
    "psr-4": {
        // Other PSR-4 namespaces
        "Nicelizhi\\OneBuy\\": "packages/Webkul/OneBuy/src"
    }
}
```
2、Register your package's service provider in the config/app.php file located in the root directory of your Bagisto application. Add the following line to the providers array:
```
<?php

return [
    
    // Other configuration options

    'providers' => ServiceProvider::defaultProviders()->merge([
        // Other service providers
        Nicelizhi\OneBuy\Providers\OneBuyServiceProvider::class,
    ])->toArray(),
    
    // Other configuration options
];
```
3、Run the following command to autoload your package:
```
composer dump-autoload
```
Your package is now read to use !

The page code from [https://github.com/nicelizhi/Bagisto](https://github.com/nicelizhi/Bagisto) if you want try it, you can git clone and do it.