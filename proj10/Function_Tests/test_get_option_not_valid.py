import unittest 
from io import StringIO
from unittest.mock import patch
from proj10 import get_option
      

class MyTestCaseNotValid(unittest.TestCase):
    def printResults(self,given_answer,expected_out,out_str):
        result ="\n-----------"
        result +="\nin_str: {}".format(given_answer)
        result +="\ninstructor error message: {}".format(expected_out)
        result +="\nstudent error message: {}".format(out_str)
        return result
        
    def printReturns(self,given_answer,option,expected_return):
        result ="\n-----------"
        result +="\nin_str: {}".format(given_answer)
        result +="\ninstructor return: {}".format(expected_return)
        result +="\nstudent return: {}".format(option)
        return result

       
    def runTest(self, given_answer, expected_out,expected_return):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:       
            option = get_option()
            out_str = fake_out.getvalue().strip()
            self.assertEqual(option,expected_return, self.printReturns(given_answer,option,expected_return))
            self.assertEqual(out_str, expected_out, self.printResults(given_answer,expected_out,out_str))

    def test1(self):
        self.runTest('x', "Error in option: x",[])
        self.runTest('Z', "Error in option: Z",[])


    def test2(self):
        self.runTest('X 2', "Error in option: X 2", [])
        self.runTest('f', "Error in option: f",[])
        self.runTest('f 5', "Error in option: f 5",[])
        self.runTest('f 0', "Error in option: f 0",[])
        
    def test3(self):
        self.runTest('X 2 3', "Error in option: X 2 3", [])
        self.runTest('t 2', "Error in option: t 2",[])
        self.runTest('T 0 3', "Error in option: T 0 3", [])
        self.runTest('t 3 0', "Error in option: t 3 0", [])
        self.runTest('T 5 3', "Error in option: T 5 3", [])
        self.runTest('t 2 5', "Error in option: t 2 5", [])
        self.runTest('t 0 5', "Error in option: t 0 5", [])        

      
if __name__ == '__main__':
    unittest.main()