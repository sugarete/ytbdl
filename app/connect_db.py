from sqlite3 import connect
import datetime
def check(sql, params=""):
    with connect("database/ytdb.db") as con:
        cur = con.cursor()
        cur.execute(sql, params)
        con.commit()
        rows = cur.fetchone()
        print(rows)
        if rows is None:
            return True
        else:
            return False
        
def insert(sql, params=""):
    # print(params)
    with connect("database/ytdb.db") as con:
        cur = con.cursor()
        cur.execute(sql, params)
        con.commit()
        return cur.lastrowid
    
def write_history(sql, params=""):
    with connect("database/ytdb.db") as con:
        cur = con.cursor()
        cur.execute(sql, params)
        con.commit()
        return cur.lastrowid
    
def get_history(sql, params):
    with connect("database/ytdb.db") as con:
        cur = con.cursor()
        cur.execute(sql, params)
        rows = cur.fetchall()
        return rows
    
def get_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")