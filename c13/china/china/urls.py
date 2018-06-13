#!/usr/bin/env python
# coding=utf-8

def china(start, end):
    for page in range(start, end+1):
        yield 'http://tech.china.com/articles/index_{}.html'.format(page)

