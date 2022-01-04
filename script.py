import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import sql

db_user = 'swider'
db_pwd = 'daswid'
db_host = 'localhost'
db_port = 49153
db_name = 'classicmodels'

connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
engine = db.create_engine(connection_str)
metadata_obj = db.MetaData(bind=engine)
with engine.connect() as conn:
	with conn.begin():
		# customers		= metadata_obj.tables['customers']
		# employees		= metadata_obj.tables['employees']
		# offices			= metadata_obj.tables['offices']
		# orderdetails	= metadata_obj.tables['orderdetails']
		# orders			= metadata_obj.tables['orders']
		# payments		= metadata_obj.tables['payments']
		# productlines	= metadata_obj.tables['productlines']

		# sel_off = select(offices)
		# print(conn.execute(sel_off))
		print(metadata_obj.tables)