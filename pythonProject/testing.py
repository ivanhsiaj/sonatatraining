import unittest
from day2.rpsfun import r_p_s
class AddTest(unittest.TestCase):
    def testAdd1(self):
        self.assertEqual('p',r_p_s('r','p'))
    def testAdd2(self):
        self.assertEqual('p',r_p_s('p','r'))
    @classmethod
    def tearDown(self):
        print("teardown")
    @classmethod
    def setUpClass(self):
        print("setUp class")
    @classmethod
    def teardownClass(self):
        print("teardown class")

