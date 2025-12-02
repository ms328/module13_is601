# app/auth/redis.py
try:
    from redis.asyncio import from_url as redis_from_url
    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False

from app.core.config import get_settings

settings = get_settings()

async def get_redis():
    if not REDIS_AVAILABLE:
        # Return a mock Redis object for testing without Redis
        return MockRedis()
    
    if not hasattr(get_redis, "redis"):
        get_redis.redis = await redis_from_url(
            settings.REDIS_URL or "redis://localhost"
        )
    return get_redis.redis

class MockRedis:
    """Mock Redis client for testing without Redis server"""
    def __init__(self):
        self.data = {}
    
    async def set(self, key: str, value: str, ex: int = None):
        self.data[key] = value
    
    async def exists(self, key: str) -> bool:
        return key in self.data
    
    async def get(self, key: str):
        return self.data.get(key)

async def add_to_blacklist(jti: str, exp: int):
    """Add a token's JTI to the blacklist"""
    redis = await get_redis()
    await redis.set(f"blacklist:{jti}", "1", ex=exp)

async def is_blacklisted(jti: str) -> bool:
    """Check if a token's JTI is blacklisted"""
    redis = await get_redis()
    return await redis.exists(f"blacklist:{jti}")