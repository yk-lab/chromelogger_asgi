class ChromeLoggerMiddleware:
    def __init__(self, app, console):
        self.app = app
        self.console = console

    async def __call__(self, scope, receive, send):
        headers = dict(scope["headers"])
        if scope["type"] in ("http"):
            header = console.get_header()
            if header is not None:
                headers.update(header)
        await self.app(receive, send)
