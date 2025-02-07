from aiohttp import web

class Server:
    def __init__(self, host : str  = "localhost", port : int = 5000):
        self.host = host
	self.port = port

    async def run(self):
	web.
