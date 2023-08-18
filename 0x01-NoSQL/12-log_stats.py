#!/usr/bin/env python3
"""Nginx logs"""
from pymongo import MongoClient


def get_logs_stats(collection):
    """Return log stats

    Args:
        collection
    """
    number_of_logs = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    total_logs = {
            method: collection.count_documents(
                {
                    "method": method
                }) for method in methods}

    status_check = collection.count_documents(
        {
            "method": "GET",
            "path": "/status"
        })
    return (number_of_logs, total_logs, status_check)


def print_stats(number_of_logs, total_logs, status_check):
    """Print stats    
    Args:

        number_of_logs()

        total_logs()

        status_check()

    """
    print("Methods:")
    for method, count in total_logs.items():
        print(f"\t{method}: {count}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    with MongoClient('mongodb://127.0.0.1:27017') as client:
        db = client.logs.nginx
        number_of_logs, total_logs, status_check = get_logs_stats(db)
        print_stats(number_of_logs, total_logs, status_check)
