import asyncio
import json
import asyncio
import aiohttp

from concurrentCache.body import Body

class ConcurrentCache:
    def __init__(self) -> None:
        self.responses = []
        self.ids = set()
        self.url = 'https://execrisk.services.dev.binaryedge.io/trigger'
        self.header = {'X-Token': '', 'Content-Type': 'application/json'} 
        self.body = Body() 

    async def create_session(self):
        print("Creating Session...")
        self.session = aiohttp.ClientSession(headers=self.header)       
        print("Session Created...")
        
    async def request(self, body):
        async with self.session.post(self.url, json = body) as response:
            self.responses.append(await response.text())
        
    def process_responses(self):
        for response in self.responses:
            r_json = json.loads(response)
            self.ids.add(r_json["process_id"])
            
    def get_ids(self):
        print("===PROCESS IDS===\n")
        print(self.ids)
        print("===\nEND PROCESS IDS===\n")


    async def main(self):
        await self.create_session()
        await asyncio.gather(self.request(self.body.one), self.request(self.body.one), self.request(self.body.one), self.request(self.body.one), self.request(self.body.one),
                              self.request(self.body.one), self.request(self.body.one), self.request(self.body.two), self.request(self.body.two), self.request(self.body.two), 
                              self.request(self.body.two), self.request(self.body.two), self.request(self.body.tree), self.request(self.body.four), self.request(self.body.four), 
                              self.request(self.body.four), self.request(self.body.four))
        self.process_responses()
        self.get_ids()
 

t = ConcurrentCache()

asyncio.run(t.main())


