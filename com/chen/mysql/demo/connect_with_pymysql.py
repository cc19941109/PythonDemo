import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user="root", passwd="123456", db="mysql")

cur = conn.cursor()
cur.execute("use spring")

cur.execute("select * from user limit 100")

print(cur.fetchone())

cur.close()
conn.close()
