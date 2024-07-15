#!/usr/bin/env python3
"""Insets documents in Mongd database my_db
collection school using pymongo"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """Inserts document sin a Mongo collectio"""
    alx = mongo_collection.insert_one(kwargs)

    return alx.inserted_id
