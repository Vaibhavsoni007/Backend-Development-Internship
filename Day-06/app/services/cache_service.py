import time


class CacheService:

    cache = {}

    @classmethod
    def get(cls, key):

        data = cls.cache.get(key)

        if not data:
            return None

        value, expiry = data


        if time.time() > expiry:

            del cls.cache[key]

            return None


        return value


    @classmethod
    def set(cls, key, value, ttl=60):

        cls.cache[key] = (
            value,
            time.time() + ttl
        )


    @classmethod
    def delete(cls, key):

        if key in cls.cache:

            del cls.cache[key]