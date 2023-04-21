import unittest 
from io import StringIO
from unittest.mock import patch
from proj10 import get_option
      

class MyTestCaseValid(unittest.TestCase):
    def printResults(self,given_answer,expected_out,out_str):
        print("-----------")
        print("in_str:",given_answer)
        print("instructor error message: ",expected_out)
        print("student error message: ",out_str)
        
    def printReturns(self,given_answer,option,expected_return):
        print("-----------")
        print("in_str:",given_answer)
        print("instructor return: ",expected_return)
        print("student return:",option)

       
    def runTest(self, given_answer, expected_out,expected_return):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:       
            option = get_option()
            out_str = fake_out.getvalue().strip()
            self.assertEqual(option,expected_return, self.printReturns(given_answer,option,expected_return))
            self.assertEqual(out_str, expected_out, self.printResults(given_answer,expected_out,out_str))

    def testQ(self):
        self.runTest('Q', '',['Q'])
        self.runTest('q', '',['Q'])

    def testH(self):
        self.runTest('H', '', ['H'])
        self.runTest('h', '',['H'])
        
    def testR(self):
        self.runTest('R', '', ['R'])
        self.runTest('r', '',['R'])
        
    def testD(self):
        self.runTest('D', '', ['D'])
        self.runTest('d', '',['D'])

    def testF(self):
        self.runTest('F 2', '', ['F', 1])
        self.runTest('f 3', '',['F', 2])
        
    def testT(self):
        self.runTest('T 2 3', '', ['T', 1, 2])
        self.runTest('t 3 1', '',['T', 2, 0])


      

if __name__ == '__main__':
    unittest.main()