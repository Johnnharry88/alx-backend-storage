#!/usr/bin/env python3
"""Log statistics check with IPs"""
from pymongo import MongoClient


def do_nginx_stats():
    """Do statistics of nginx logs"""
    hook = MongoClient()
    nginx_check = hook.logs.nginx

    no_of_docs = nginx_check.count_documents({})
    print("{} logs".format(no_of_docs))
    print("Methods:")
    hold_x = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for h in hold_x:
        count_h = nginx_check.count_documents({"method": h})
        print(f"\tmethod {h}: {count_h}")
    stat = nginx_check.count_documents({"method": "GET", "path": "/status"})
    print(f"{stat} status check")

    print("IPs:")
    alx = [
            {"$group":
                {
                "_id": "$ip",
                "count": {"$sum": 1}
                }
            },
            {"$sort": {"count": -1}},
            {"$limit": 10},
            {"$project": {
                "_id": 0,
                "ip": "$_id",
                "count": 1
            }}
            ]
    alx_sort = nginx_check.aggregate(alx)
    for a in alx_sort:
        count = a.get("count")
        ip_address = a.get("ip")
        print("\t{}: {}".format(ip_address, count))

if __name__ == "__main__":
    do_nginx_stats()
