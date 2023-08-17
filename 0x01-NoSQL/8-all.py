#!/usr/bin/env python3
"""Function that lists all documents in a collection"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """Finds list of documents
    """
    doc = list(mongo_collection.find({}))
    return doc
