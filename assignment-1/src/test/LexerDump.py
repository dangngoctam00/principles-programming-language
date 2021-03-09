import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_string_11(self):
        self.assertTrue(TestLexer.checkLexeme("\"tam\n\"", "Error Token \"", 17))