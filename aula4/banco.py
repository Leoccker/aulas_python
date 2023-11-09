import mysql.connector

def getConexao():
  con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="estoque"
  )
  return con

print(getConexao())
