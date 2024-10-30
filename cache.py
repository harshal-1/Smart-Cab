# cache.py
import redis

cache = redis.StrictRedis(host='localhost', port=6379, db=0)

def cache_cab_location(cab_id, location):
    cache.set(cab_id, location)

def get_cached_cab_location(cab_id):
    return cache.get(cab_id)
