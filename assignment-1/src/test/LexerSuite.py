import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_identifier_0(self):
        self.assertTrue(TestLexer.checkLexeme("While a = 3  Do c = 3 + 3;","While,a,=,3,Do,c,=,3,+,3,;,<EOF>",100))

    def test_identifier_1(self):
        self.assertTrue(TestLexer.checkLexeme("a_bc","a_bc,<EOF>",101))

    def test_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("identifier hello","identifier,hello,<EOF>",183))

    def test_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme("identifier_______   ","identifier_______,<EOF>",165))

    def test_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme("a123","a123,<EOF>",166))

    def test_opeator_0(self):
        self.assertTrue(TestLexer.checkLexeme("\\.","\\.,<EOF>",102))

    def test_opeator_1(self):
        self.assertTrue(TestLexer.checkLexeme("abc+","abc,+,<EOF>",179))

    def test_opeator_2(self):
        self.assertTrue(TestLexer.checkLexeme("abc+","abc,+,<EOF>",186))

    def test_integer_1(self):
        self.assertTrue(TestLexer.checkLexeme("000000", "0,0,0,0,0,0,<EOF>", 103))


    def test_integer_2(self):
        self.assertTrue(TestLexer.checkLexeme("0O123", "0O123,<EOF>", 104))


    def test_integer_3(self):
        self.assertTrue(TestLexer.checkLexeme("0X1", "0X1,<EOF>", 105))

    def test_integer_4(self):
        self.assertTrue(TestLexer.checkLexeme("0012", "0,0,12,<EOF>", 113))

    def test_integer_5(self):
        self.assertTrue(TestLexer.checkLexeme("0012a", "0,0,12,a,<EOF>", 167))

    def test_integer_6(self):
        self.assertTrue(TestLexer.checkLexeme("0X92000", "0X92000,<EOF>", 171))

    #test float number
    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme("0.123", "0.123,<EOF>", 106))

    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme("12e-3", "12e-3,<EOF>", 107))

    def test_float_3(self):
        self.assertTrue(TestLexer.checkLexeme("123e3", "123e3,<EOF>", 108))

    def test_float_4(self):
        self.assertTrue(TestLexer.checkLexeme("012.25", "0,12.25,<EOF>", 109)) #need to think carefully

    def test_float_5(self):
        self.assertTrue(TestLexer.checkLexeme("123.", "123.,<EOF>", 110))

    def test_float_6(self):
        self.assertTrue(TestLexer.checkLexeme("123.0e3", "123.0e3,<EOF>", 111))

    def test_float_7(self):
        self.assertTrue(TestLexer.checkLexeme("123.e", "123.,e,<EOF>", 112))

    def test_float_8(self):
        self.assertTrue(TestLexer.checkLexeme(".1", ".,1,<EOF>", 181))

    def test_float_9(self):
        self.assertTrue(TestLexer.checkLexeme(".3e-2", ".,3e-2,<EOF>", 152))

    def test_float_10(self):
        self.assertTrue(TestLexer.checkLexeme("e-2", "e,-,2,<EOF>", 183))

    def test_float_11(self):
        self.assertTrue(TestLexer.checkLexeme("0x12.e+5", "0x12,.,e,+,5,<EOF>", 154))

    def test_float_12(self):
        self.assertTrue(TestLexer.checkLexeme("123.123.123", "123.123,.,123,<EOF>", 168))

    def test_float_13(self):
        self.assertTrue(TestLexer.checkLexeme("123.123.123", "123.123,.,123,<EOF>", 185))

    def test_float_14(self):
        self.assertTrue(TestLexer.checkLexeme(".1", ".,1,<EOF>", 169))

    def test_float_15(self):
        self.assertTrue(TestLexer.checkLexeme("00.0002e+3", "0,0.0002e+3,<EOF>", 172))

    def test_float_16(self):
        self.assertTrue(TestLexer.checkLexeme("1e", "1,e,<EOF>", 173))

    # Test String

    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme("""   "'"Hello abc 9 \\t"   """, """'"Hello abc 9 \\t,<EOF>""", 120))

    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme("""   "He asked me: '"Where is John?'""   """, """He asked me: '"Where is John?'",<EOF>""", 121))

    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\' hello \\'"  ""","""\\' hello \\',<EOF>""" ,122))

    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme("""  "abc '"  ""","""Unclosed String: abc '"  """ ,123))

    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme("""  "abc' "  ""","Illegal Escape In String: abc' " ,124))

    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme("""  "hello \\'' "  ""","Illegal Escape In String: hello \\'' " ,125))

    def test_string_7(self):
        self.assertTrue(TestLexer.checkLexeme("""  "hi ;) \\ "  ""","Illegal Escape In String: hi ;) \\ " ,126))

    def test_string_8(self):
        self.assertTrue(TestLexer.checkLexeme("""  "hello ;) \\t\\n\\f\\b \\a "  ""","Illegal Escape In String: hello ;) \\t\\n\\f\\b \\a" ,127))

    def test_string_9(self):
        self.assertTrue(TestLexer.checkLexeme("\"abc \'\" \\t\"", "abc \'\" \\t,<EOF>", 119))
    def test_string_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc \'\" \\t" """, "abc \'\" \\t,<EOF>", 118))

    def test_string_11(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\n" """, "Error Token \"", 117))

    def test_string_12(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\"\"""", ",Error Token \"", 116)) #think

    def test_string_13(self):
        self.assertTrue(TestLexer.checkLexeme(""" "string !@#$%^&*()_+) " """, "string !@#$%^&*()_+) ,<EOF>", 157))

    def test_string_14(self):
        self.assertTrue(TestLexer.checkLexeme(""" "string \B" """, "Illegal Escape In String: string \B", 158))

    def test_string_15(self):
        self.assertTrue(TestLexer.checkLexeme(""" "string" """, "string,<EOF>", 159))

    def test_string_16(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\t\\n'"string" """, "\\t\\n'\"string,<EOF>", 160))

    def test_string_17(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" """, ",<EOF>", 115))

    def test_string_18(self):
        self.assertTrue(TestLexer.checkLexeme(""" "string 'a" """, "Illegal Escape In String: string 'a", 161))

    def test_string_19(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123\\mstring" """, "Illegal Escape In String: 123\\m", 162))

    def test_string_20(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123\\t """, "Unclosed String: 123\\t ", 163))

    def test_string_with_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\b\\f\\r\\t\\n\\'\\\\ '"1231212@#$%?" ""","""abc\\b\\f\\r\\t\\n\\'\\\\ '"1231212@#$%?,<EOF>""", 180))

    def test_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme("** abc **","<EOF>" ,128))

    def test_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme("x + y = 3**abc**","x,+,y,=,3,<EOF>" ,129))

    def test_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme("****","<EOF>" ,130))

    def test_comment_4(self):
        input = """
            **This is single line comment***
            x + 3 = 5;
            **This is a
            * multi-line
            * comment
            **
        """
        self.assertTrue(TestLexer.checkLexeme(input,"*,x,+,3,=,5,;,<EOF>" ,131))

    def test_comment_5(self):
        input = """
            **hello ;)*
        """
        self.assertTrue(TestLexer.checkLexeme(input,"Unterminated Comment" ,134))

    def test_comment_6(self):
        input = """
            **hello ;)* * * *
        """
        self.assertTrue(TestLexer.checkLexeme(input,"Unterminated Comment" ,135))

    def test_comment_7(self):
        input = """
            **hello ;)
        """
        self.assertTrue(TestLexer.checkLexeme(input,"Unterminated Comment" ,136))

    def test_comment_8(self):
        input = """
            **hello ;)**
            **
            *
        """
        self.assertTrue(TestLexer.checkLexeme(input,"Unterminated Comment" ,137))

    def test_comment_9(self):
        input = """
            **hello ;)**
            **
            * *
        """
        self.assertTrue(TestLexer.checkLexeme(input,"Unterminated Comment" ,114))

    def test_comment_10(self):
        input = """
            **************************************!@#$%^&*()_+```)**identifier
        """
        self.assertTrue(TestLexer.checkLexeme(input,"identifier,<EOF>" ,174))

    def test_comment_11(self):
        input = """
            hello**************************************!@#$%^&*()_+```)**identifier
        """
        self.assertTrue(TestLexer.checkLexeme(input,"hello,identifier,<EOF>" ,175))

    def test_comment_12(self):
        input = """
            ***!@#$%^&*()_+```)**identifier
        """
        self.assertTrue(TestLexer.checkLexeme(input,"identifier,<EOF>" ,176))

    def test_comment_13(self):
        input = """
            *****identifier
        """
        self.assertTrue(TestLexer.checkLexeme(input,"*,identifier,<EOF>" ,177))

    def test_comment_14(self):
        input = """
            **
            !@#$%^&*()___)
            **
            ^
        """
        self.assertTrue(TestLexer.checkLexeme(input,"Error Token ^" ,178))

    def test_comment_15(self):
        input = """
            **
            !@#$%^&*()___)
            **
            123
        """
        self.assertTrue(TestLexer.checkLexeme(input,"123,<EOF>" ,170))


    def test_wrong_token_1(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",132))

    def test_wrong_token_2(self):
        self.assertTrue(TestLexer.checkLexeme("?abc","Error Token ?",133))

    def test_wrong_token_3(self):
        self.assertTrue(TestLexer.checkLexeme("/","Error Token /",138))

    def test_wrong_token_4(self):
        self.assertTrue(TestLexer.checkLexeme("\"","Error Token \"",139))

    def test_wrong_token_5(self):
        self.assertTrue(TestLexer.checkLexeme("hello@","hello,Error Token @",140))

    def test_wrong_token_6(self):
        self.assertTrue(TestLexer.checkLexeme("^&l@","Error Token ^",141))

    def test_wrong_token_7(self):
        self.assertTrue(TestLexer.checkLexeme("abc&","abc,Error Token &",142))

    def test_wrong_token_8(self):
        self.assertTrue(TestLexer.checkLexeme("abc,&","abc,,,Error Token &",143))

    def test_wrong_token_9(self):
        self.assertTrue(TestLexer.checkLexeme("'","Error Token '",144))

    def test_wrong_token_10(self):
        self.assertTrue(TestLexer.checkLexeme("hi ;) /","hi,;,),Error Token /",145))

    def test_wrong_token_11(self):
        self.assertTrue(TestLexer.checkLexeme(" |","Error Token |",146))

    def test_wrong_token_12(self):
        self.assertTrue(TestLexer.checkLexeme(" !@l","!,Error Token @",147))

    def test_wrong_token_13(self):
        self.assertTrue(TestLexer.checkLexeme("hello i !@l","hello,i,!,Error Token @",148))

    def test_wrong_token_14(self):
        self.assertTrue(TestLexer.checkLexeme("hi ?l","hi,Error Token ?",149))

    def test_wrong_token_15(self):
        self.assertTrue(TestLexer.checkLexeme("_@#$%^&*()___+)","Error Token _",150))

    def test_wrong_token_16(self):
        self.assertTrue(TestLexer.checkLexeme(" asterisk__ ^* ", "asterisk__,Error Token ^", 151))

    def test_wrong_token_17(self):
        self.assertTrue(TestLexer.checkLexeme(" asterisk__ ((/))* ", "asterisk__,(,(,Error Token /", 182))

    def test_wrong_token_18(self):
        self.assertTrue(TestLexer.checkLexeme(" asterisk__|| ((\))* ", "asterisk__,||,(,(,\,),),*,<EOF>", 153))

    def test_wrong_token_19(self):
        self.assertTrue(TestLexer.checkLexeme("hello `", "hello,Error Token `", 184))
    def test_wrong_token_20(self):
        self.assertTrue(TestLexer.checkLexeme("****", "<EOF>", 155))

    def test_wrong_token_21(self):
        self.assertTrue(TestLexer.checkLexeme("*", "*,<EOF>", 156))

    def test_overall_0(self):
        self.assertTrue(TestLexer.checkLexeme(""" "string \\\\\c !@#$%^&*())"  """, "Illegal Escape In String: string \\\\\c", 187))

    def test_overall_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Error Dot"  """, "Error Dot,<EOF>", 188))

    def test_overall_2(self):
        self.assertTrue(TestLexer.checkLexeme("Error", "Error Token E", 189))

    def test_overall_3(self):
        self.assertTrue(TestLexer.checkLexeme("error dot.", "error,dot,.,<EOF>", 190))

    def test_overall_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'"'"'"'"'"'"'"'"" """, "\'\"\'\"\'\"\'\"\'\"\'\"\'\"\'\",<EOF>", 191))

    def test_overall_5(self):
        self.assertTrue(TestLexer.checkLexeme("** hi ** ^", "Error Token ^", 192))

    def test_overall_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\\\\\\\" """, "\\\\\\\\,<EOF>", 193))

    def test_overall_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\\\\\ " """, "Illegal Escape In String: \\\\\\ ", 194))

    def test_overall_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\\\\\n" """, "\\\\\\n,<EOF>", 195))

    def test_overall_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\\\\\n" **!@#$%^&*(****)** """, "\\\\\\n,<EOF>", 196))

    def test_overall_10(self):
        self.assertTrue(TestLexer.checkLexeme(" While (x == 5) : + - ", "While,(,x,==,5,),:,+,-,<EOF>", 197))

    def test_overall_11(self):
        self.assertTrue(TestLexer.checkLexeme("**\n^**@", "Error Token @", 198))

    def test_overall_12(self):
        self.assertTrue(TestLexer.checkLexeme("-0143e", "-,0,143,e,<EOF>", 199))


    # def test_overall_13(self):
        # self.assertTrue(TestLexer.checkLexeme(""" "abc \'\" \\t" """, "abc \'\" \\t,<EOF>", 10))

