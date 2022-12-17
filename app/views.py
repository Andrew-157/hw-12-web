from agregation import run_agregations
import aiohttp_jinja2


@aiohttp_jinja2.template('results.html')
async def agregator(request):

    url_1 = 'https://www.investopedia.com/terms/c/capitalism.asp'
    url_2 = 'https://www.imf.org/external/pubs/ft/fandd/2015/06/basics.htm'

    results = await run_agregations(url_1, url_2)

    return {'results': results}
