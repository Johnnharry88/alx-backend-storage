#!/usr/bin/env python3
"""Mddule that provides stats about the logs that occured in Nginx
stored in Mongo database"""

from pymongo import MongoClient

hold_x = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, opt=None):
    """Provides statistics for logs on Niginx"""
    xty = {}
    if opt:
        value = mongo_collection.count_documents(
                {"method": {"$regex": opt}})
        print(f"\tmethod {opt}: {value}")
        return

    res = mongo_collection.count_documents(xty)
    print(f"{res} logs")
    print("Methods:")
    for m in hold_x:
        log_stats(nginx_collection, m)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
