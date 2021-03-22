import re
from urllib.parse import unquote, quote


from starlette.requests import Request
from starlette.templating import Jinja2Templates

import config
from util import response_code
from util.Redirect import Redirect
from util.check_url_safely import check_url_safely
from util.url_redis import inster_url, select_url, get_flag
import uvicorn
from fastapi import FastAPI


from util.url_redis import inster_url

app = FastAPI()
tmp = Jinja2Templates(directory='templates')


@app.get("/")
async def read_item(request: Request):
    flag = int(await get_flag())
    return tmp.TemplateResponse('index.html', {
        'request': request,  # 一定要返回request
        'url_num': flag-config.flag  # 当前短链数量
    })


@app.get("/{short_code}")
async def read_root(short_code: str):
    url = await select_url(short_code=short_code)
    if url:
        url = unquote(url, 'utf-8')
    else:
        url = config.server_address
    return Redirect(url=url)



@app.get("/api/insert")
async def read_item(url: str=config.server_address):
    url = unquote(url, 'utf-8')
    if not await check_url_safely(url=url):
        return response_code.resp_400(data=None, message='该网站存在风险！')
    if len(url) <= 3:
        return response_code.resp_400(data=None, message='请输入正确的网址！')
    else:
        if not re.search('[a-zA-Z]+://', url):
            url = f'http://{url}'
        short_code = await inster_url(url=url)
        if short_code:
            return response_code.resp_200(data={'url': f'{config.server_address}/{short_code}'})
        else:
            return response_code.resp_400(data=None, message='请输入正确的网址！')


# @app.get("/api/test", include_in_schema=False)
# async def read_item(flag: int):
#     return {encode(flag)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
