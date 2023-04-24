import redis


rediscli = redis.StrictRedis(
    host='redis',
    port=6379,
    db=0,
)
