---
title: How to copy Redis DB to remote Redis DB
date: 2025-01-22 10:00:00
tags: [redis, copy, shell, bash, redis-cli, python, ssh]
categories: [Database]
description: How to copy Redis DB to remote Redis DB using redis-cli and Python.
lang: en
sitemap: true
comments: true
cover: /images/en/2025/01/How-to-copy-Redis-DB-to-remote-Redis-DB-cover.jpg
---

![How to copy Redis DB to remote Redis DB](/images/en/2025/01/How-to-copy-Redis-DB-to-remote-Redis-DB-cover.jpg)

# Introduction

In this article, we will learn how to copy a Redis database to a remote Redis database using `redis-cli` and Python. We will create a Python script that dumps the local Redis database and sends it to the remote server using SSH. Then, we will create a shell script that imports the Redis dump into the remote Redis database.

# About Redis

Redis is an open-source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker.

# Copy Redis DB to Remote Redis DB

```python
import redis
from sshtunnel import SSHTunnelForwarder

# Source Redis connection details
SRC_REDIS_HOST = '127.0.0.1'
SRC_REDIS_PORT = 6379
SRC_REDIS_DB = 21
SRC_REDIS_PASSWORD = ''

# Target Redis connection details
TARGET_REDIS_HOST = '127.0.0.1'
TARGET_REDIS_PORT = 6379
TARGET_REDIS_DB = 50
TARGET_REDIS_PASSWORD = ''

# SSH proxy details
SSH_HOST = '1.1.1.1'
SSH_PORT = 22
SSH_USER = 'root'
SSH_KEY = '/root/.ssh/id_rsa'

# Create SSH tunnel
with SSHTunnelForwarder(
    (SSH_HOST, SSH_PORT),
    ssh_username=SSH_USER,
    ssh_pkey=SSH_KEY,
    remote_bind_address=(SRC_REDIS_HOST, SRC_REDIS_PORT)
) as tunnel:

    src_redis = redis.Redis(
        host='127.0.0.1',
        port=tunnel.local_bind_port,
        db=SRC_REDIS_DB,
        password=SRC_REDIS_PASSWORD
    )

    # Connect to target Redis
    target_redis = redis.Redis(
        host=TARGET_REDIS_HOST,
        port=TARGET_REDIS_PORT,
        db=TARGET_REDIS_DB,
        password=TARGET_REDIS_PASSWORD
    )

    # Function to copy data from source to target Redis
    def sync_redis(src, target):
        for key in src.keys():
            key_type = src.type(key)
            if key_type == b'string':
                value = src.get(key)
                target.set(key, value)
            elif key_type == b'hash':
                all_hash_data = src.hgetall(key)
                for k, v in all_hash_data.items():
                    target.hset(key, k, v)
            elif key_type == b'list':
                all_list_data = src.lrange(key, 0, -1)
                for item in all_list_data:
                    target.rpush(key, item)
            elif key_type == b'set':
                all_set_data = src.smembers(key)
                for item in all_set_data:
                    target.sadd(key, item)
            elif key_type == b'zset':
                all_zset_data = src.zrange(key, 0, -1, withscores=True)
                for item, score in all_zset_data:
                    target.zadd(key, {item: score})
            else:
                print(f"Unsupported key type {key_type} for key {key}")

    # Sync data from source to target
    sync_redis(src_redis, target_redis)
    print("Data sync complete.")
```

The Python script above connects to the source Redis database, creates an SSH tunnel to the remote server, and then connects to the target Redis database. It then copies the data from the source Redis to the target Redis using the `sync_redis` function.

Next, we will create a shell script to import the Redis dump into the remote Redis database.

```shell
#!/bin/bash

# Variables
BACKUP_DIR="/path/to/redis-dump"
REDIS_HOST="127.0.0.1"
REDIS_PORT="6379"
REDIS_PASSWORD=""
REDIS_DBS=("12" "13" "14")
REDIS_CLI_PATH="/usr/bin/redis-cli"

# Check if the Redis CLI exists

if [ ! -f "$REDIS_CLI_PATH" ]; then
    echo "Redis CLI not found at $REDIS_CLI_PATH"
    exit 1
fi

for REDIS_DB in "${REDIS_DBS[@]}"; do
    REDIS_DUMP_FILE="$BACKUP_DIR/redis-dump-$REDIS_DB.rdb"

    # Restore the Redis database from the dump file
    $REDIS_CLI_PATH -h $REDIS_HOST -p $REDIS_PORT -n $REDIS_DB --rdb $REDIS_DUMP_FILE

    # Check if the restore was successful
    if [ $? -eq 0 ]; then
        echo "Redis restore successful"
    else
        echo "Redis restore failed"
    fi
done
```

The shell script above restores the Redis database from the dump file for each database specified in the `REDIS_DBS` array.

You can run the Python script to copy the Redis database to the remote server and then run the shell script to import the Redis dump into the remote Redis database.

# Conclusion

In this article, we learned how to copy a Redis database to a remote Redis database using `redis-cli` and Python. We created a Python script that dumps the local Redis database and sends it to the remote server using SSH. We also created a shell script that imports the Redis dump into the remote Redis database.