from aiohttp import web
from db import Link
import aiohttp


async def index(request):
    return web.Response(text="Hello AIOHTTP!")


async def agregator(request):

    source_1 = 'https://www.investopedia.com/terms/c/capitalism.asp'
    source_2 = 'https://www.imf.org/external/pubs/ft/fandd/2015/06/basics.htm'

    session = await aiohttp.ClientSession()
