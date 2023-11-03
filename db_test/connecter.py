import sqlite3
from sqlite3 import Error

def create_basic_table(ladb):
    conn = get_connection(ladb)
    cur = conn.cursor()
    cur.execute("CREATE TABLE movie(title, year, score)")
    res = cur.execute("SELECT name FROM sqlite_master")
    print(res.fetchone())
    if conn:
        conn.close()

def insert(ladb):
    conn = get_connection(ladb)
    if conn:
        cur = conn.cursor()
        insertstmt= "INSERT INTO movie VALUES\
          ('Monty Python and the Holy Grail', 1975, 8.2),\
          ('And Now for Something Completely Different', 1971, 7.5);" # Le point virgule !!!
        print(insertstmt)
        cur.execute(insertstmt)
        print ("post insert")
        conn.commit()
        conn.close()


def show_table_vals(ladb, latable):
    conn = get_connection(ladb)
    if conn:
        cur = conn.cursor()
        stringselect = ("select * from %s"  %latable)
        print(stringselect)
        res = cur.execute(stringselect)
        fradon = cur.fetchall()
       # print(len(fradon))
        conn.close()
        return fradon

def get_connection(dbname):
    conn = None
    try:
        conn = sqlite3.connect(dbname)
        if conn:
            print("ok connecté")
            return conn
    except Error as e:
        print(e)


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("connection ...")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            print("déconnecte")


if __name__ == '__main__':
    #create_connection(r"jktest1.db")
    #create_basic_table(r"jktest1.db")
    insert(r"jktest1.db")
    momo = show_table_vals(r"jktest1.db",r"movie")

    for row in momo:
        print (row)
