#!/usr/bin/env python
# coding=utf-8

from pymongo import MongoClient


try:
    client = MongoClient(host='localhost', port=27017)
    db = client.student
    collection = db.Student
    # generator
    datas = collection.find()[:3]
    for data in datas:
        print (data)
    # 插入数据 推荐使用insert_one, insert_many()
    # 查询 find({'name': 'xx'}, {})  第二个参数是显示的key，value
    # count()计数，统计查询结果
    # sort('field', pymongo.ASCEDING)
    # skip() 偏移几个结果, limit()限制结果的数量
    # update()修改 update({"name": "pp"}, {"$set": obj}), update_one()第二个参数只能是$set形式
    # remove(), delete_one(), delete_many({"age": {"$lt": 30}})
    # 
except Exception as e:
    print  (e)

