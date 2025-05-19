from django.conf import settings
from redis.asyncio import Redis

REDIS_URL = getattr(settings, "REDIS_URL", "redis://localhost:6379/0")


async def get_redis() -> Redis:
    return Redis.from_url(REDIS_URL, decode_responses=True)


async def add_user_to_room(room_id: int, username: str):
    redis = await get_redis()
    exists = await redis.sismember(f"room:{room_id}:users", username)
    if exists:
        raise ValueError(f"El usuario '{username}' ya está en la sala {room_id}.")
    await redis.sadd(f"room:{room_id}:users", username)


async def remove_user_from_room(room_id: int, username: str):
    redis = await get_redis()
    await redis.srem(f"room:{room_id}:users", username)


async def get_users_in_room(room_id: int):
    redis = await get_redis()
    return await redis.smembers(f"room:{room_id}:users")
