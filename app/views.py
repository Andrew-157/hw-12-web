from aiohttp import web
from db import Link
from agregation import run_agregations
import asyncio
from agregation import results


async def agregator(request):

    url_1 = 'https://www.investopedia.com/terms/c/capitalism.asp'
    url_2 = 'https://www.imf.org/external/pubs/ft/fandd/2015/06/basics.htm'

    links = [Link(link=url_1), Link(link=url_2)]

    request.app['db_session'].add_all(links)
    request.app['db_session'].commit()

    return web.Response(text=f"""
                        <p>Result 1: {results[0]}</p>
                        <p>Result 2: {results[1]}</p>
                        """)
