# Generated from c:\Users\HP\Downloads\temp\ppl\Assignment-1-PPL\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2K")
        buf.write("\u02af\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3")
        buf.write(")\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38\38\3")
        buf.write("8\39\39\39\3:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3=\3")
        buf.write("=\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3")
        buf.write("E\3F\3F\7F\u0209\nF\fF\16F\u020c\13F\3G\3G\5G\u0210\n")
        buf.write("G\3G\6G\u0213\nG\rG\16G\u0214\3H\3H\3H\3H\5H\u021b\nH")
        buf.write("\3I\3I\3J\3J\3J\3J\3J\5J\u0224\nJ\3K\3K\3K\3K\3K\7K\u022b")
        buf.write("\nK\fK\16K\u022e\13K\3L\3L\3L\3L\5L\u0234\nL\3M\3M\3M")
        buf.write("\3M\5M\u023a\nM\3N\3N\5N\u023e\nN\3O\3O\3O\7O\u0243\n")
        buf.write("O\fO\16O\u0246\13O\3O\3O\3O\7O\u024b\nO\fO\16O\u024e\13")
        buf.write("O\3O\3O\3O\7O\u0253\nO\fO\16O\u0256\13O\5O\u0258\nO\3")
        buf.write("P\3P\3P\7P\u025d\nP\fP\16P\u0260\13P\5P\u0262\nP\3P\3")
        buf.write("P\3P\3P\3P\5P\u0269\nP\3Q\3Q\3Q\7Q\u026e\nQ\fQ\16Q\u0271")
        buf.write("\13Q\3Q\3Q\3R\6R\u0276\nR\rR\16R\u0277\3R\3R\3S\3S\3S")
        buf.write("\3S\7S\u0280\nS\fS\16S\u0283\13S\3S\3S\3S\3S\3S\3T\3T")
        buf.write("\3U\3U\3U\7U\u028f\nU\fU\16U\u0292\13U\3V\3V\3V\7V\u0297")
        buf.write("\nV\fV\16V\u029a\13V\3V\3V\3W\3W\3W\3W\3W\7W\u02a3\nW")
        buf.write("\fW\16W\u02a6\13W\3W\7W\u02a9\nW\fW\16W\u02ac\13W\5W\u02ae")
        buf.write("\nW\3\u0281\2X\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66")
        buf.write("k\67m8o9q:s;u<w=y>{?}@\177A\u0081\2\u0083\2\u0085\2\u0087")
        buf.write("\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095")
        buf.write("B\u0097\2\u0099\2\u009b\2\u009dC\u009fD\u00a1E\u00a3F")
        buf.write("\u00a5G\u00a7H\u00a9I\u00abJ\u00adK\3\2\16\3\2\62;\3\2")
        buf.write("\63;\3\2c|\3\2C\\\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\3")
        buf.write("\2$$\7\2\f\f\17\17$$))^^\5\2\13\f\17\17\"\"\6\2\f\f$$")
        buf.write("))^^\3\2,,\2\u02c3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0095\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\3\u00af")
        buf.write("\3\2\2\2\5\u00bc\3\2\2\2\7\u00c9\3\2\2\2\t\u00d7\3\2\2")
        buf.write("\2\13\u00e5\3\2\2\2\r\u00f5\3\2\2\2\17\u0105\3\2\2\2\21")
        buf.write("\u0114\3\2\2\2\23\u0123\3\2\2\2\25\u0125\3\2\2\2\27\u0127")
        buf.write("\3\2\2\2\31\u0129\3\2\2\2\33\u012b\3\2\2\2\35\u012d\3")
        buf.write("\2\2\2\37\u012f\3\2\2\2!\u0131\3\2\2\2#\u0133\3\2\2\2")
        buf.write("%\u0135\3\2\2\2\'\u0137\3\2\2\2)\u013c\3\2\2\2+\u0142")
        buf.write("\3\2\2\2-\u014b\3\2\2\2/\u014e\3\2\2\2\61\u0153\3\2\2")
        buf.write("\2\63\u015a\3\2\2\2\65\u0162\3\2\2\2\67\u0168\3\2\2\2")
        buf.write("9\u016f\3\2\2\2;\u0178\3\2\2\2=\u017c\3\2\2\2?\u0185\3")
        buf.write("\2\2\2A\u0188\3\2\2\2C\u0192\3\2\2\2E\u0199\3\2\2\2G\u019e")
        buf.write("\3\2\2\2I\u01a2\3\2\2\2K\u01a8\3\2\2\2M\u01ad\3\2\2\2")
        buf.write("O\u01b3\3\2\2\2Q\u01b9\3\2\2\2S\u01bb\3\2\2\2U\u01bd\3")
        buf.write("\2\2\2W\u01bf\3\2\2\2Y\u01c1\3\2\2\2[\u01c3\3\2\2\2]\u01c6")
        buf.write("\3\2\2\2_\u01c9\3\2\2\2a\u01cc\3\2\2\2c\u01ce\3\2\2\2")
        buf.write("e\u01d0\3\2\2\2g\u01d3\3\2\2\2i\u01d6\3\2\2\2k\u01d9\3")
        buf.write("\2\2\2m\u01dc\3\2\2\2o\u01df\3\2\2\2q\u01e2\3\2\2\2s\u01e5")
        buf.write("\3\2\2\2u\u01e8\3\2\2\2w\u01ec\3\2\2\2y\u01f0\3\2\2\2")
        buf.write("{\u01f4\3\2\2\2}\u01f6\3\2\2\2\177\u01f9\3\2\2\2\u0081")
        buf.write("\u01fc\3\2\2\2\u0083\u01fe\3\2\2\2\u0085\u0200\3\2\2\2")
        buf.write("\u0087\u0202\3\2\2\2\u0089\u0204\3\2\2\2\u008b\u0206\3")
        buf.write("\2\2\2\u008d\u020d\3\2\2\2\u008f\u021a\3\2\2\2\u0091\u021c")
        buf.write("\3\2\2\2\u0093\u0223\3\2\2\2\u0095\u0225\3\2\2\2\u0097")
        buf.write("\u0233\3\2\2\2\u0099\u0239\3\2\2\2\u009b\u023d\3\2\2\2")
        buf.write("\u009d\u0257\3\2\2\2\u009f\u0261\3\2\2\2\u00a1\u026a\3")
        buf.write("\2\2\2\u00a3\u0275\3\2\2\2\u00a5\u027b\3\2\2\2\u00a7\u0289")
        buf.write("\3\2\2\2\u00a9\u028b\3\2\2\2\u00ab\u0293\3\2\2\2\u00ad")
        buf.write("\u029d\3\2\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1")
        buf.write("\u00b2\7v\2\2\u00b2\u00b3\7a\2\2\u00b3\u00b4\7q\2\2\u00b4")
        buf.write("\u00b5\7h\2\2\u00b5\u00b6\7a\2\2\u00b6\u00b7\7h\2\2\u00b7")
        buf.write("\u00b8\7n\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7c\2\2\u00ba")
        buf.write("\u00bb\7v\2\2\u00bb\4\3\2\2\2\u00bc\u00bd\7h\2\2\u00bd")
        buf.write("\u00be\7n\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7c\2\2\u00c0")
        buf.write("\u00c1\7v\2\2\u00c1\u00c2\7a\2\2\u00c2\u00c3\7v\2\2\u00c3")
        buf.write("\u00c4\7q\2\2\u00c4\u00c5\7a\2\2\u00c5\u00c6\7k\2\2\u00c6")
        buf.write("\u00c7\7p\2\2\u00c7\u00c8\7v\2\2\u00c8\6\3\2\2\2\u00c9")
        buf.write("\u00ca\7k\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7v\2\2\u00cc")
        buf.write("\u00cd\7a\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7h\2\2\u00cf")
        buf.write("\u00d0\7a\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2\7v\2\2\u00d2")
        buf.write("\u00d3\7t\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7p\2\2\u00d5")
        buf.write("\u00d6\7i\2\2\u00d6\b\3\2\2\2\u00d7\u00d8\7u\2\2\u00d8")
        buf.write("\u00d9\7v\2\2\u00d9\u00da\7t\2\2\u00da\u00db\7k\2\2\u00db")
        buf.write("\u00dc\7p\2\2\u00dc\u00dd\7i\2\2\u00dd\u00de\7a\2\2\u00de")
        buf.write("\u00df\7q\2\2\u00df\u00e0\7h\2\2\u00e0\u00e1\7a\2\2\u00e1")
        buf.write("\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7v\2\2\u00e4")
        buf.write("\n\3\2\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7\7n\2\2\u00e7")
        buf.write("\u00e8\7q\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write("\u00eb\7a\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7h\2\2\u00ed")
        buf.write("\u00ee\7a\2\2\u00ee\u00ef\7u\2\2\u00ef\u00f0\7v\2\2\u00f0")
        buf.write("\u00f1\7t\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7p\2\2\u00f3")
        buf.write("\u00f4\7i\2\2\u00f4\f\3\2\2\2\u00f5\u00f6\7u\2\2\u00f6")
        buf.write("\u00f7\7v\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7k\2\2\u00f9")
        buf.write("\u00fa\7p\2\2\u00fa\u00fb\7i\2\2\u00fb\u00fc\7a\2\2\u00fc")
        buf.write("\u00fd\7q\2\2\u00fd\u00fe\7h\2\2\u00fe\u00ff\7a\2\2\u00ff")
        buf.write("\u0100\7h\2\2\u0100\u0101\7n\2\2\u0101\u0102\7q\2\2\u0102")
        buf.write("\u0103\7c\2\2\u0103\u0104\7v\2\2\u0104\16\3\2\2\2\u0105")
        buf.write("\u0106\7d\2\2\u0106\u0107\7q\2\2\u0107\u0108\7q\2\2\u0108")
        buf.write("\u0109\7n\2\2\u0109\u010a\7a\2\2\u010a\u010b\7q\2\2\u010b")
        buf.write("\u010c\7h\2\2\u010c\u010d\7a\2\2\u010d\u010e\7u\2\2\u010e")
        buf.write("\u010f\7v\2\2\u010f\u0110\7t\2\2\u0110\u0111\7k\2\2\u0111")
        buf.write("\u0112\7p\2\2\u0112\u0113\7i\2\2\u0113\20\3\2\2\2\u0114")
        buf.write("\u0115\7u\2\2\u0115\u0116\7v\2\2\u0116\u0117\7t\2\2\u0117")
        buf.write("\u0118\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a\7i\2\2\u011a")
        buf.write("\u011b\7a\2\2\u011b\u011c\7q\2\2\u011c\u011d\7h\2\2\u011d")
        buf.write("\u011e\7a\2\2\u011e\u011f\7d\2\2\u011f\u0120\7q\2\2\u0120")
        buf.write("\u0121\7q\2\2\u0121\u0122\7n\2\2\u0122\22\3\2\2\2\u0123")
        buf.write("\u0124\7*\2\2\u0124\24\3\2\2\2\u0125\u0126\7+\2\2\u0126")
        buf.write("\26\3\2\2\2\u0127\u0128\7]\2\2\u0128\30\3\2\2\2\u0129")
        buf.write("\u012a\7_\2\2\u012a\32\3\2\2\2\u012b\u012c\7}\2\2\u012c")
        buf.write("\34\3\2\2\2\u012d\u012e\7\177\2\2\u012e\36\3\2\2\2\u012f")
        buf.write("\u0130\7<\2\2\u0130 \3\2\2\2\u0131\u0132\7=\2\2\u0132")
        buf.write("\"\3\2\2\2\u0133\u0134\7\60\2\2\u0134$\3\2\2\2\u0135\u0136")
        buf.write("\7.\2\2\u0136&\3\2\2\2\u0137\u0138\7D\2\2\u0138\u0139")
        buf.write("\7q\2\2\u0139\u013a\7f\2\2\u013a\u013b\7{\2\2\u013b(\3")
        buf.write("\2\2\2\u013c\u013d\7D\2\2\u013d\u013e\7t\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f\u0140\7c\2\2\u0140\u0141\7m\2\2\u0141*\3")
        buf.write("\2\2\2\u0142\u0143\7E\2\2\u0143\u0144\7q\2\2\u0144\u0145")
        buf.write("\7p\2\2\u0145\u0146\7v\2\2\u0146\u0147\7k\2\2\u0147\u0148")
        buf.write("\7p\2\2\u0148\u0149\7w\2\2\u0149\u014a\7g\2\2\u014a,\3")
        buf.write("\2\2\2\u014b\u014c\7F\2\2\u014c\u014d\7q\2\2\u014d.\3")
        buf.write("\2\2\2\u014e\u014f\7G\2\2\u014f\u0150\7n\2\2\u0150\u0151")
        buf.write("\7u\2\2\u0151\u0152\7g\2\2\u0152\60\3\2\2\2\u0153\u0154")
        buf.write("\7G\2\2\u0154\u0155\7n\2\2\u0155\u0156\7u\2\2\u0156\u0157")
        buf.write("\7g\2\2\u0157\u0158\7K\2\2\u0158\u0159\7h\2\2\u0159\62")
        buf.write("\3\2\2\2\u015a\u015b\7G\2\2\u015b\u015c\7p\2\2\u015c\u015d")
        buf.write("\7f\2\2\u015d\u015e\7D\2\2\u015e\u015f\7q\2\2\u015f\u0160")
        buf.write("\7f\2\2\u0160\u0161\7{\2\2\u0161\64\3\2\2\2\u0162\u0163")
        buf.write("\7G\2\2\u0163\u0164\7p\2\2\u0164\u0165\7f\2\2\u0165\u0166")
        buf.write("\7K\2\2\u0166\u0167\7h\2\2\u0167\66\3\2\2\2\u0168\u0169")
        buf.write("\7G\2\2\u0169\u016a\7p\2\2\u016a\u016b\7f\2\2\u016b\u016c")
        buf.write("\7H\2\2\u016c\u016d\7q\2\2\u016d\u016e\7t\2\2\u016e8\3")
        buf.write("\2\2\2\u016f\u0170\7G\2\2\u0170\u0171\7p\2\2\u0171\u0172")
        buf.write("\7f\2\2\u0172\u0173\7Y\2\2\u0173\u0174\7j\2\2\u0174\u0175")
        buf.write("\7k\2\2\u0175\u0176\7n\2\2\u0176\u0177\7g\2\2\u0177:\3")
        buf.write("\2\2\2\u0178\u0179\7H\2\2\u0179\u017a\7q\2\2\u017a\u017b")
        buf.write("\7t\2\2\u017b<\3\2\2\2\u017c\u017d\7H\2\2\u017d\u017e")
        buf.write("\7w\2\2\u017e\u017f\7p\2\2\u017f\u0180\7e\2\2\u0180\u0181")
        buf.write("\7v\2\2\u0181\u0182\7k\2\2\u0182\u0183\7q\2\2\u0183\u0184")
        buf.write("\7p\2\2\u0184>\3\2\2\2\u0185\u0186\7K\2\2\u0186\u0187")
        buf.write("\7h\2\2\u0187@\3\2\2\2\u0188\u0189\7R\2\2\u0189\u018a")
        buf.write("\7c\2\2\u018a\u018b\7t\2\2\u018b\u018c\7c\2\2\u018c\u018d")
        buf.write("\7o\2\2\u018d\u018e\7g\2\2\u018e\u018f\7v\2\2\u018f\u0190")
        buf.write("\7g\2\2\u0190\u0191\7t\2\2\u0191B\3\2\2\2\u0192\u0193")
        buf.write("\7T\2\2\u0193\u0194\7g\2\2\u0194\u0195\7v\2\2\u0195\u0196")
        buf.write("\7w\2\2\u0196\u0197\7t\2\2\u0197\u0198\7p\2\2\u0198D\3")
        buf.write("\2\2\2\u0199\u019a\7V\2\2\u019a\u019b\7j\2\2\u019b\u019c")
        buf.write("\7g\2\2\u019c\u019d\7p\2\2\u019dF\3\2\2\2\u019e\u019f")
        buf.write("\7X\2\2\u019f\u01a0\7c\2\2\u01a0\u01a1\7t\2\2\u01a1H\3")
        buf.write("\2\2\2\u01a2\u01a3\7Y\2\2\u01a3\u01a4\7j\2\2\u01a4\u01a5")
        buf.write("\7k\2\2\u01a5\u01a6\7n\2\2\u01a6\u01a7\7g\2\2\u01a7J\3")
        buf.write("\2\2\2\u01a8\u01a9\7V\2\2\u01a9\u01aa\7t\2\2\u01aa\u01ab")
        buf.write("\7w\2\2\u01ab\u01ac\7g\2\2\u01acL\3\2\2\2\u01ad\u01ae")
        buf.write("\7H\2\2\u01ae\u01af\7c\2\2\u01af\u01b0\7n\2\2\u01b0\u01b1")
        buf.write("\7u\2\2\u01b1\u01b2\7g\2\2\u01b2N\3\2\2\2\u01b3\u01b4")
        buf.write("\7G\2\2\u01b4\u01b5\7p\2\2\u01b5\u01b6\7f\2\2\u01b6\u01b7")
        buf.write("\7F\2\2\u01b7\u01b8\7q\2\2\u01b8P\3\2\2\2\u01b9\u01ba")
        buf.write("\7?\2\2\u01baR\3\2\2\2\u01bb\u01bc\7-\2\2\u01bcT\3\2\2")
        buf.write("\2\u01bd\u01be\7/\2\2\u01beV\3\2\2\2\u01bf\u01c0\7,\2")
        buf.write("\2\u01c0X\3\2\2\2\u01c1\u01c2\7^\2\2\u01c2Z\3\2\2\2\u01c3")
        buf.write("\u01c4\7^\2\2\u01c4\u01c5\7\'\2\2\u01c5\\\3\2\2\2\u01c6")
        buf.write("\u01c7\7?\2\2\u01c7\u01c8\7?\2\2\u01c8^\3\2\2\2\u01c9")
        buf.write("\u01ca\7#\2\2\u01ca\u01cb\7?\2\2\u01cb`\3\2\2\2\u01cc")
        buf.write("\u01cd\7@\2\2\u01cdb\3\2\2\2\u01ce\u01cf\7>\2\2\u01cf")
        buf.write("d\3\2\2\2\u01d0\u01d1\7@\2\2\u01d1\u01d2\7?\2\2\u01d2")
        buf.write("f\3\2\2\2\u01d3\u01d4\7>\2\2\u01d4\u01d5\7?\2\2\u01d5")
        buf.write("h\3\2\2\2\u01d6\u01d7\7-\2\2\u01d7\u01d8\7\60\2\2\u01d8")
        buf.write("j\3\2\2\2\u01d9\u01da\7/\2\2\u01da\u01db\7\60\2\2\u01db")
        buf.write("l\3\2\2\2\u01dc\u01dd\7,\2\2\u01dd\u01de\7\60\2\2\u01de")
        buf.write("n\3\2\2\2\u01df\u01e0\7^\2\2\u01e0\u01e1\7\60\2\2\u01e1")
        buf.write("p\3\2\2\2\u01e2\u01e3\7@\2\2\u01e3\u01e4\7\60\2\2\u01e4")
        buf.write("r\3\2\2\2\u01e5\u01e6\7>\2\2\u01e6\u01e7\7\60\2\2\u01e7")
        buf.write("t\3\2\2\2\u01e8\u01e9\7@\2\2\u01e9\u01ea\7?\2\2\u01ea")
        buf.write("\u01eb\7\60\2\2\u01ebv\3\2\2\2\u01ec\u01ed\7>\2\2\u01ed")
        buf.write("\u01ee\7?\2\2\u01ee\u01ef\7\60\2\2\u01efx\3\2\2\2\u01f0")
        buf.write("\u01f1\7?\2\2\u01f1\u01f2\7\61\2\2\u01f2\u01f3\7?\2\2")
        buf.write("\u01f3z\3\2\2\2\u01f4\u01f5\7#\2\2\u01f5|\3\2\2\2\u01f6")
        buf.write("\u01f7\7(\2\2\u01f7\u01f8\7(\2\2\u01f8~\3\2\2\2\u01f9")
        buf.write("\u01fa\7~\2\2\u01fa\u01fb\7~\2\2\u01fb\u0080\3\2\2\2\u01fc")
        buf.write("\u01fd\t\2\2\2\u01fd\u0082\3\2\2\2\u01fe\u01ff\t\3\2\2")
        buf.write("\u01ff\u0084\3\2\2\2\u0200\u0201\t\4\2\2\u0201\u0086\3")
        buf.write("\2\2\2\u0202\u0203\t\5\2\2\u0203\u0088\3\2\2\2\u0204\u0205")
        buf.write("\7a\2\2\u0205\u008a\3\2\2\2\u0206\u020a\7\60\2\2\u0207")
        buf.write("\u0209\t\2\2\2\u0208\u0207\3\2\2\2\u0209\u020c\3\2\2\2")
        buf.write("\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u008c\3")
        buf.write("\2\2\2\u020c\u020a\3\2\2\2\u020d\u020f\t\6\2\2\u020e\u0210")
        buf.write("\t\7\2\2\u020f\u020e\3\2\2\2\u020f\u0210\3\2\2\2\u0210")
        buf.write("\u0212\3\2\2\2\u0211\u0213\t\3\2\2\u0212\u0211\3\2\2\2")
        buf.write("\u0213\u0214\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215\3")
        buf.write("\2\2\2\u0215\u008e\3\2\2\2\u0216\u0217\7^\2\2\u0217\u021b")
        buf.write("\t\b\2\2\u0218\u0219\7)\2\2\u0219\u021b\7$\2\2\u021a\u0216")
        buf.write("\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u0090\3\2\2\2\u021c")
        buf.write("\u021d\t\b\2\2\u021d\u0092\3\2\2\2\u021e\u021f\7^\2\2")
        buf.write("\u021f\u0224\n\b\2\2\u0220\u0224\7^\2\2\u0221\u0222\7")
        buf.write(")\2\2\u0222\u0224\n\t\2\2\u0223\u021e\3\2\2\2\u0223\u0220")
        buf.write("\3\2\2\2\u0223\u0221\3\2\2\2\u0224\u0094\3\2\2\2\u0225")
        buf.write("\u022c\5\u0085C\2\u0226\u022b\5\u0089E\2\u0227\u022b\5")
        buf.write("\u0085C\2\u0228\u022b\5\u0087D\2\u0229\u022b\5\u0081A")
        buf.write("\2\u022a\u0226\3\2\2\2\u022a\u0227\3\2\2\2\u022a\u0228")
        buf.write("\3\2\2\2\u022a\u0229\3\2\2\2\u022b\u022e\3\2\2\2\u022c")
        buf.write("\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u0096\3\2\2\2")
        buf.write("\u022e\u022c\3\2\2\2\u022f\u0230\7\62\2\2\u0230\u0234")
        buf.write("\7z\2\2\u0231\u0232\7\62\2\2\u0232\u0234\7Z\2\2\u0233")
        buf.write("\u022f\3\2\2\2\u0233\u0231\3\2\2\2\u0234\u0098\3\2\2\2")
        buf.write("\u0235\u0236\7\62\2\2\u0236\u023a\7q\2\2\u0237\u0238\7")
        buf.write("\62\2\2\u0238\u023a\7Q\2\2\u0239\u0235\3\2\2\2\u0239\u0237")
        buf.write("\3\2\2\2\u023a\u009a\3\2\2\2\u023b\u023e\5K&\2\u023c\u023e")
        buf.write("\5M\'\2\u023d\u023b\3\2\2\2\u023d\u023c\3\2\2\2\u023e")
        buf.write("\u009c\3\2\2\2\u023f\u0258\7\62\2\2\u0240\u0244\5\u0083")
        buf.write("B\2\u0241\u0243\5\u0081A\2\u0242\u0241\3\2\2\2\u0243\u0246")
        buf.write("\3\2\2\2\u0244\u0242\3\2\2\2\u0244\u0245\3\2\2\2\u0245")
        buf.write("\u0258\3\2\2\2\u0246\u0244\3\2\2\2\u0247\u0248\5\u0097")
        buf.write("L\2\u0248\u024c\5\u0083B\2\u0249\u024b\5\u0081A\2\u024a")
        buf.write("\u0249\3\2\2\2\u024b\u024e\3\2\2\2\u024c\u024a\3\2\2\2")
        buf.write("\u024c\u024d\3\2\2\2\u024d\u0258\3\2\2\2\u024e\u024c\3")
        buf.write("\2\2\2\u024f\u0250\5\u0099M\2\u0250\u0254\5\u0083B\2\u0251")
        buf.write("\u0253\5\u0081A\2\u0252\u0251\3\2\2\2\u0253\u0256\3\2")
        buf.write("\2\2\u0254\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0258")
        buf.write("\3\2\2\2\u0256\u0254\3\2\2\2\u0257\u023f\3\2\2\2\u0257")
        buf.write("\u0240\3\2\2\2\u0257\u0247\3\2\2\2\u0257\u024f\3\2\2\2")
        buf.write("\u0258\u009e\3\2\2\2\u0259\u0262\7\62\2\2\u025a\u025e")
        buf.write("\5\u0083B\2\u025b\u025d\5\u0081A\2\u025c\u025b\3\2\2\2")
        buf.write("\u025d\u0260\3\2\2\2\u025e\u025c\3\2\2\2\u025e\u025f\3")
        buf.write("\2\2\2\u025f\u0262\3\2\2\2\u0260\u025e\3\2\2\2\u0261\u0259")
        buf.write("\3\2\2\2\u0261\u025a\3\2\2\2\u0262\u0268\3\2\2\2\u0263")
        buf.write("\u0269\5\u008bF\2\u0264\u0269\5\u008dG\2\u0265\u0266\5")
        buf.write("\u008bF\2\u0266\u0267\5\u008dG\2\u0267\u0269\3\2\2\2\u0268")
        buf.write("\u0263\3\2\2\2\u0268\u0264\3\2\2\2\u0268\u0265\3\2\2\2")
        buf.write("\u0269\u00a0\3\2\2\2\u026a\u026f\7$\2\2\u026b\u026e\n")
        buf.write("\n\2\2\u026c\u026e\5\u008fH\2\u026d\u026b\3\2\2\2\u026d")
        buf.write("\u026c\3\2\2\2\u026e\u0271\3\2\2\2\u026f\u026d\3\2\2\2")
        buf.write("\u026f\u0270\3\2\2\2\u0270\u0272\3\2\2\2\u0271\u026f\3")
        buf.write("\2\2\2\u0272\u0273\7$\2\2\u0273\u00a2\3\2\2\2\u0274\u0276")
        buf.write("\t\13\2\2\u0275\u0274\3\2\2\2\u0276\u0277\3\2\2\2\u0277")
        buf.write("\u0275\3\2\2\2\u0277\u0278\3\2\2\2\u0278\u0279\3\2\2\2")
        buf.write("\u0279\u027a\bR\2\2\u027a\u00a4\3\2\2\2\u027b\u027c\7")
        buf.write(",\2\2\u027c\u027d\7,\2\2\u027d\u0281\3\2\2\2\u027e\u0280")
        buf.write("\13\2\2\2\u027f\u027e\3\2\2\2\u0280\u0283\3\2\2\2\u0281")
        buf.write("\u0282\3\2\2\2\u0281\u027f\3\2\2\2\u0282\u0284\3\2\2\2")
        buf.write("\u0283\u0281\3\2\2\2\u0284\u0285\7,\2\2\u0285\u0286\7")
        buf.write(",\2\2\u0286\u0287\3\2\2\2\u0287\u0288\bS\2\2\u0288\u00a6")
        buf.write("\3\2\2\2\u0289\u028a\13\2\2\2\u028a\u00a8\3\2\2\2\u028b")
        buf.write("\u0290\7$\2\2\u028c\u028f\n\n\2\2\u028d\u028f\5\u008f")
        buf.write("H\2\u028e\u028c\3\2\2\2\u028e\u028d\3\2\2\2\u028f\u0292")
        buf.write("\3\2\2\2\u0290\u028e\3\2\2\2\u0290\u0291\3\2\2\2\u0291")
        buf.write("\u00aa\3\2\2\2\u0292\u0290\3\2\2\2\u0293\u0298\7$\2\2")
        buf.write("\u0294\u0297\n\f\2\2\u0295\u0297\5\u008fH\2\u0296\u0294")
        buf.write("\3\2\2\2\u0296\u0295\3\2\2\2\u0297\u029a\3\2\2\2\u0298")
        buf.write("\u0296\3\2\2\2\u0298\u0299\3\2\2\2\u0299\u029b\3\2\2\2")
        buf.write("\u029a\u0298\3\2\2\2\u029b\u029c\5\u0093J\2\u029c\u00ac")
        buf.write("\3\2\2\2\u029d\u029e\7,\2\2\u029e\u029f\7,\2\2\u029f\u02ad")
        buf.write("\3\2\2\2\u02a0\u02a1\7,\2\2\u02a1\u02a3\n\r\2\2\u02a2")
        buf.write("\u02a0\3\2\2\2\u02a3\u02a6\3\2\2\2\u02a4\u02a2\3\2\2\2")
        buf.write("\u02a4\u02a5\3\2\2\2\u02a5\u02ae\3\2\2\2\u02a6\u02a4\3")
        buf.write("\2\2\2\u02a7\u02a9\n\r\2\2\u02a8\u02a7\3\2\2\2\u02a9\u02ac")
        buf.write("\3\2\2\2\u02aa\u02a8\3\2\2\2\u02aa\u02ab\3\2\2\2\u02ab")
        buf.write("\u02ae\3\2\2\2\u02ac\u02aa\3\2\2\2\u02ad\u02a4\3\2\2\2")
        buf.write("\u02ad\u02aa\3\2\2\2\u02ae\u00ae\3\2\2\2\37\2\u020a\u020f")
        buf.write("\u0214\u021a\u0223\u022a\u022c\u0233\u0239\u023d\u0244")
        buf.write("\u024c\u0254\u0257\u025e\u0261\u0268\u026d\u026f\u0277")
        buf.write("\u0281\u028e\u0290\u0296\u0298\u02a4\u02aa\u02ad\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT_OF_FLOAT = 1
    FLOAT_TO_INT = 2
    INT_OF_STRING = 3
    STRING_OF_INT = 4
    FLOAT_OF_STRING = 5
    STRING_OF_FLOAT = 6
    BOOL_OF_STRING = 7
    STRING_OF_BOOL = 8
    LP = 9
    RP = 10
    LSB = 11
    RSB = 12
    LCB = 13
    RCB = 14
    COLON = 15
    SEMICOLON = 16
    DOT = 17
    COMMA = 18
    BODY = 19
    BREAK = 20
    CONTINUE = 21
    DO = 22
    ELSE = 23
    ELSEIF = 24
    ENDBODY = 25
    ENDIF = 26
    ENDFOR = 27
    ENDWHILE = 28
    FOR = 29
    FUNCTION = 30
    IF = 31
    PARAMETER = 32
    RETURN = 33
    THEN = 34
    VAR = 35
    WHILE = 36
    TRUE = 37
    FALSE = 38
    ENDDO = 39
    EQUAL = 40
    ADD_OP_INT = 41
    SUB_OP_INT = 42
    MUL_OP_INT = 43
    DIV_OP_INT = 44
    MOD_OP_INT = 45
    EQUAL_OP_INT = 46
    NOT_EQUAL_OP_INT = 47
    GREATER_OP_INT = 48
    LESS_OP_INT = 49
    GREATER_EQUAL_OP_INT = 50
    LESS_EQUAL_OP_INT = 51
    ADD_OP_FLOAT = 52
    SUB_OP_FLOAT = 53
    MUL_OP_FLOAT = 54
    DIV_OP_FLOAT = 55
    GREATER_OP_FLOAT = 56
    LESS_OP_FLOAT = 57
    GREATER_EQUAL_OP_FLOAT = 58
    LESS_EQUAL_OP_FLOAT = 59
    NOT_EQUAL_OP_FLOAT = 60
    NOT_OP = 61
    AND_OP = 62
    OR_OP = 63
    IDENTIFIER = 64
    INTEGER = 65
    FLOAT = 66
    STRING = 67
    WS = 68
    COMMENT = 69
    ERROR_CHAR = 70
    UNCLOSE_STRING = 71
    ILLEGAL_ESCAPE = 72
    UNTERMINATED_COMMENT = 73

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int_of_float'", "'float_to_int'", "'int_of_string'", "'string_of_int'", 
            "'float_of_string'", "'string_of_float'", "'bool_of_string'", 
            "'string_of_bool'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "':'", "';'", "'.'", "','", "'Body'", "'Break'", "'Continue'", 
            "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", 
            "'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", 
            "'Return'", "'Then'", "'Var'", "'While'", "'True'", "'False'", 
            "'EndDo'", "'='", "'+'", "'-'", "'*'", "'\\'", "'\\%'", "'=='", 
            "'!='", "'>'", "'<'", "'>='", "'<='", "'+.'", "'-.'", "'*.'", 
            "'\\.'", "'>.'", "'<.'", "'>=.'", "'<=.'", "'=/='", "'!'", "'&&'", 
            "'||'" ]

    symbolicNames = [ "<INVALID>",
            "INT_OF_FLOAT", "FLOAT_TO_INT", "INT_OF_STRING", "STRING_OF_INT", 
            "FLOAT_OF_STRING", "STRING_OF_FLOAT", "BOOL_OF_STRING", "STRING_OF_BOOL", 
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
            "OR_OP", "IDENTIFIER", "INTEGER", "FLOAT", "STRING", "WS", "COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "INT_OF_FLOAT", "FLOAT_TO_INT", "INT_OF_STRING", "STRING_OF_INT", 
                  "FLOAT_OF_STRING", "STRING_OF_FLOAT", "BOOL_OF_STRING", 
                  "STRING_OF_BOOL", "LP", "RP", "LSB", "RSB", "LCB", "RCB", 
                  "COLON", "SEMICOLON", "DOT", "COMMA", "BODY", "BREAK", 
                  "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                  "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                  "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
                  "EQUAL", "ADD_OP_INT", "SUB_OP_INT", "MUL_OP_INT", "DIV_OP_INT", 
                  "MOD_OP_INT", "EQUAL_OP_INT", "NOT_EQUAL_OP_INT", "GREATER_OP_INT", 
                  "LESS_OP_INT", "GREATER_EQUAL_OP_INT", "LESS_EQUAL_OP_INT", 
                  "ADD_OP_FLOAT", "SUB_OP_FLOAT", "MUL_OP_FLOAT", "DIV_OP_FLOAT", 
                  "GREATER_OP_FLOAT", "LESS_OP_FLOAT", "GREATER_EQUAL_OP_FLOAT", 
                  "LESS_EQUAL_OP_FLOAT", "NOT_EQUAL_OP_FLOAT", "NOT_OP", 
                  "AND_OP", "OR_OP", "DIGIT", "NZERO_DIGIT", "LOWER_LETTER", 
                  "UPPER_LETTER", "UNDERSCORE", "DECIMAL_PART", "EXPONENT_PART", 
                  "ESCAPE_SEQUENCE", "ESCAPE_CHARACTER", "ILLEGAL_ESCAPE_SQ", 
                  "IDENTIFIER", "HEXA", "OCTAL", "BOOLEAN", "INTEGER", "FLOAT", 
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


