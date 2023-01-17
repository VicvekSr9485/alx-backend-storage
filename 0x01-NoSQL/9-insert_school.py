#!/usr/bin/env python3
""" Insert a document in Python module """


def insert_school(mongo_collection, **kwargs):
    """ Python function that inserts a new document in a collection based on kwargs
    """
    doc_col = mongo_collection.insert_one(kwargs)
    return doc_col.inserted_id
