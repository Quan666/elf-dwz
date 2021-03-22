import httpx
import config
async def check_url_safely(url:str)->bool:
    if len(config.check_url_safely_api)<=0:
        return True
    async with httpx.AsyncClient(proxies={}) as client:
        try:
            res = await client.get(config.check_url_safely_api+url)
            res = res.json()
            if res['code']==200:
                if res['data']['level']==3:
                    return False
            return True
        except Exception as e:
            print('检查链接安全出错：{}'.format(e))
            return True
