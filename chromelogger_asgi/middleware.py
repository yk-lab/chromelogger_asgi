import chromelogger as console

class ChromeLoggerMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        headers = dict(scope["headers"])
        if scope["type"] in ("http"):
            header = console.get_header()
            if header is not None:
                headers.update(header)
        await self.app(scope, receive, send)
