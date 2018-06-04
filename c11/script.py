#!/usr/bin/env python
# coding=utf-8

import json
from pymongo import MongoClient
from mitmproxy import ctx


DB_HOST = 'localhost'
DB_PORT = 27017

client = MongoClient(DB_HOST, DB_PORT)
db = client.dedaobooks
collection = db.books


def reqponse(flow):
    global collection
    url = 'https://dedao.igetget.com/v3/discover/booklist'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        books = data.get('c').get('list')
        for book in books:
            data = {
                'title': book.get('operating_title'),
                'cover': book.get('cover'),
                'summary': book.get('summary'),
                'price': book.get('price'),
            }
        ctx.log.info(str(data))
        collection.insert_one(data)

