---
title: How to backup mysql and redis
date: 2025-01-20 10:00:00
tags: [mysql, redis, backup, shell, bash]
categories: [Database]
description: How to backup mysql and redis, and how to restore them.
lang: en
sitemap: true
comments: true
cover: /images/en/2025/01/How-to-backup-mysql-and-redis-cover.jpg
---

![How to backup mysql and redis](/images/en/2025/01/How-to-backup-mysql-and-redis-cover.jpg)

# Introduction

In this article, we will learn how to backup and restore MySQL and Redis databases using shell scripts. We will create two shell scripts: one for backing up the databases and another for restoring them.

# About MySQL

MySQL is an open-source relational database management system (RDBMS). It is a central component of the LAMP open-source web application software stack.

# About Redis

Redis is an open-source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker.

# Backup MySQL And Redis Shell

```shell
#!/bin/bash

#Variables
BACKUP_DIR="/www/wwwroot/backup"
DB_NAME="db"
DB_USER="root"
DB_PASSWORD="password"
DATE=$(date +%F)

REDIS_HOST="127.0.0.1"
REDIS_PORT="6379"
REDIS_PASSWORD=""
REDIS_DBS=("12" "13" "14")
REDIS_CLI_PATH="/usr/bin/redis-cli"


# backup mysql
# Dump the MySQL database and compress it
mysqldump -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" | gzip > "$BACKUP_DIR/$DB_NAME-$DATE.sql.gz"

# Check if the backup was successful
if [ $? -eq 0 ]; then
    echo "MySQL backup successful: $BACKUP_DIR/$DB_NAME-$DATE.sql.gz"
else
    echo "MySQL backup failed"
fi

# backup redis for redis db 0

# Check if the Redis CLI exists
if [ ! -f "$REDIS_CLI_PATH" ]; then
    echo "Redis CLI not found at $REDIS_CLI_PATH"
    exit 1
fi

for REDIS_DB in "${REDIS_DBS[@]}"; do
    REDIS_DUMP_FILE="$BACKUP_DIR/redis-dump-$REDIS_DB-$DATE.rdb"

    # Save the Redis database to a dump file
    $REDIS_CLI_PATH -h $REDIS_HOST -p $REDIS_PORT -n $REDIS_DB --rdb $REDIS_DUMP_FILE

    # Check if the dump was successful
    if [ $? -eq 0 ]; then
        echo "Redis backup successful: $REDIS_DUMP_FILE"
    else
        echo "Redis backup failed"
    fi
done
```

# Restore MySQL And Redis Shell

```shell
#!/bin/bash

#Variables
BACKUP_DIR="/www/wwwroot/backup"
DB_NAME="db"
DB_PASSWORD="password"
DATE="2025-01-20"

REDIS_HOST="127.0.0.1"
REDIS_PORT="6379"
REDIS_PASSWORD=""
REDIS_DBS=("12" "13" "14")
REDIS_CLI_PATH="/usr/bin/redis-cli"

# restore mysql
# Decompress the MySQL backup and import it
gunzip < "$BACKUP_DIR/$DB_NAME-$DATE.sql.gz" | mysql -u root -p"$DB_PASSWORD" "$DB_NAME"

# Check if the restore was successful
if [ $? -eq 0 ]; then
    echo "MySQL restore successful"
else
    echo "MySQL restore failed"
fi

# restore redis for redis db 0

# Check if the Redis CLI exists
if [ ! -f "$REDIS_CLI_PATH" ]; then
    echo "Redis CLI not found at $REDIS_CLI_PATH"
    exit 1
fi

for REDIS_DB in "${REDIS_DBS[@]}"; do
    REDIS_DUMP_FILE="$BACKUP_DIR/redis-dump-$REDIS_DB-$DATE.rdb"

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

# Conclusion

In this article, we have learned how to backup and restore MySQL and Redis databases using shell scripts. These scripts can be scheduled to run automatically at regular intervals to ensure that your data is safe and secure.

If you have any questions or feedback, please feel free to leave a comment below.
