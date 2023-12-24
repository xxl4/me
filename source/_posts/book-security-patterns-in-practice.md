---
title: 安全模式 最佳实践 Security Patterns In Practice
tags:
  - 安全
categories:
  - 书籍
  - 安全
date: 2023-12-24 10:23:12
description: 安全模式 最佳实践 Security Patterns In Practice 9787111501077
lang: zh-CN
---
# 第一章 动机与目的
## 1.1 为什么需要安全模式
## 1.2 基本定义
## 1.3 安全模式的历史
## 1.4 安全模式的工业级应用
## 1.5 其他建设安全系统的方法
# 第二章 模式与安全模式
## 2.1 什么是安全模式
## 2.2 安全模式的性质
## 2.3 模式的描述与目录
## 2.4 安全模式的剖析
## 2.5 模式图
## 2.6 如何对安全模式分类
## 2.7 模式挖掘
## 2.8 安全模式的应用
## 2.9 如何评估安全模式及其对安全的影响
## 2.10 威胁建模和滥用模式
## 2.11 容错模式
# 第三章 安全系统开发方法
## 3.1 为模式增加信息
## 3.2 基于生命周期的方法
## 3.3 采用模型驱动的工程方法
# 第四章 身份管理模式
## 4.1 概述
## 4.2 信任环
## 4.3 身份提供者
## 4.4 身份联合
## 4.5 自由联盟身份联合
# 第五章 身份认证模式
## 5.1 概述
## 5.2 认证器
## 5.3 远程认证器/授权者
## 5.4 凭据
# 第六章 访问控制模式
## 6.1 概述
## 6.2 授权
## 6.3 基于角色的访问控制
## 6.4 多级安全
## 6.5 基于策略的访问控制
## 6.6 访问控制列表
## 6.7 权能
## 6.8 具体化的引用监控器
## 6.9 受控的访问会话
## 6.10 基于会话和角色的访问控制
## 6.11 安全日志和审计
# 第七章 安全进程控制模式
## 7.1 概述
## 7.2 安全进程/线程
## 7.3 受控进程创建器
## 7.4 受控对象工厂
## 7.5 受控对象监控器
## 7.6 受保护的入口点
## 7.7 保护环
# 第八章 安全执行模式和文件管理模式
## 8.1 概述
## 8.2 虚拟地址空间访问控制
## 8.3 执行域
## 8.4 受控执行域
## 8.5 虚拟地址空间结构选择
# 第九章 安全操作系统体系结构和管理模式
## 9.1 概述
## 9.2 模块化操作系统体系结构
## 9.3 分层操作系统体系结构
## 9.4 微内核操作系统体系结构
## 9.5 虚拟机操作系统体系结构
## 9.6 管理员分级
## 9.7 文件访问控制
# 第十章 网络安全模式
## 10.1 概述
## 10.2 抽象虚拟专用网
## 10.3 IPSec虚拟专用网
## 10.4 传输层安全虚拟专用网
## 10.5 传输层安全
## 10.6 抽象入侵检测系统
## 10.7 基于签名的入侵检测系统
## 10.8 基于行为的入侵检测系统
# 第十一章 Web 服务安全模式
## 11.1 概述
## 11.2 应用防火墙
## 11.3 XML防火墙
## 11.4 XACML授权
## 11.5 XACML访问控制评估
## 11.6 Web服务策略语言
## 11.7 WS策略
## 11.8 WS信任
## 11.9 SAML断言
# 第十二章 Web 服务密码学模式
## 12.1 概述
## 12.2 对称加密
## 12.3 非对称加密
## 12.4 运用散列法的数字签名
## 12.5 XML加密
## 12.6 XML签名
## 12.7 WS安全
# 第十三章 安全中间件模式
## 13.1 概述
## 13.2 安全经纪人
## 13.3 安全管道和过滤器
## 13.4 安全黑板
## 13.5 安全适配器
## 13.6 安全的三层结构
## 13.7 安全企业服务总线
## 13.8 安全的分布式发布/订购
## 13.9 安全的“模型–视图–控制器”
# 第十四章 误用模式
## 14.1 概述
## 14.2 蠕虫
## 14.3 VoIP中的拒绝服务
## 14.4 Web服务欺骗
# 第十五章 云计算架构模式
## 15.1 简介
## 15.2 基础设施即服务
## 15.3 平台即服务
## 15.4 软件即服务
# 第十六章 构建安全的架构
## 16.1 列举威胁
## 16.2 分析阶段
## 16.3 设计阶段
## 16.4 法律案例的安全处理
## 16.5 SCADA系统
## 16.6 医疗应用
## 16.6.1 医疗记录及其规程
## 16.6.2 病人治疗记录模式
## 16.6.3 病人记录模式
## 16.7 环境辅助生活
## 16.8 无线网络安全
## 16.9 本章小结
# 第十七章 安全模式总结及安全模式的未来
## 17.1 安全模式总结
## 17.2 安全模式的未来研究方向
## 17.3 安全原则
## 17.4 未来展望
# 附录 XACML 访问控制评估的伪代码
# 术语

# 术语
### A&A 
授权和访问控制（Authorization And Access control）授权定义了基于访问器（用户，执行流程），被访问资源和资源的目标用户对资源许可的访问。访问控制定义了授权的执行机制。

### AAL
环境辅助生活（Ambient Assisted Living）.家居环境的架构，包括传感器和摄像头等设备以支持和监控身体机能受损的人与残疾人

### Access Matrix (访问矩阵)
授权模型表明对每个活动对象（主体），能够获取什么资源（对象或者受保护的对象），以及如何获取（访问类型）

### ACL
访问控制列表（Access Controll List）,和莫一对象绑定，表明哪些主体可以通过何种方式访问对象。

### Analysis Stage

### Antipattern

### API

### Authentication

### Authorization

### Bastion Host

### Brief

### class Diagram

### clearance

### Cloud computing

### collahnration diagram

### compartment

### confidentiality

### contract

### credential

### CSA (cloud security alliance)

### cyberphysical system

### DDOS

### defendant

### deployment diagram (UML)

### deposition

### descriptor

### diagram

### digital signature

### Domain

### DOS

### EHR (electronic healthcare record)

### ESB (Enterprise service bus)

### execution domain

### export

### federation

### firewall

### gatekeeper

### gateway

### HIPAA (Health Insurance Portability And Accountbility Act)

### hypervisor

### I&A (Identification and Authentication)

### IAM (Identify and Access Management)

### identify

### IDS (Instruction Detection System)

### information hiding

### intergrity

### IP (Internet protocol)

###  IPse

### ITG

### Layer

### liberty alliance identity federation

### logging and anditing

### MAC

### MDD Or MDE (Model-driven devclopment or Model-driven engineering)

# 
[安全模式最佳实践 购买](https://product.dangdang.com/23709802.html?ref=book-260513-3032_4-1652924-6)