import sqlite3

# python 中三个引号用来输入多行数据
# sqlite 是大小写敏感的数据库

query="""
CREATE TABLE tbl_test
(id INTEGER PRIMARY KEY NOT NULL,
name VARCHAR(32),
age INTEGER);
"""

conn=sqlite3.connect(':memory:')
conn.execute(query)
conn.commit()


data=[(1,'cc',23),
      (2,'dd',11),
      (3,'ee',18)]

stmt = "INSERT INTO tbl_test VALUES(?,?,?)"

conn.executemany(stmt,data)
conn.commit()

cursor = conn.execute("select * from tbl_test")
rows = cursor.fetchall()
print('rows:')
print(rows)
print(' -- --- -- -\n')

print(cursor.description)
print(' -- --- -- -\n')

conn.close()



