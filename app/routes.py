from aiohttp.web import Application
from views import index


def setup_routes(app: Application):
    app.router.add_get('/agregator', index)
