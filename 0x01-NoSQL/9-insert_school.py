#!/usr/bin/env python3
"""Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """Insert_school
    Args:
        mongo_collection(collection)
        **kwargs(dicts)
    """
    insert = mongo_collection.insert_one(kwargs)
    return insert.inserted_id
