---
title: How to Build Your K8S Service
tags:
  - K8S
  - Docker
  - Minikube
  - Qemu
  - Hyperkit
  - Hyper-V
  - KVM
  - Parallels
  - Podman
  - VirtualBox
  - Vmware Fusion
  - Workstation
  - kubectl
categories:
  - Technology
  - K8S
date: 2023-12-11 09:23:12
description: How to Build Your K8S Service
lang: en
comments: true

---
Today we will use minikube tool build own K8S Service,Minikube is local Kubernetes, focusing on making it easy to learn and develop for Kubernetes.

All you need is Docker (or similarly compatible) container or a Virtual Machine environment, and Kubernetes is a single command away: 
```
minikube start
```

### What you'll need
1、2 CPUs or more  
2、2GB of free memory  
3、20GB of free disk space  
4、Internet connection  
5、Container or virtual machine manager, such as: Docker, QEMU, Hyperkit, Hyper-V, KVM, Parallels, [Podman](https://minikube.sigs.k8s.io/docs/drivers/podman/), [VirtualBox](https://minikube.sigs.k8s.io/docs/drivers/virtualbox/), or [VMware Fusion/Workstation](https://minikube.sigs.k8s.io/docs/drivers/vmware/)  

## 1、Install MiniKube
Click on the buttons that describe your taget platform. For other architectures, see [the minikute release page](https://github.com/kubernetes/minikube/releases/latest) for a complete list of minikube binaries.

To install the lastes minikube stable release on x86-64 Linux using binary download.
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
Other platform, you can see it [Minikube Install Doc](https://minikube.sigs.k8s.io/docs/start/)


## 2、 Minikube Start Your Cluster
From a terminal with administrator access(but not logged in as root) run:

```
minikube start
```
If minikube fails to start,see the [drivers page](https://minikube.sigs.k8s.io/docs/drivers/) for help setting up a compatible container or virtual-machine manager.

## Referce
[MiniKube](https://minikube.sigs.k8s.io/docs/start/)  