import sqlalchemy as db

db_user = 'swider'
db_pwd = 'daswid'
db_host = 'localhost'
db_port = 49156
db_name = 'classicmodels'

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

engine = db.create_engine(connection_str)
connection = engine.connect()