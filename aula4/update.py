import mysql.connector
import banco

con = banco.getConexao()
cursor = con.cursor()

sql = "update cliente set nome_cliente = 'Dionatan T' where nome_cliente = 'Dionatan'"
cursor.execute(sql)
con.commit()

print(cursor.rowcount, "registro(s) afetados(s)")

con.close