#!/usr/bin/env python3
"""Module returns average score of students"""


def top_students(mongo_collection):
    """Computs students avg score"""
    alx = [
            {
                "$project":
                    {
                        "name": "$name",
                        "averageScore": {"$avg": "$topics.score"}
                    }
            },
            {
                "$sort":
                    {
                        "averageScore": -1
                    }
            }
        ]
    return mongo_collection.aggregate(alx)
