---
title: How to deploy Nuxt.js
date: 2024-09-26 00:00:00
tags: [Nuxt.js, Deployment]
categories: [Development]
description: How to deploy a Nuxt.js application to a server.
comments: true
sitemap: true
lang: en
---

Nuxt.js is a popular framework for building Vue.js applications. In this article, we will discuss how to deploy a Nuxt.js application to a server.

### 1. Build the Nuxt.js application

Before deploying the Nuxt.js application, you need to build it. To build the application, run the following command in the terminal:

```bash
npm run build
```

This will generate a `dist` directory containing the built files.

### 2. Copy the built files to the server

Once the Nuxt.js application is built, you need to copy the built files to the server. You can use tools like `rsync` or `scp` to copy the files to the server.

For example, to copy the files to a server with the IP address `
```bash
rsync -avz dist/ user@server:/path/to/destination
```

### 3. Configure the server

After copying the built files to the server, you need to configure the server to serve the Nuxt.js application. You can use a web server like Nginx or Apache to serve the application.

For example, to configure Nginx to serve the Nuxt.js application, you can create a new server block in the Nginx configuration file:

```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        root /path/to/destination;
        try_files $uri $uri/ @spa;
    }

    location @spa {
        rewrite ^.*$ /index.html last;
    }
}
```

### 4. Start the server

After configuring the server, you can start the server to serve the Nuxt.js application. For example, to start Nginx, run the following command in the terminal:

```bash
sudo systemctl start nginx
```

### Conclusion

In this article, we discussed how to deploy a Nuxt.js application to a server. By following these steps, you can deploy your Nuxt.js application and make it accessible to users.
```