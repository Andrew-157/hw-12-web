from sqlalchemy import MetaData, Column, Integer, String, Table


meta = MetaData()


link = Table(
    'links', meta,

    Column('id', Integer, primary_key=True),
    Column('link', String(150), nullable=False),
    Column('data', String(200), nullable=False)
)


async def pg_context(app):
    conf = app['conf']['postgres']
