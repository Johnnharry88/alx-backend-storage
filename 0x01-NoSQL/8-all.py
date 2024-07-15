#!/usr/bin/env python3
""" A functio that accepts mong collections nad 
Lsit all documents in it 
"""

import pymongo


def list_all(mongo_collection):
    """Lsts out all document in Mongo my_db"""
    if mongo_collection is not None:
        alx = mongo_collection.find()
        return [ a for a in alx]
    else:
        return []
#    alx = mongo_collection.find()
#    return [a for a in alx]
