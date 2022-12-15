import aiohttp
import bs4


async def source_1(session: aiohttp.ClientSession, source):

    async with session.get(source, ssl=False) as response:

        content = await response.text()
