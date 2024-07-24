#!/usr/bin/python3.8
""" doc doc doc """
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """doc doc doc"""

    def __init__(self):
        """doc doc doc"""
        super().__init__()

    def put(self, key, item):
        """doc doc doc"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = list(self.cache_data.keys())[-1]
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """doc doc doc"""
        return self.cache_data.get(key)
