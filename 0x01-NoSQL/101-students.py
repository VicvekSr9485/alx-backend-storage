#!/usr/bin/env python3
""" Top students """


def top_students(mongo_collection):
    """ Python function that returns all students sorted by average score
    """
    return db.mongo_collection.aggregate([{"$score": {averageScore: {"$avg": "score"},
                                            {"$sort": {averageScore: -1}}}}])
