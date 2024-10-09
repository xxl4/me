---
title: How to reflog git had delete file
date: 2024-10-09 10:00:00
tags: [git, reflog]
categories: [Tools]
comments: true
sitemap:
  lastmod: 2024-10-09 10:00:00
    priority: 0.8
    changefreq: daily
description: How to reflog git had delete file
lang: en
---

Today i will show you how to reflog git restore file that you had delete.

## Step 1: Check reflog

```bash
git reflog
```

## Step 2: Find the commit that delete file

```bash
git show <commit>
```

## Step 3: Restore file

```bash
git checkout <commit> -- <file>
```

## Step 4: Commit file

```bash
git add <file>
git commit -m "Restore file"
```

## Step 5: Push file

```bash
git push
```

That's it. You had restore file that you had delete.
```

```bash
git reflog
```

```bash
git reset HEAD@{2} 
```


## Conclusion

Today i show you how to reflog git restore file that you had delete. Hope you enjoy it.

## Reference

- [Git reflog](https://git-scm.com/docs/git-reflog)
- [Git reset](https://git-scm.com/docs/git-reset)
- [Git checkout](https://git-scm.com/docs/git-checkout)
```

