#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """Return list of schools

    Args:
        mongo_collection(mongo object)

        topic(string) will be topic searched

    """
    filter = list(mongo_collection.find({"topics": topic}))
    return filter
