import aiohttp
import asyncio
from bs4 import BeautifulSoup


async def source_1(session: aiohttp.ClientSession, url):

    async with session.get(url, ssl=False) as response:

        content = await response.text()

        soup = BeautifulSoup(content, "html.parser")

        soup_content = soup.find_all('p')[2]

        start_index = str(soup_content).find('>')

        finish_index = str(soup_content)[1:].find('<')

        result = str(soup_content)[start_index+1: finish_index-1]

        return result


async def source_2(session: aiohttp.ClientSession, url):

    async with session.get(url, ssl=False) as response:

        content = await response.text()

        soup = BeautifulSoup(content, "html.parser")

        soup_content = soup.find_all('p')[4]

        start_index = str(soup_content).find('>')

        finish_index = str(soup_content)[1:].find('<')

        result = str(soup_content)[start_index+1: finish_index+1]

        return result


async def run_agregations(url_1, url_2):

    async with aiohttp.ClientSession() as session:

        agregation_1 = asyncio.create_task(source_1(session, url_1))
        agregation_2 = asyncio.create_task(source_2(session, url_2))

        result_1 = await agregation_1
        result_2 = await agregation_2

    return result_1, result_2

url_1 = 'https://www.investopedia.com/terms/c/capitalism.asp'
url_2 = 'https://www.imf.org/external/pubs/ft/fandd/2015/06/basics.htm'

results = asyncio.run(run_agregations(url_1, url_2))
