---
title: How to Use try catch finally in your php code
tags:
  - PHP
  - Debug
  - Laravel
categories:
  - technology
  - PHP
date: 2023-12-04 20:23:12
description: How to Use try catch finally in your php code
---
今天在处理一块PHP的逻辑的是否，发现这块的地方很容易出错的情况，因为这块是一个队列的程序，很多异步的逻辑都会在插入到这边，从而完成异步的数据处理逻辑，在完成逻辑处理后，回告给到对方。
场景是很简单的，只是这块影响关系到的业务场景毕竟多，并且也是经常有需求的变化更新，万一在代码逻辑测试不充分的情况下，就容易造成这块的业务的停止和消耗。
为了应对这种情况的发生，我们初步确定使用相对简单和粗暴的方式，就是基于 try catch 去获取到错误，从而针对有异常的数据，可以抛到其他的数据标识，交付给到其他的程序继续处理或者排查

```

$filenane = "goods_export_".$item->id.".xlsx";
try {
    Excel::store(new GoodsExport($this->redisKey), $filenane , "public", \Maatwebsite\Excel\Excel::XLSX);
}catch(Exception $e) {
    var_dump($e);
}finally {
    \App\Models\Sd\Process::where("id", $item->id)->update(["status"=> 2, "filename"=>"程序有异常，请检查"]); //
}

```

针对与容易出异常的程序，大家一定还是需要多使用 try catch 的动作，从而也可以更好的保障程序的健壮性。

[source medium.com](https://medium.com/@cdndns/how-to-use-try-catch-finally-in-your-php-code-b166a140c075)