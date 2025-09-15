import pymysql

conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='shopping_db2')
cur = conn.cursor()
cur.execute("select avg(age) from customer where address = 'gyunggi'")
rows = cur.fetchone()
print(int(rows[0]))
cur.close()
conn.commit()
conn.close()
