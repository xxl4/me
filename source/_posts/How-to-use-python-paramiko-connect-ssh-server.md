---
title: How to use python paramiko connect ssh server
date: 2024-12-18 21:45:00
tags: [python, paramiko, ssh, server, Linux, Unix, Ubuntu, CentOS, Debian, Fedora, RHEL, SUSE, OpenSUSE, Arch, Manjaro, Mint, Gentoo, Slackware, Alpine, Raspbian, Raspberry Pi, BeagleBone, Odroid, Banana Pi, Cubieboard, Orange Pi, Jetson Nano, Jetson Xavier, Jetson AGX, Jetson TX, Jetson TK, Jetson Developer Kit, Jetson, Nvidia, ARM, x86]
categories: [python, paramiko, ssh, server, Linux, Unix, Ubuntu, CentOS, Debian, Fedora, RHEL, SUSE]
lang: en
description: How to use python paramiko connect ssh server
sitemap:
  lastmod: 2024-12-18 21:45:00
  priority: 0.75
  changefreq: daily
---

# How to use python paramiko connect ssh server

## Python Paramiko

Paramiko is a Python (2.7, 3.4+) implementation of the SSHv2 protocol, providing both client and server functionality. While it leverages a Python C extension for low-level cryptography (Cryptography), Paramiko itself is a pure Python interface around SSH networking concepts.

## Install Paramiko

```bash
pip install paramiko
```

## Connect SSH Server

```python
# -*- coding: utf-8 -*-
# This is a small tool to report on successful logins
# to accounts other than those listed in the variable
# expected.  Such a report might lead to an investigation
# into how and why those other accounts were logging in.

import paramiko
import os

# connection the agent host use user and password or use private key and publish key
def connect(host, port, user, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, user, password)
        return ssh
    except Exception as e:
        print('[-] Error connecting to host: ' + str(e))
        return None

# connection the agent host use private key and publish key
def connect_key(host, port, user, key):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, user, key_filename=key)
        return ssh
    except Exception as e:
        print('[-] Error connecting to host: ' + str(e))
        return None

    
# execute command
def execute(ssh, command):
    try:
        stdin, stdout, stderr = ssh.exec_command(command)
        return stdout.read()
    except Exception as e:
        print('[-] Error executing command: ' + str(e))
        return None
    
# close connection
def close(ssh):
    ssh.close()

# main function
def main():
    host = ''
    port = 22
    user = "root"
    password = ""
    ssh = connect(host, port, user, password)
    if ssh:
        print(execute(ssh, 'ls -l'))

        # push server publish key to remote server
        
        # if the private key and publish key is not exist, generate it

        if os.path.exists(host + '_private.key') and os.path.exists(host + '_public.key'):
            print('[-] The private key and publish key is exist')
            return

        # generate the private key and publish key
        key = paramiko.RSAKey.generate(2048)
        public_key = key.get_base64()
        private_key = key.get_base64()

        # push the public key to remote server

        public_key = f"ssh-rsa {public_key} {user}@{host}"

        execute(ssh, 'echo ' + public_key + ' >> ~/.ssh/authorized_keys')

        print(public_key)

        # save the private key to local
        key.write_private_key_file(host + '_private.key')
        # save the public key to local
        with open(host + '_public.key', 'w') as public_key_file:
            public_key_file.write(public_key)

        close(ssh)
    else:
        print('[-] Connection failed')

def main_key():
    host = ''
    port = 22
    user = "root"
    ssh = connect_key(host, port, user, key= host + '_private.key')
    if ssh:
        print(execute(ssh, 'ls -l'))

        # check the public key is exist in remote server
        public_key = open(host + '_public.key', 'r').read()
        public_key = public_key.strip()
        print(public_key)
        authorized_keys = execute(ssh, 'cat ~/.ssh/authorized_keys')
        print(authorized_keys)
        if public_key in authorized_keys.decode("utf-8"):
            print('[-] The public key is exist')
        else:
            # push the public key to remote server
            execute(ssh, 'echo ' + public_key + ' >> ~/.ssh/authorized_keys')

        # install the agent to remote server

        # check the agent is exist in remote server

        # if not exist, push the agent to remote server

        # generate the agent config file

        # push the agent config file to remote server

        # start the agent


        close(ssh)
    else:
        print('[-] Connection failed')

if __name__ == '__main__':
    # main()
    main_key()

```

When you have managed to connect to the server, you can execute commands on the server. You can also push the public key to the server and install the agent on the server.

The agent is a small tool to report on successful logins to accounts other than those listed in the variable expected. Such a report might lead to an investigation into how and why those other accounts were logging in.

## Conclusion

In this article, we introduce how to use python paramiko connect ssh server.

## Reference

- [Paramiko](http://www.paramiko.org/)
- [Paramiko GitHub](https://github.com/paramiko/paramiko)
- [Paramiko Documentation](http://docs.paramiko.org/en/stable/)
