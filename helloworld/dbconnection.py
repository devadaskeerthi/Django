import pymysql

con=pymysql.connect(user="root",password="",host="localhost",database="hello_db")

def insert(qry):
    cursor=con.cursor()
    cursor.execute(qry)
    con.commit()

def selectone(qry):
    cursor=con.cursor()
    cursor.execute(qry)
    d=cursor.fetchone()
    return d

def update(qry):
    cursor=con.cursor()
    cursor.execute(qry)
    con.commit()

def selectall(qry):
    cursor=con.cursor()
    cursor.execute(qry)
    d=cursor.fetchall()
    return d