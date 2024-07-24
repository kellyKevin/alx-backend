#!/usr/bin/python3.8
""" doc doc doc """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """doc doc doc"""

    def put(self, key, item):
        """doc doc doc"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """doc doc doc"""
        return self.cache_data.get(key)
