import sys
import os
import unittest
from itertools import permutations
if __name__=='__main__':
    sys.path.append(os.path.abspath(".."))

class Admin(object):
    def _init_(username,password):
         User._username = username
         User._password = password
         
    def username(self):
        return Admin._username

    
    def password(self):
        return Admin._password
    
    def __str__(self):
        return ""

    
        username: {0}
        password: {1}

        "".format(Admin._username,Admin._password)
        


if __name__=='__main__':
    unittest.main()

