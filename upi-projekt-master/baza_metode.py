import sqlite3
import os, sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/entiteti/')

def newQuestion(save_id,question,aA,aB,aC,aD,ca):
    con=sqlite3.connect('baza\\kviz3.db')    
    try:
        cur=con.cursor()
        #DATABASE QUERY       
        cur.execute('INSERT INTO pitanja VALUES (null,?,?,?,?,?,?,?)',(save_id,question,aA,aB,aC,aD,ca))
        con.commit()
        
    except Exception as e:
        print("Error at newQuestion: ",e)
        con.rollback
    con.close()
