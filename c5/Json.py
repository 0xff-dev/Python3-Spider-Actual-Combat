#!/usr/bin/env python
# coding=utf-8

import json
import csv


data = [{
    'name': '小胖',
    'gender': '男',
    'birthday': '1999-10-10',
}]


# test json
with open('./data.json', 'w', encoding='utf-8') as fp:
    # ensure_acs_ii=False, 设置文件的中文正常显示
    fp.write(json.dumps(data, indent=2, ensure_ascii=False))


# test csv
#list witer
with open('./list_write.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    # writerows()写入多行
    writer.writerow(['id', 'name', 'score'])
    writer.writerow(['1001', 'kb', '99'])
    writer.writerow(['1002', 'www', '90'])
    writer.writerow(['1003', 'pp', '56'])
    writer.writerows([['1004', 'mm', '60'], ['1005', 'nn', '70']])

with open('./list_write.csv', 'r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print (row)


# dict write
with open('./dict_write.csv', 'w') as csvfile:
    fields = ['name', 'age', 'likes']
    writer = csv.DictWriter(csvfile, fieldnames=fields, delimiter=' ')
    writer.writeheader()
    writer.writerow({'name': 'zhu', 'age': '12', 'likes':'屎'})
    writer.writerow({'name': 'dog', 'age': '11', 'likes': '屎'})
    writer.writerows([{'name': 'aa', 'age': '11', 'likes': 'assa'}, {'name': 'qqq', 'age': '2', 'likes': 'aaa'}])

with open('./dict_write.csv', 'r') as fp:
    fields = ['name', 'age', 'likes']
    reader = csv.DictReader(fp)
    for row in reader:
        print (row)

