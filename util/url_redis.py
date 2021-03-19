import redis
import config
from util.Base62 import encode

pool = redis.ConnectionPool(host=config.redis_ip, port=config.redis_p, db=config.redis_db)


async def inster_url(url: str) -> str:
    r = redis.Redis(connection_pool=pool)

    # 先判断链接在数据库没
    if r.hget(name='elfurl', key=url):
        return str(r.hget(name='elfurl', key=url), encoding="utf-8")

    # 先判断flag存在不存在
    flag = r.get(name='elfflag')
    if flag is None:
        r.set(name='elfflag', value=config.flag)
    else:
        r.incr(name='elfflag')
    flag = int(r.get(name='elfflag'))
    # 获取短链
    short_code = encode(flag)
    # 存入 短链-原链
    if not r.set(name=short_code, value=url):
        return None
    # 存入 原链-短链
    if not r.hset(name='elfurl', key=url, value=short_code):
        return None
    return short_code


async def select_url(short_code: str) -> str:
    r = redis.Redis(connection_pool=pool)
    url = r.get(name=short_code)
    if url is not None:
        return str(url, encoding="utf-8")
    else:
        return None


if __name__ == "__main__":
    print(inster_url('asssd'))
