import pymysql

conn = pymysql.connect(host='localhost', user='somonox', password='hohomerryx-mas', db='study_1')
cur = conn.cursor()

def add_status(status):
    cur.execute("insert into LED(status) values('{0}')".format(status))
    conn.commit()