from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.weiboinfo import Base, WeiboInfo

engine = create_engine('sqlite:///dashboard.db', echo=True)
Session = sessionmaker(bind=engine)

session = Session()

if not engine.dialect.has_table(engine, WeiboInfo.__tablename__):
    print 'creating table weiboinfo...'
    Base.metadata.tables[WeiboInfo.__tablename__].create(bind=engine)