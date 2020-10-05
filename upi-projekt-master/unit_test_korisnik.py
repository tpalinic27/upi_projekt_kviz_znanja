import sys
import os
import unittest
from itertools import permutations
if __name__=='__main__':
    sys.path.append(os.path.abspath(".."))

class Korisnik(object):
    def _init_(nickname):
         Korisnik._nickname = nickname
         
    def nickname(self):
        return Korisnik._nickname
    
    def __str__(self):
        return ""

    
        nickname: {0}

        "".format(Korisnik._nickname)
        


if __name__=='__main__':
    unittest.main()
