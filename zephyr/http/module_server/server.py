from aiohttp import web, web_exceptions
import asyncio
import signal
class Server:
    def __init__(self, host : str  = "localhost", port : int = 5000):
        self.host = host
        self.port = port
        self.app = web.Application()
        self.shutdown_event = asyncio.Event()

    async def run(self):
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner,self.host, self.port)
        await site.start()

    def handdle_shutdown(self):
        self.shutdown_event.set()

    async def start(self):
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGTERM, signal.SIGINT):
            loop.add_signal_handler(sig, self.handdle_shutdown)
        try:
            self.run()
            await self.shutdown_event.wait()
        except web_exceptions as e:
            raise web_exceptions(e)




        
       
