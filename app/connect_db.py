from sqlite3 import connect

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
    
