import aiohttp


def create_session():

    session = aiohttp.ClientSession()

    return session
