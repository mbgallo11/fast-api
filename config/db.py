from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://ocsadmin@192.168.160.154:3306/python_test")

conn = engine.connect()