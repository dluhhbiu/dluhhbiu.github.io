#!/usr/bin/env python

'''
tag_generator.py

Copyright 2017 Long Qian
Contact: lqian8@jhu.edu

This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os
import re

post_dir = '_posts/'
tag_dir = 'tag/'
pattern = re.compile('[A-z]+:')

filenames = glob.glob(post_dir + '*md')

total_tags = []
for filename in filenames:
    f = open(filename, 'r', encoding="utf8")
    crawl = False
    for line in f:
        if crawl and (line.strip() == '---' or pattern.match(line.strip())):
            crawl = False
            break
        if crawl:
            tag = line.strip().split('- ')[1]
            total_tags.append(tag)
        if line.strip() == 'tags:':
            crawl = True
    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())
