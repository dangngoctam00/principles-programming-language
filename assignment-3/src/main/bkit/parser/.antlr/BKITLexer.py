# Generated from /home/scotlandyard/201/ppl/assignment3/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0232\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&")
        buf.write("\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\67\3\67\3\67\38")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\7>\u0184\n")
        buf.write(">\f>\16>\u0187\13>\3?\3?\5?\u018b\n?\3?\6?\u018e\n?\r")
        buf.write("?\16?\u018f\3@\3@\3@\3@\5@\u0196\n@\3A\3A\3B\3B\3B\3B")
        buf.write("\3B\5B\u019f\nB\3C\3C\3C\7C\u01a4\nC\fC\16C\u01a7\13C")
        buf.write("\3C\3C\3C\5C\u01ac\nC\3C\3C\7C\u01b0\nC\fC\16C\u01b3\13")
        buf.write("C\3C\3C\3C\5C\u01b8\nC\3C\3C\7C\u01bc\nC\fC\16C\u01bf")
        buf.write("\13C\5C\u01c1\nC\3D\3D\3D\7D\u01c6\nD\fD\16D\u01c9\13")
        buf.write("D\5D\u01cb\nD\3D\3D\3D\3D\3D\5D\u01d2\nD\3E\3E\3E\3E\3")
        buf.write("E\7E\u01d9\nE\fE\16E\u01dc\13E\3F\3F\3F\3F\5F\u01e2\n")
        buf.write("F\3G\3G\3G\3G\5G\u01e8\nG\3H\3H\5H\u01ec\nH\3I\3I\3I\7")
        buf.write("I\u01f1\nI\fI\16I\u01f4\13I\3I\3I\3J\6J\u01f9\nJ\rJ\16")
        buf.write("J\u01fa\3J\3J\3K\3K\3K\3K\7K\u0203\nK\fK\16K\u0206\13")
        buf.write("K\3K\3K\3K\3K\3K\3L\3L\3M\3M\3M\7M\u0212\nM\fM\16M\u0215")
        buf.write("\13M\3N\3N\3N\7N\u021a\nN\fN\16N\u021d\13N\3N\3N\3O\3")
        buf.write("O\3O\3O\3O\7O\u0226\nO\fO\16O\u0229\13O\3O\7O\u022c\n")
        buf.write("O\fO\16O\u022f\13O\5O\u0231\nO\3\u0204\2P\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q\2s\2u\2w\2y\2{")
        buf.write("\2}\2\177\2\u0081\2\u0083\2\u0085:\u0087;\u0089<\u008b")
        buf.write("\2\u008d\2\u008f\2\u0091=\u0093>\u0095?\u0097@\u0099A")
        buf.write("\u009bB\u009dC\3\2\20\3\2\62;\3\2\63;\3\2c|\3\2C\\\4\2")
        buf.write("GGgg\4\2--//\t\2))^^ddhhppttvv\3\2$$\3\2CH\3\2\629\7\2")
        buf.write("\f\f\17\17$$))^^\5\2\13\f\17\17\"\"\6\2\f\f$$))^^\3\2")
        buf.write(",,\2\u024a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2")
        buf.write("\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2")
        buf.write("\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\3\u009f\3\2\2\2\5\u00a1\3\2\2\2\7\u00a3\3\2\2")
        buf.write("\2\t\u00a5\3\2\2\2\13\u00a7\3\2\2\2\r\u00a9\3\2\2\2\17")
        buf.write("\u00ab\3\2\2\2\21\u00ad\3\2\2\2\23\u00af\3\2\2\2\25\u00b1")
        buf.write("\3\2\2\2\27\u00b3\3\2\2\2\31\u00b8\3\2\2\2\33\u00be\3")
        buf.write("\2\2\2\35\u00c7\3\2\2\2\37\u00ca\3\2\2\2!\u00cf\3\2\2")
        buf.write("\2#\u00d6\3\2\2\2%\u00de\3\2\2\2\'\u00e4\3\2\2\2)\u00eb")
        buf.write("\3\2\2\2+\u00f4\3\2\2\2-\u00f8\3\2\2\2/\u0101\3\2\2\2")
        buf.write("\61\u0104\3\2\2\2\63\u010e\3\2\2\2\65\u0115\3\2\2\2\67")
        buf.write("\u011a\3\2\2\29\u011e\3\2\2\2;\u0124\3\2\2\2=\u0129\3")
        buf.write("\2\2\2?\u012f\3\2\2\2A\u0135\3\2\2\2C\u0137\3\2\2\2E\u0139")
        buf.write("\3\2\2\2G\u013b\3\2\2\2I\u013d\3\2\2\2K\u013f\3\2\2\2")
        buf.write("M\u0141\3\2\2\2O\u0144\3\2\2\2Q\u0147\3\2\2\2S\u0149\3")
        buf.write("\2\2\2U\u014b\3\2\2\2W\u014e\3\2\2\2Y\u0151\3\2\2\2[\u0154")
        buf.write("\3\2\2\2]\u0157\3\2\2\2_\u015a\3\2\2\2a\u015d\3\2\2\2")
        buf.write("c\u0160\3\2\2\2e\u0163\3\2\2\2g\u0167\3\2\2\2i\u016b\3")
        buf.write("\2\2\2k\u016f\3\2\2\2m\u0171\3\2\2\2o\u0174\3\2\2\2q\u0177")
        buf.write("\3\2\2\2s\u0179\3\2\2\2u\u017b\3\2\2\2w\u017d\3\2\2\2")
        buf.write("y\u017f\3\2\2\2{\u0181\3\2\2\2}\u0188\3\2\2\2\177\u0195")
        buf.write("\3\2\2\2\u0081\u0197\3\2\2\2\u0083\u019e\3\2\2\2\u0085")
        buf.write("\u01c0\3\2\2\2\u0087\u01ca\3\2\2\2\u0089\u01d3\3\2\2\2")
        buf.write("\u008b\u01e1\3\2\2\2\u008d\u01e7\3\2\2\2\u008f\u01eb\3")
        buf.write("\2\2\2\u0091\u01ed\3\2\2\2\u0093\u01f8\3\2\2\2\u0095\u01fe")
        buf.write("\3\2\2\2\u0097\u020c\3\2\2\2\u0099\u020e\3\2\2\2\u009b")
        buf.write("\u0216\3\2\2\2\u009d\u0220\3\2\2\2\u009f\u00a0\7*\2\2")
        buf.write("\u00a0\4\3\2\2\2\u00a1\u00a2\7+\2\2\u00a2\6\3\2\2\2\u00a3")
        buf.write("\u00a4\7]\2\2\u00a4\b\3\2\2\2\u00a5\u00a6\7_\2\2\u00a6")
        buf.write("\n\3\2\2\2\u00a7\u00a8\7}\2\2\u00a8\f\3\2\2\2\u00a9\u00aa")
        buf.write("\7\177\2\2\u00aa\16\3\2\2\2\u00ab\u00ac\7<\2\2\u00ac\20")
        buf.write("\3\2\2\2\u00ad\u00ae\7=\2\2\u00ae\22\3\2\2\2\u00af\u00b0")
        buf.write("\7\60\2\2\u00b0\24\3\2\2\2\u00b1\u00b2\7.\2\2\u00b2\26")
        buf.write("\3\2\2\2\u00b3\u00b4\7D\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6")
        buf.write("\7f\2\2\u00b6\u00b7\7{\2\2\u00b7\30\3\2\2\2\u00b8\u00b9")
        buf.write("\7D\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc")
        buf.write("\7c\2\2\u00bc\u00bd\7m\2\2\u00bd\32\3\2\2\2\u00be\u00bf")
        buf.write("\7E\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2")
        buf.write("\7v\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5")
        buf.write("\7w\2\2\u00c5\u00c6\7g\2\2\u00c6\34\3\2\2\2\u00c7\u00c8")
        buf.write("\7F\2\2\u00c8\u00c9\7q\2\2\u00c9\36\3\2\2\2\u00ca\u00cb")
        buf.write("\7G\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd\7u\2\2\u00cd\u00ce")
        buf.write("\7g\2\2\u00ce \3\2\2\2\u00cf\u00d0\7G\2\2\u00d0\u00d1")
        buf.write("\7n\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4")
        buf.write("\7K\2\2\u00d4\u00d5\7h\2\2\u00d5\"\3\2\2\2\u00d6\u00d7")
        buf.write("\7G\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9\7f\2\2\u00d9\u00da")
        buf.write("\7D\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7f\2\2\u00dc\u00dd")
        buf.write("\7{\2\2\u00dd$\3\2\2\2\u00de\u00df\7G\2\2\u00df\u00e0")
        buf.write("\7p\2\2\u00e0\u00e1\7f\2\2\u00e1\u00e2\7K\2\2\u00e2\u00e3")
        buf.write("\7h\2\2\u00e3&\3\2\2\2\u00e4\u00e5\7G\2\2\u00e5\u00e6")
        buf.write("\7p\2\2\u00e6\u00e7\7f\2\2\u00e7\u00e8\7H\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7t\2\2\u00ea(\3\2\2\2\u00eb\u00ec")
        buf.write("\7G\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7f\2\2\u00ee\u00ef")
        buf.write("\7Y\2\2\u00ef\u00f0\7j\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2")
        buf.write("\7n\2\2\u00f2\u00f3\7g\2\2\u00f3*\3\2\2\2\u00f4\u00f5")
        buf.write("\7H\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7t\2\2\u00f7,\3")
        buf.write("\2\2\2\u00f8\u00f9\7H\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb")
        buf.write("\7p\2\2\u00fb\u00fc\7e\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe")
        buf.write("\7k\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100\7p\2\2\u0100.\3")
        buf.write("\2\2\2\u0101\u0102\7K\2\2\u0102\u0103\7h\2\2\u0103\60")
        buf.write("\3\2\2\2\u0104\u0105\7R\2\2\u0105\u0106\7c\2\2\u0106\u0107")
        buf.write("\7t\2\2\u0107\u0108\7c\2\2\u0108\u0109\7o\2\2\u0109\u010a")
        buf.write("\7g\2\2\u010a\u010b\7v\2\2\u010b\u010c\7g\2\2\u010c\u010d")
        buf.write("\7t\2\2\u010d\62\3\2\2\2\u010e\u010f\7T\2\2\u010f\u0110")
        buf.write("\7g\2\2\u0110\u0111\7v\2\2\u0111\u0112\7w\2\2\u0112\u0113")
        buf.write("\7t\2\2\u0113\u0114\7p\2\2\u0114\64\3\2\2\2\u0115\u0116")
        buf.write("\7V\2\2\u0116\u0117\7j\2\2\u0117\u0118\7g\2\2\u0118\u0119")
        buf.write("\7p\2\2\u0119\66\3\2\2\2\u011a\u011b\7X\2\2\u011b\u011c")
        buf.write("\7c\2\2\u011c\u011d\7t\2\2\u011d8\3\2\2\2\u011e\u011f")
        buf.write("\7Y\2\2\u011f\u0120\7j\2\2\u0120\u0121\7k\2\2\u0121\u0122")
        buf.write("\7n\2\2\u0122\u0123\7g\2\2\u0123:\3\2\2\2\u0124\u0125")
        buf.write("\7V\2\2\u0125\u0126\7t\2\2\u0126\u0127\7w\2\2\u0127\u0128")
        buf.write("\7g\2\2\u0128<\3\2\2\2\u0129\u012a\7H\2\2\u012a\u012b")
        buf.write("\7c\2\2\u012b\u012c\7n\2\2\u012c\u012d\7u\2\2\u012d\u012e")
        buf.write("\7g\2\2\u012e>\3\2\2\2\u012f\u0130\7G\2\2\u0130\u0131")
        buf.write("\7p\2\2\u0131\u0132\7f\2\2\u0132\u0133\7F\2\2\u0133\u0134")
        buf.write("\7q\2\2\u0134@\3\2\2\2\u0135\u0136\7?\2\2\u0136B\3\2\2")
        buf.write("\2\u0137\u0138\7-\2\2\u0138D\3\2\2\2\u0139\u013a\7/\2")
        buf.write("\2\u013aF\3\2\2\2\u013b\u013c\7,\2\2\u013cH\3\2\2\2\u013d")
        buf.write("\u013e\7^\2\2\u013eJ\3\2\2\2\u013f\u0140\7\'\2\2\u0140")
        buf.write("L\3\2\2\2\u0141\u0142\7?\2\2\u0142\u0143\7?\2\2\u0143")
        buf.write("N\3\2\2\2\u0144\u0145\7#\2\2\u0145\u0146\7?\2\2\u0146")
        buf.write("P\3\2\2\2\u0147\u0148\7@\2\2\u0148R\3\2\2\2\u0149\u014a")
        buf.write("\7>\2\2\u014aT\3\2\2\2\u014b\u014c\7@\2\2\u014c\u014d")
        buf.write("\7?\2\2\u014dV\3\2\2\2\u014e\u014f\7>\2\2\u014f\u0150")
        buf.write("\7?\2\2\u0150X\3\2\2\2\u0151\u0152\7-\2\2\u0152\u0153")
        buf.write("\7\60\2\2\u0153Z\3\2\2\2\u0154\u0155\7/\2\2\u0155\u0156")
        buf.write("\7\60\2\2\u0156\\\3\2\2\2\u0157\u0158\7,\2\2\u0158\u0159")
        buf.write("\7\60\2\2\u0159^\3\2\2\2\u015a\u015b\7^\2\2\u015b\u015c")
        buf.write("\7\60\2\2\u015c`\3\2\2\2\u015d\u015e\7@\2\2\u015e\u015f")
        buf.write("\7\60\2\2\u015fb\3\2\2\2\u0160\u0161\7>\2\2\u0161\u0162")
        buf.write("\7\60\2\2\u0162d\3\2\2\2\u0163\u0164\7@\2\2\u0164\u0165")
        buf.write("\7?\2\2\u0165\u0166\7\60\2\2\u0166f\3\2\2\2\u0167\u0168")
        buf.write("\7>\2\2\u0168\u0169\7?\2\2\u0169\u016a\7\60\2\2\u016a")
        buf.write("h\3\2\2\2\u016b\u016c\7?\2\2\u016c\u016d\7\61\2\2\u016d")
        buf.write("\u016e\7?\2\2\u016ej\3\2\2\2\u016f\u0170\7#\2\2\u0170")
        buf.write("l\3\2\2\2\u0171\u0172\7(\2\2\u0172\u0173\7(\2\2\u0173")
        buf.write("n\3\2\2\2\u0174\u0175\7~\2\2\u0175\u0176\7~\2\2\u0176")
        buf.write("p\3\2\2\2\u0177\u0178\t\2\2\2\u0178r\3\2\2\2\u0179\u017a")
        buf.write("\t\3\2\2\u017at\3\2\2\2\u017b\u017c\t\4\2\2\u017cv\3\2")
        buf.write("\2\2\u017d\u017e\t\5\2\2\u017ex\3\2\2\2\u017f\u0180\7")
        buf.write("a\2\2\u0180z\3\2\2\2\u0181\u0185\7\60\2\2\u0182\u0184")
        buf.write("\t\2\2\2\u0183\u0182\3\2\2\2\u0184\u0187\3\2\2\2\u0185")
        buf.write("\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186|\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0188\u018a\t\6\2\2\u0189\u018b\t\7\2\2")
        buf.write("\u018a\u0189\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018d\3")
        buf.write("\2\2\2\u018c\u018e\t\3\2\2\u018d\u018c\3\2\2\2\u018e\u018f")
        buf.write("\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("~\3\2\2\2\u0191\u0192\7^\2\2\u0192\u0196\t\b\2\2\u0193")
        buf.write("\u0194\7)\2\2\u0194\u0196\7$\2\2\u0195\u0191\3\2\2\2\u0195")
        buf.write("\u0193\3\2\2\2\u0196\u0080\3\2\2\2\u0197\u0198\t\b\2\2")
        buf.write("\u0198\u0082\3\2\2\2\u0199\u019a\7^\2\2\u019a\u019f\n")
        buf.write("\b\2\2\u019b\u019f\7^\2\2\u019c\u019d\7)\2\2\u019d\u019f")
        buf.write("\n\t\2\2\u019e\u0199\3\2\2\2\u019e\u019b\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019f\u0084\3\2\2\2\u01a0\u01c1\7\62\2")
        buf.write("\2\u01a1\u01a5\5s:\2\u01a2\u01a4\5q9\2\u01a3\u01a2\3\2")
        buf.write("\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01c1\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8")
        buf.write("\u01ab\5\u008bF\2\u01a9\u01ac\5s:\2\u01aa\u01ac\t\n\2")
        buf.write("\2\u01ab\u01a9\3\2\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01b1")
        buf.write("\3\2\2\2\u01ad\u01b0\5q9\2\u01ae\u01b0\t\n\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1")
        buf.write("\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01c1\3\2\2\2")
        buf.write("\u01b3\u01b1\3\2\2\2\u01b4\u01b7\5\u008dG\2\u01b5\u01b8")
        buf.write("\5s:\2\u01b6\u01b8\t\13\2\2\u01b7\u01b5\3\2\2\2\u01b7")
        buf.write("\u01b6\3\2\2\2\u01b8\u01bd\3\2\2\2\u01b9\u01bc\5q9\2\u01ba")
        buf.write("\u01bc\t\13\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01ba\3\2\2")
        buf.write("\2\u01bc\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be")
        buf.write("\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0")
        buf.write("\u01a0\3\2\2\2\u01c0\u01a1\3\2\2\2\u01c0\u01a8\3\2\2\2")
        buf.write("\u01c0\u01b4\3\2\2\2\u01c1\u0086\3\2\2\2\u01c2\u01cb\7")
        buf.write("\62\2\2\u01c3\u01c7\5s:\2\u01c4\u01c6\5q9\2\u01c5\u01c4")
        buf.write("\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7")
        buf.write("\u01c8\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01ca\u01c2\3\2\2\2\u01ca\u01c3\3\2\2\2\u01cb\u01d1\3")
        buf.write("\2\2\2\u01cc\u01d2\5{>\2\u01cd\u01d2\5}?\2\u01ce\u01cf")
        buf.write("\5{>\2\u01cf\u01d0\5}?\2\u01d0\u01d2\3\2\2\2\u01d1\u01cc")
        buf.write("\3\2\2\2\u01d1\u01cd\3\2\2\2\u01d1\u01ce\3\2\2\2\u01d2")
        buf.write("\u0088\3\2\2\2\u01d3\u01da\5u;\2\u01d4\u01d9\5y=\2\u01d5")
        buf.write("\u01d9\5u;\2\u01d6\u01d9\5w<\2\u01d7\u01d9\5q9\2\u01d8")
        buf.write("\u01d4\3\2\2\2\u01d8\u01d5\3\2\2\2\u01d8\u01d6\3\2\2\2")
        buf.write("\u01d8\u01d7\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8\3")
        buf.write("\2\2\2\u01da\u01db\3\2\2\2\u01db\u008a\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dd\u01de\7\62\2\2\u01de\u01e2\7z\2\2\u01df")
        buf.write("\u01e0\7\62\2\2\u01e0\u01e2\7Z\2\2\u01e1\u01dd\3\2\2\2")
        buf.write("\u01e1\u01df\3\2\2\2\u01e2\u008c\3\2\2\2\u01e3\u01e4\7")
        buf.write("\62\2\2\u01e4\u01e8\7q\2\2\u01e5\u01e6\7\62\2\2\u01e6")
        buf.write("\u01e8\7Q\2\2\u01e7\u01e3\3\2\2\2\u01e7\u01e5\3\2\2\2")
        buf.write("\u01e8\u008e\3\2\2\2\u01e9\u01ec\5;\36\2\u01ea\u01ec\5")
        buf.write("=\37\2\u01eb\u01e9\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec\u0090")
        buf.write("\3\2\2\2\u01ed\u01f2\7$\2\2\u01ee\u01f1\n\f\2\2\u01ef")
        buf.write("\u01f1\5\177@\2\u01f0\u01ee\3\2\2\2\u01f0\u01ef\3\2\2")
        buf.write("\2\u01f1\u01f4\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3")
        buf.write("\3\2\2\2\u01f3\u01f5\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5")
        buf.write("\u01f6\7$\2\2\u01f6\u0092\3\2\2\2\u01f7\u01f9\t\r\2\2")
        buf.write("\u01f8\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01f8\3")
        buf.write("\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd")
        buf.write("\bJ\2\2\u01fd\u0094\3\2\2\2\u01fe\u01ff\7,\2\2\u01ff\u0200")
        buf.write("\7,\2\2\u0200\u0204\3\2\2\2\u0201\u0203\13\2\2\2\u0202")
        buf.write("\u0201\3\2\2\2\u0203\u0206\3\2\2\2\u0204\u0205\3\2\2\2")
        buf.write("\u0204\u0202\3\2\2\2\u0205\u0207\3\2\2\2\u0206\u0204\3")
        buf.write("\2\2\2\u0207\u0208\7,\2\2\u0208\u0209\7,\2\2\u0209\u020a")
        buf.write("\3\2\2\2\u020a\u020b\bK\2\2\u020b\u0096\3\2\2\2\u020c")
        buf.write("\u020d\13\2\2\2\u020d\u0098\3\2\2\2\u020e\u0213\7$\2\2")
        buf.write("\u020f\u0212\n\f\2\2\u0210\u0212\5\177@\2\u0211\u020f")
        buf.write("\3\2\2\2\u0211\u0210\3\2\2\2\u0212\u0215\3\2\2\2\u0213")
        buf.write("\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u009a\3\2\2\2")
        buf.write("\u0215\u0213\3\2\2\2\u0216\u021b\7$\2\2\u0217\u021a\n")
        buf.write("\16\2\2\u0218\u021a\5\177@\2\u0219\u0217\3\2\2\2\u0219")
        buf.write("\u0218\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2\2")
        buf.write("\u021b\u021c\3\2\2\2\u021c\u021e\3\2\2\2\u021d\u021b\3")
        buf.write("\2\2\2\u021e\u021f\5\u0083B\2\u021f\u009c\3\2\2\2\u0220")
        buf.write("\u0221\7,\2\2\u0221\u0222\7,\2\2\u0222\u0230\3\2\2\2\u0223")
        buf.write("\u0224\7,\2\2\u0224\u0226\n\17\2\2\u0225\u0223\3\2\2\2")
        buf.write("\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3")
        buf.write("\2\2\2\u0228\u0231\3\2\2\2\u0229\u0227\3\2\2\2\u022a\u022c")
        buf.write("\n\17\2\2\u022b\u022a\3\2\2\2\u022c\u022f\3\2\2\2\u022d")
        buf.write("\u022b\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u0231\3\2\2\2")
        buf.write("\u022f\u022d\3\2\2\2\u0230\u0227\3\2\2\2\u0230\u022d\3")
        buf.write("\2\2\2\u0231\u009e\3\2\2\2#\2\u0185\u018a\u018f\u0195")
        buf.write("\u019e\u01a5\u01ab\u01af\u01b1\u01b7\u01bb\u01bd\u01c0")
        buf.write("\u01c7\u01ca\u01d1\u01d8\u01da\u01e1\u01e7\u01eb\u01f0")
        buf.write("\u01f2\u01fa\u0204\u0211\u0213\u0219\u021b\u0227\u022d")
        buf.write("\u0230\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LP = 1
    RP = 2
    LSB = 3
    RSB = 4
    LCB = 5
    RCB = 6
    COLON = 7
    SEMICOLON = 8
    DOT = 9
    COMMA = 10
    BODY = 11
    BREAK = 12
    CONTINUE = 13
    DO = 14
    ELSE = 15
    ELSEIF = 16
    ENDBODY = 17
    ENDIF = 18
    ENDFOR = 19
    ENDWHILE = 20
    FOR = 21
    FUNCTION = 22
    IF = 23
    PARAMETER = 24
    RETURN = 25
    THEN = 26
    VAR = 27
    WHILE = 28
    TRUE = 29
    FALSE = 30
    ENDDO = 31
    EQUAL = 32
    ADD_OP_INT = 33
    SUB_OP_INT = 34
    MUL_OP_INT = 35
    DIV_OP_INT = 36
    MOD_OP_INT = 37
    EQUAL_OP_INT = 38
    NOT_EQUAL_OP_INT = 39
    GREATER_OP_INT = 40
    LESS_OP_INT = 41
    GREATER_EQUAL_OP_INT = 42
    LESS_EQUAL_OP_INT = 43
    ADD_OP_FLOAT = 44
    SUB_OP_FLOAT = 45
    MUL_OP_FLOAT = 46
    DIV_OP_FLOAT = 47
    GREATER_OP_FLOAT = 48
    LESS_OP_FLOAT = 49
    GREATER_EQUAL_OP_FLOAT = 50
    LESS_EQUAL_OP_FLOAT = 51
    NOT_EQUAL_OP_FLOAT = 52
    NOT_OP = 53
    AND_OP = 54
    OR_OP = 55
    INTEGER = 56
    FLOAT = 57
    IDENTIFIER = 58
    STRING = 59
    WS = 60
    COMMENT = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    UNTERMINATED_COMMENT = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "'{'", "'}'", "':'", "';'", "'.'", 
            "','", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'Var'", "'While'", "'True'", "'False'", "'EndDo'", "'='", "'+'", 
            "'-'", "'*'", "'\\'", "'%'", "'=='", "'!='", "'>'", "'<'", "'>='", 
            "'<='", "'+.'", "'-.'", "'*.'", "'\\.'", "'>.'", "'<.'", "'>=.'", 
            "'<=.'", "'=/='", "'!'", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>",
            "LP", "RP", "LSB", "RSB", "LCB", "RCB", "COLON", "SEMICOLON", 
            "DOT", "COMMA", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
            "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
            "FALSE", "ENDDO", "EQUAL", "ADD_OP_INT", "SUB_OP_INT", "MUL_OP_INT", 
            "DIV_OP_INT", "MOD_OP_INT", "EQUAL_OP_INT", "NOT_EQUAL_OP_INT", 
            "GREATER_OP_INT", "LESS_OP_INT", "GREATER_EQUAL_OP_INT", "LESS_EQUAL_OP_INT", 
            "ADD_OP_FLOAT", "SUB_OP_FLOAT", "MUL_OP_FLOAT", "DIV_OP_FLOAT", 
            "GREATER_OP_FLOAT", "LESS_OP_FLOAT", "GREATER_EQUAL_OP_FLOAT", 
            "LESS_EQUAL_OP_FLOAT", "NOT_EQUAL_OP_FLOAT", "NOT_OP", "AND_OP", 
            "OR_OP", "INTEGER", "FLOAT", "IDENTIFIER", "STRING", "WS", "COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "LP", "RP", "LSB", "RSB", "LCB", "RCB", "COLON", "SEMICOLON", 
                  "DOT", "COMMA", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                  "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", 
                  "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", 
                  "WHILE", "TRUE", "FALSE", "ENDDO", "EQUAL", "ADD_OP_INT", 
                  "SUB_OP_INT", "MUL_OP_INT", "DIV_OP_INT", "MOD_OP_INT", 
                  "EQUAL_OP_INT", "NOT_EQUAL_OP_INT", "GREATER_OP_INT", 
                  "LESS_OP_INT", "GREATER_EQUAL_OP_INT", "LESS_EQUAL_OP_INT", 
                  "ADD_OP_FLOAT", "SUB_OP_FLOAT", "MUL_OP_FLOAT", "DIV_OP_FLOAT", 
                  "GREATER_OP_FLOAT", "LESS_OP_FLOAT", "GREATER_EQUAL_OP_FLOAT", 
                  "LESS_EQUAL_OP_FLOAT", "NOT_EQUAL_OP_FLOAT", "NOT_OP", 
                  "AND_OP", "OR_OP", "DIGIT", "NZERO_DIGIT", "LOWER_LETTER", 
                  "UPPER_LETTER", "UNDERSCORE", "DECIMAL_PART", "EXPONENT_PART", 
                  "ESCAPE_SEQUENCE", "ESCAPE_CHARACTER", "ILLEGAL_ESCAPE_SQ", 
                  "INTEGER", "FLOAT", "IDENTIFIER", "HEXA", "OCTAL", "BOOLEAN", 
                  "STRING", "WS", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
    	tk = self.type
    	result = super().emit()
    	if tk == self.UNCLOSE_STRING:       
    		raise UncloseString(result.text[1:])
    	elif tk == self.ILLEGAL_ESCAPE:
    		raise IllegalEscape(result.text[1:])
    	elif tk == self.ERROR_CHAR:
    		raise ErrorToken(result.text)
    	elif tk == self.UNTERMINATED_COMMENT:
    		raise UnterminatedComment()
    	elif tk == self.STRING:
    		result.text = self.text[1:-1]
    		return result;
    	else:
    		return result;


