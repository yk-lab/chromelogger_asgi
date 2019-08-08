import logging

import chromelogger as console

logger = logging.getLogger()


class ChromeLoggerMiddleware:
    def __init__(self, app):
        logger.debug("ChromeLoggerMiddleware __init__")
        logger.debug(f"app type is {type(app)}")
        self.app = app

    async def __call__(self, scope, receive, send):
        logger.debug("ChromeLoggerMiddleware __call__")
        logger.debug(f"scope is {scope}, type: {type(scope)}")
        headers = dict(scope["headers"])
        logger.debug(f"headers is {headers}")
        if scope["type"] in ("http"):
            header = console.get_header()
            logger.debug(f"console header is {header}")
            if header is not None:
                headers.update(header)
                logger.debug(f"updated headers")
        await self.app(scope, receive, send)
