---
title: 在ubuntu中实现自动定时任务
tags:
  - Ubuntu
  - Crontab
categories:
  - Technology
  - Ubuntu
date: 2010-09-17 09:45:12
lang: zh-CN
---

> 如果想在ubuntu中实现某个时间或者每隔多久自动执行某些操作，可以使用内置的cron服务，

查询cron服务有没有运行可以使用：/etc/init.d/cron status

Cron服务提供以下几种方法供大家使用：
# 1.直接用crontab命令编辑
cron服务提供crontab命令来设定cron服务的，以下是这个命令的一些参数与说明：
crontab -u //设定某个用户的cron服务，一般root用户在执行这个命令的时候需要此参数
crontab -l //列出某个用户cron服务的详细内容
crontab -r //删除没个用户的cron服务
crontab -e //编辑某个用户的cron服务
比如说root查看自己的cron设置：crontab -u root -l
再例如，root想删除fred的cron设置：crontab -u fred -r
在编辑cron服务时，编辑的内容有一些格式和约定，输入：crontab -u root -e
进入vi编辑模式，编辑的内容一定要符合下面的格式：*/1 * * * * ls >> /tmp/ls.txt

这 个格式的前一部分是对时间的设定，后面一部分是要执行的命令，如果要执行的命令太多，可以把这些命令写到一个脚本里面，然后在这里直接调用这个脚本就可以 了，调用的时候记得写出命令的完整路径。时间的设定我们有一定的约定，前面五个*号代表五个数字，数字的取值范围和含义如下：

1---分钟（0-59）
2--小时（0-23）
3---日期（1-31）
4---月份（1-12）
5---星期（0-6）//0代表星期天

除了数字还有几个个特殊的符号就是"*"、"/"和"-"、","，*代表所有的取值范围内的数字，"/"代表每的意思,"*/5"表示每5个单位，"-"代表从某个数字到某个数字,","分开几个离散的数字。以下举几个例子说明问题：

A、每天早上6点
0 6 * * * echo "Good morning." >> /tmp/test.txt //注意单纯echo，从屏幕上看不到任何输出，因为cron把任何输出都email到root的信箱了。

B、每两个小时
0 */2 * * * echo "Have a break now." >> /tmp/test.txt

C、晚上11点到早上8点之间每两个小时，早上八点
0 23-7/2，8 * * * echo "Have a good dream：）" >> /tmp/test.txt

D、每个月的4号和每个礼拜的礼拜一到礼拜三的早上11点
0 11 4 * 1-3 command line

E、1月1日早上4点
0 4 1 1 * command line

每 次编辑完某个用户的cron设置后，cron自动在/var/spool/cron下生成一个与此用户同名的文件，此用户的cron信息都记录在这个文件 中，这个文件是不可以直接编辑的，只可以用crontab -e 来编辑。cron启动后每过一份钟读一次这个文件，检查是否要执行里面的命令。因此此文件修改后不需要重新启动cron服务。

# 2.编辑/etc/crontab 文件配置cron
cron 服务每分钟不仅要读一次/var/spool/cron内的所有文件，还需要读一次/etc/crontab,因此我们配置这个文件也能运用 cron服务做一些事情。用crontab配置是针对某个用户的，而编辑/etc/crontab是针对系统的任务。此文件的文件格式是：

SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root //如果出现错误，或者有数据输出，数据作为邮件发给这个帐号
HOME=/ //使用者运行的路径,这里是根目录

# run-parts
30 5 * * * reboot //每天早上5点30，自动重启服务器
01 * * * * root run-parts /etc/cron.hourly //每小时执行/etc/cron.hourly内的脚本，含义是每个小时的01分开始执行
02 4 * * * root run-parts /etc/cron.daily //每天执行/etc/cron.daily内的脚本，含义是每天的4点02分开始执行
22 4 * * 0 root run-parts /etc/cron.weekly //每星期执行/etc/cron.weekly内的脚本，含义是每个周日的4点22分执行
42 4 1 * * root run-parts /etc/cron.monthly //每月去执行/etc/cron.monthly内的脚本，含义是每个月1日的4点42分执行


注意上面的分钟错开设置是为了避免同时执行时产生冲突阻塞。可以根据执行时间的长短灵活设定。
大家注意"run-parts"这个参数了，如果去掉这个参数的话，后面就可以写要运行的某个脚本名，而不是文件夹名了。

可 以发现： /etc/下面分别有cron.hourly、cron.daily、cron.weekly、cron.monthly这几个文件夹，分别代 表每小诗、每天、每周、每月自动执行，那么根据你的要求把设计好的命令文件放到对应的文件夹下面，它就可以定时自动执行了。
