from re import U
import unittest
import unittest
from palindromo import Palindromo
class TestPalindromo(unittest.TestCase):
    __palindromo=None
    def setUp(self):
        self.__palindromo=Palindromo('menem')
    def testUnPalindromoPar(self):
        self.assertEqual(self.__palindromo.esPalindromo(),True)
    def testNoPalindromo(self):
        self.__palindromo.setPalabra('nose')
        self.assertEqual(self.__palindromo.esPalindromo(),False)
if __name__ =='__main__':
        unittest.main()
