from urllib.parse import quote

from starlette.responses import Response
import typing

from starlette.background import BackgroundTask
from starlette.datastructures import URL

# 自己实现跳转
class Redirect(Response):
    def __init__(
            self,
            url: typing.Union[str, URL],
            status_code: int = 307,
            headers: dict = None,
            background: BackgroundTask = None,
    ) -> None:
        super().__init__(
            content=b"", status_code=status_code, headers=headers, background=background
        )
        self.headers["location"] = quote(str(url), safe=":/%#?&=@[]!$&'()*+,;")
