---
title: Use Javascript disabled the right click and f12 Develop
tags:
  - Javascript
categories:
  - Technology
  - Javascript
date: 2023-12-01 13:45:12
lang: en
---
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>My page</title>
    <!-- Bootstrap core CSS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
	
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <style>
		html, body
		{
			width:100%;
			height:100%;
		}
    </style>
  </head>
  <body oncontextmenu="self.event.returnValue = false">
    <!-- Page Content -->
    <div class="container-fuid">
      <div class="row">
        <div class="col-lg-12 text-center">
          <h1 class="mt-5">Bootstrap 5 start page</h1>
          <p class="lead">Start by dragging components to page or double click to edit text</p>
        </div>
      </div>
    </div>
  </body>
  <script>
    //disabled the page when use right click to view source
    document.οncοntextmenu=function(){return false;}; 
    document.onselectstart=function(){return false;};
    let h = window.innerHeight;
    let w = window.innerWidth;

    //disabled the right click
    document.oncontextmenu = function () { return false; };
 
    // disabled the user use f12 and shift+ctrl+i use develop tool
    window.onkeydown = window.onkeyup = window.onkeypress = function () {
        window.event.returnValue = false;
        return false;
    }

    // disabled the javascript debug tool F12
    document.onkeydown = function () {
        if (window.event && window.event.keyCode == 123) {
            event.keyCode = 0;
            event.returnValue = false;
            return false;
        }
    };

    //check the page width and height,when the page height and width have change,will close the page
    window.onresize = function () {
        if (h != window.innerHeight || w != window.innerWidth) {
            window.close();
            window.location = "about:blank";
        }
    }
    </script>
</html>

```