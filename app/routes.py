from aiohttp.web import Application
from views import agregator


def setup_routes(app: Application):

    app.router.add_get('/agregator', agregator)
