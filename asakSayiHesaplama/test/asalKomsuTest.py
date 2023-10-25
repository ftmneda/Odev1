'''
Created on Oct 25, 2023

@author: neda
'''
import unittest
import prod.asalKomsu as ak


class Test(unittest.TestCase):


    def test010(self):
        sonuc = ak.asalKomsu(ustSınır=2)
        beklenenSonuc= 2
        self.assertEqual(beklenenSonuc, sonuc)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test010']
    unittest.main()