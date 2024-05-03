---
title: How to add cicd for bagisto ecommerce on github
tags:
  - Laravel
  - PHP
  - Bagisto
  - CICD
  - github
categories:
  - Technology
  - Laravel
date: 2023-12-22 09:23:12
description: How to add cicd for bagisto ecommerce on github
lang: en
comments: true
---
Today i want to add CICD for owner bagisto project on github. when create a anything project, maybe you should to configure it first that can save your many time.

```
name: Laravel

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  laravel-tests:

    runs-on: ubuntu-latest

    container:
      image: kirschbaumdevelopment/laravel-test-runner:8.1
    services:
      mysql:
        image: mysql:5.7
        env:
          MYSQL_ROOT_PASSWORD: password
          MYSQL_DATABASE: test
        ports:
          - 33306:3306
        options: --health-cmd="mysqladmin ping" --health-interval=10s --health-timeout=5s --health-retries=3

    steps:
    - uses: shivammathur/setup-php@15c43e89cdef867065b0213be354c2841860869e
      with:
        php-version: '8.1'
    - uses: actions/checkout@v3
    - name: Copy .env
      run: php -r "file_exists('.env') || copy('.env.example', '.env');"
    - name: Install Dependencies
      run: composer install -q --no-ansi --no-interaction --no-scripts --no-progress --prefer-dist
    - name: Directory Permissions
      run: chmod -R 777 storage bootstrap/cache
    - name: Generate key
      run: php artisan key:generate
    - name: Create Database
      run: |
        mkdir -p database
        touch database/database.sqlite
    - name: Execute tests (Unit and Feature tests) via pest
      env:
        DB_CONNECTION: mysql
        DB_HOST: mysql
        DB_PORT: 3306
        DB_DATABASE: test
        DB_USERNAME: root
        DB_PASSWORD: password
      run: php artisan migrate && php artisan db:seed && vendor/bin/pest
```
