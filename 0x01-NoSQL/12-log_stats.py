#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    data_nginx = list(collection.find())
    method = {
            "GET": 0,
            "POST": 0,
            "PUT": 0,
            "PATCH": 0,
            "DELETE": 0,
            "path": 0
        }

    for logs in data_nginx:
        if logs['method'] == "GET":
            method['GET'] += 1
        if logs['method'] == "POST":
            method['POST'] += 1
        if logs['method'] == "PUT":
            method['PUT'] += 1
        if logs['method'] == "PATCH":
            method['PATCH'] += 1
        if logs['method'] == "DELETE":
            method['DELETE'] += 1
        if logs['path'] == '/status':
            method['path'] += 1
    print("Methods:")
    print(f"    method GET: {method['GET']}")
    print(f"    method POST: {method['POST']}")
    print(f"    method PUT: {method['PUT']}")
    print(f"    method PATCH: {method['PATCH']}")
    print(f"    method DELETE: {method['DELETE']}")
    print(f"{method['path']} status check") 
    client.close()
