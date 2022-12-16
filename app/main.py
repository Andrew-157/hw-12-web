from aiohttp import web

from settings import config
from routes import setup_routes
from db import pg_context
import aiohttp_jinja2
import jinja2
from settings import BASE_DIR


app = web.Application()
app['config'] = config
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(
    'D:\\hws-web\\hw-12\\app\\templates'))
setup_routes(app)
app.cleanup_ctx.append(pg_context)
web.run_app(app)
