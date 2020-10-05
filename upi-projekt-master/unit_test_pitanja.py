import unittest
import os, sys, sqlite3, datetime

from baza_metode import newQuestion
dirname = os.path.dirname(sys.argv[0])

from unit_test_korisnik import Korisnik

class TestStringMethods(unittest.TestCase):
            
    def test_init_newQuestion(self):
        newQuestion(1,"Pitanje","OdgA","OdgB","OdgC","OdgD","TocOdg")
        con=sqlite3.connect('baza\\kviz3.db')
        cur=con.cursor()

        idd=cur.execute('SELECT * FROM sqlite_sequence').fetchall()
        print("Ovo je idd")
        print(idd)
        seq=idd[1][1]
        print("ovo je seq:")
        print(seq)
        row=cur.execute('SELECT * FROM pitanja WHERE id=(?)',(seq,)).fetchone()
        self.assertEqual(row,(seq,1,"Pitanje","OdgA","OdgB","OdgC","OdgD","TocOdg"))
        podaci=(seq,"1",)
        print("Ovo je rezultat:")
        print(row)
        print("Ovo je unos:")
        print(podaci)
        con=sqlite3.connect('baza\\kviz3.db')
        cur=con.cursor()
        cur.execute('DELETE FROM pitanja WHERE id=?',(seq,))
        con.commit()
   

if __name__ == '__main__':
    unittest.main()
