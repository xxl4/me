---
title: How to Use Paramiko and Python to SSH into a Server
tags:
  - Python
  - Paramiko
  - SSH
  - Server
categories:
    - Programming
date: 2021-09-13 18:10:00
lang: en
sitemap: true
description: How to Use Paramiko and Python to SSH into a Server
comments: true
author: Steve Sun
---

In this article, I will show you how to use Paramiko and Python to SSH into a server. Paramiko is a Python library that provides a simple interface to SSH. It allows you to programmatically execute commands on a remote server over an encrypted connection.

## Install Paramiko

Before we can use Paramiko, we need to install it. You can install Paramiko using pip:

```bash
pip install paramiko
```

## SSH into a Server

To SSH into a server using Paramiko, you need to create an SSH client and connect to the server. Here's an example:

```python
import paramiko

# Create an SSH client
client = paramiko.SSHClient()

# Automatically add the server's host key
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the server

client.connect('hostname', username='username', password='password')

# Execute a command on the server

stdin, stdout, stderr = client.exec_command('ls -l')

# Print the output of the command

print(stdout.read().decode())

# Close the connection

client.close()
```
In this example, we create an SSH client using `paramiko.SSHClient()`. We then connect to the server using `client.connect()`, passing in the hostname, username, and password. We execute a command on the server using `client.exec_command()`, passing in the command we want to execute. We then print the output of the command using `stdout.read().decode()`. Finally, we close the connection using `client.close()`.


# How to batch execute commands on multiple servers

```python
import paramiko

def ssh_command(hostname, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    print(f"Output from {hostname}:")
    print(stdout.read().decode())
    client.close()

servers = [
    {
        'hostname': 'server1.example.com',
        'username': 'user1',
        'password': 'password1'
    },
    {
        'hostname': 'server2.example.com',
        'username': 'user2',
        'password': 'password2'
    }
]

command = 'ls -l'

for server in servers:
    ssh_command(server['hostname'], server['username'], server['password'], command)
```

In this example, we define a function `ssh_command()` that takes the hostname, username, password, and command as arguments. We create an SSH client, connect to the server, execute the command, and print the output. We then define a list of servers with their hostnames, usernames, and passwords. We loop through the list of servers and execute the command on each server.

## Conclusion

In this article, I showed you how to use Paramiko and Python to SSH into a server. Paramiko is a powerful library that allows you to interact with remote servers over an encrypted connection. I hope you found this article helpful. If you have any questions or comments, please let me know!

Happy coding! 🚀
```