from sqlalchemy import MetaData, Column, Integer, String, Table
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Link(Base):

    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    link = Column(String(150), nullable=False)
    agregated_data = Column(String(200), nullable=False)


async def pg_context(app):

    conf = app['config']['postgres']
    url_db = f"postgresql://{conf['user']}:{conf['password']}@{conf['host']}/{conf['database']}"
    DBSession = sessionmaker(bind=create_engine(url_db))
    session = DBSession()
    app['db_session'] = session

    yield

    app['db_session'].close()
