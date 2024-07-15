#!/usr/bin/env python3
"""Search School by Topic"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """Find the specific attr"""
    search = mongo_collection.find({"topics": {"$in": [topic]}})
    return search
