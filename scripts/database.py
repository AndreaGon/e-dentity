from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, insert, select, BigInteger, Sequence, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid
meta = MetaData()
engine = create_engine('cockroachdb://andrea:BZcmfUSQMpJGehPF@free-tier6.gcp-asia-southeast1.cockroachlabs.cloud:26257/defaultdb?sslmode=require&options=--cluster=noted-lion-88')
meta.drop_all(engine)

#Create registration table
users = Table(
  'user_table', meta,
  Column('user_uuid', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
  Column('fullname', String),
  Column('phonenumber', String),
  Column('email', String),
  Column('dateofbirth', String),
  Column('address', String),
  Column('password', String)
)

meta.create_all(engine)
conn = engine.connect()

def showData(tablename, currentId, idColumn = "id"):
  result = conn.execute("SELECT * FROM " + tablename + " WHERE user_uuid = '" + currentId + "'")
  return result

def addData(tablename, data):
  conn.execute("INSERT INTO " + tablename + " VALUES " + data)
  
def addImageData(id, data):
  conn.execute(identification.insert(), {'user_uuid' : id, 'verification_img' : data})
  
def getPassword(email):
  result = conn.execute("SELECT password FROM user_table WHERE email = '" + email + "'")
  return result
