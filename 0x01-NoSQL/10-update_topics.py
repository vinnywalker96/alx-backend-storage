#!/usr/bin/env python3
"""Change School Topics"""


def update_topics(mongo_collection, name, topics):
    """Update school topics
    Args:
        mongo_collection(collection object):

        name(string) will be the school name to update

        topics (list of strings) will be the list of topics
    """
    filter = {"name": name}
    data = {
        "$set": {
            "topics": topics
            }
        }
    updated = mongo_collection.update_many(filter, data)
    return updated
