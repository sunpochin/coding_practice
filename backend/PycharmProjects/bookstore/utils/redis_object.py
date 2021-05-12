import aioredis
from utils.const import *

redis = None


async def check_test_redis():
    global redis
    if TESTING:
        redis = aioredis.create_redis_pool(TEST_REDIS_URL)
