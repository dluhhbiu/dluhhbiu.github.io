---
layout: post
title: How to solve problem with PostgreSQL which is not running on Mac
date: 2019-11-18 16:08:14 +0300
comments: true
tags: 
 - macos 
 - postgresql 
---

Sometimes you can get an error related to PostgreSQL. When you try to connect to Postgres from you app or through psql. I got it only when working on mac os.

```bash
psql: could not connect to server: No such file or directory. Is the server running locally and accepting connections on Unix domain socket "/tmp/.s.PGSQL.5432"?
```

There are several reasons for getting this error and several solutions to solve it:
1) Just try to restart it:
```bash
$ brew services restart postgresql
```
2) If a process crashed and pid file was not destroyed:
```bash
$ brew services stop postgresql
$ rm /usr/local/var/postgres/postmaster.pid # adjust path accordingly to your install
$ brew services start postgresql
```
3) If PostgreSQL is updated, but not enough correctly. DB has one version and the server has another:
```bash
$ brew postgresql-upgrade-database
$ brew services start postgresql
```
4) If something terrible happened then try to reinstall postgresql:
```bash
$ brew uninstall postgresql 
$ brew install postgresql 
$ brew postgresql-upgrade-database
```


**When writing the article, I used next materials:**
 - [https://dba.stackexchange.com](https://dba.stackexchange.com/questions/75214/postgresql-not-running-on-mac){:target="_blank"}
