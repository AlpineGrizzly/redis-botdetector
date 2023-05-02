# Will create bots to connect to Redis database

import redis

r = redis.Redis(db=5)

# Add some normal looking addresses
r.lpush("ips", "51.218.112.236")
r.lpush("ips", "90.213.45.98")
r.lpush("ips", "115.215.230.176")
r.lpush("ips", "51.218.112.236")

# Our bot who wants those new PS5s
for _ in range(20):
    r.lpush("ips", "104.174.118.18")
