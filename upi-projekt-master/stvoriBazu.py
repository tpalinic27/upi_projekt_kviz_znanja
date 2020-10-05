import sqlite3 as lite
import sys

con=lite.connect('baza\\kviz3.db')

print ("Creating database/tables...")
with con:
    cur =con.cursor()
    #DROP TABLE
    cur.execute("DROP TABLE IF EXISTS kviz3")
    
    #CREATE TABLE admin
    cur.execute("CREATE TABLE IF NOT EXISTS admin (id INTEGER PRIMARY KEY AUTOINCREMENT, ime TEXT,sifra TEXT)")
    cur.execute('INSERT INTO admin VALUES(null,?,?)',('admin','admin'))
    con.commit()

    #CREATE TABLE pitanja
    cur.execute("CREATE TABLE IF NOT EXISTS pitanja (id INTEGER PRIMARY KEY AUTOINCREMENT, broj INTEGER, pitanje TEXT,odgovorA TEXT,odgovorB TEXT,odgovorC TEXT,odgovorD TEXT,tocanOdg TEXT)")
    
    #CREATE TABLE korisnik
    cur.execute("CREATE TABLE IF NOT EXISTS korisnik (id INTEGER PRIMARY KEY AUTOINCREMENT, ime TEXT, bodovi INTEGER)")

con.close()
print ("Database/tables created.")


