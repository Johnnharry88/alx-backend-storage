#!/usr/bin/env python3
"""Updates the school collection with attribute topics
"""

import pymongo



def update_topics(mongo_collection, name, topics):
    """Updates a document with specific attribute topic and value topics"""
    alx = mongo_collection.update_many({
            "name": name
        },
        {
            "$set": {
                "topics": topics
            }
        })
    return alx
