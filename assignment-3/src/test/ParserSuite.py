import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_418(self):
        input = """                      
                    Function: main
                        Parameter: x[1][1]
                        Body:                            
                            x = {{1}};                           
                            Return x;
                        EndBody.                      

                """
        expect = str("Redeclared Variable: x")
        self.assertTrue(TestParser.checkParser(input,expect,418))

    