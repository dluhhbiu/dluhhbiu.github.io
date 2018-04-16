---
layout: post
title: How to send email from the server and not get into spam
date: 2018-04-14 21:26:18 +0300
comments: true
tags: 
 - ubuntu 
 - postfix 
 - DKIM
 - gmail
---

### What I want
 - Sending emails from the server
 - Pass spam filters
 - Free sending
 - Sending only (without receiving emails)

### Installing postfix
```bash
apt update
apt install mailutils -y
```
Select `Internet Site`. And write your domain in next step. For example, I will use `example.com`

### SPF
Create txt record
```
v=spf1 include:_spf.google.com ip4:IP_SERVER ~all
```

### DKIM
```bash
apt install opendkim opendkim-tools
mkdir /etc/postfix/dkim/
# Generate key for server
opendkim-genkey -D /etc/postfix/dkim/ -d example.com -s mail
```
Folder `/etc/postfix/dkim/` will have 2 files `mail.private` and `mail.txt` (private and public keys)

We must change permission to private key
```bash
# Set permission
chmod 600 /etc/postfix/dkim/mail.private
# Change folder owner
chown -R opendkim /etc/postfix/dkim/
```
Edit file `/etc/opendkim.conf` to look like this:
```bash
Syslog yes
Domain *
Selector mail
Socket inet:8891@localhost  
Mode sv
# Set list of keys
KeyTable file:/etc/postfix/dkim/keytable
# Match keys and domains
SigningTable file:/etc/postfix/dkim/signingtable
```
File `/etc/postfix/dkim/keytable` must has information about private key:
```bash
# key_name domain:selector:/path/to/ley
mail._domainkey.example.com example.com:mail:/etc/postfix/dkim/mail.private
```
File `/etc/postfix/dkim/signingtable` has list of domains what need to sign:
```bash
# domain key_name
example.com mail._domainkey.example.com
```
File `/etc/default/opendkim` must has rule about SOCKET, which will listen opendkim (other rules about SOCKET necessary remove):
```bash
SOCKET="inet:8891@localhost"
```
Little bit changes in Postfix config file `/etc/postfix/main.cf`:
```bash
# myhostname must has right value
myhostname = example.com
# This rule because we don't want receiving emails
mydestination = localhost
# Add in end file
milter_default_action = accept
milter_protocol = 2
smtpd_milters = inet:localhost:8891
non_smtpd_milters = inet:localhost:8891
```
You must sure what this file `/etc/mailname` look like this
```bash
example.com
```
Restarting postfix and opendkim:
```bash
service postfix restart
service opendkim restart
```

### DNS
Creating A record for subdomain
```bash
тип: A
имя: mail._domainkey
указатель: IP_SERVER
TTL: 300
```
Take data from `/etc/postfix/dkim/mail.txt` and creating another TXT record
```bash
тип: TXT
имя: mail._domainkey
указатель: v=DKIM1; k=rsa; p=MI*** 
TTL: 300
```
### Testing
We can check on DKIM work with utility `opendkim-testkey`
```bash
opendkim-testkey -d example.com -s mail -vvv
# Good result
opendkim-testkey: using default configfile /etc/opendkim.conf
opendkim-testkey: checking key 'mail._domainkey.example.com'
opendkim-testkey: key not secure
opendkim-testkey: key OK
```
Great! Your email server working now. But sometimes these actions are not enough. And your mail still catch into spam. This [site](https://www.mail-tester.com/){:target="_blank"} can helps you. 

Send email from your server to `mail-tester`. And fix errors which `mail-tester` find.
```bash
echo "Test Email message body" | mail -s "Email test subject" -aFrom:testemail@example.com besthopox@gmail.com
```

**When I writing the article, I used next materials:**
 - [https://wiki.debian.org/opendkim](https://wiki.debian.org/opendkim){:target="_blank"}
