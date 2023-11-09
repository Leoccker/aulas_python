import mysql.connector

def getConexao():
  con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ei4"
  )
  return con
print(getConexao())
