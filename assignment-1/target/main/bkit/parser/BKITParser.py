# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3K")
        buf.write("\u01e9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\7\2")
        buf.write("\\\n\2\f\2\16\2_\13\2\3\2\7\2b\n\2\f\2\16\2e\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\5\4q\n\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4w\n\4\7\4y\n\4\f\4\16\4|\13\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\6\5\u0083\n\5\r\5\16\5\u0084\5\5\u0087\n\5\3")
        buf.write("\6\3\6\5\6\u008b\n\6\3\7\3\7\3\7\3\7\3\7\7\7\u0092\n\7")
        buf.write("\f\7\16\7\u0095\13\7\3\7\7\7\u0098\n\7\f\7\16\7\u009b")
        buf.write("\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00a5\n\b\3")
        buf.write("\t\3\t\3\t\3\t\5\t\u00ab\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\7\n\u00b4\n\n\f\n\16\n\u00b7\13\n\3\n\7\n\u00ba\n\n")
        buf.write("\f\n\16\n\u00bd\13\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\7")
        buf.write("\f\u00c6\n\f\f\f\16\f\u00c9\13\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00d4\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\7\16\u00df\n\16\f\16\16\16\u00e2")
        buf.write("\13\16\3\16\3\16\5\16\u00e6\n\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\7\21\u0103\n\21\f\21\16\21\u0106\13\21\3\21\7\21")
        buf.write("\u0109\n\21\f\21\16\21\u010c\13\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\5\24")
        buf.write("\u011c\n\24\3\24\3\24\3\24\3\25\3\25\3\25\7\25\u0124\n")
        buf.write("\25\f\25\16\25\u0127\13\25\3\26\3\26\5\26\u012b\n\26\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\5\32\u0140\n")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u016f\n\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\7\34\u017a\n\34\f\34\16\34\u017d\13")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\7\35\u018e\n\35\f\35\16\35\u0191")
        buf.write("\13\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u01a5")
        buf.write("\n\36\f\36\16\36\u01a8\13\36\3\37\3\37\3\37\5\37\u01ad")
        buf.write("\n\37\3 \3 \3 \3 \3 \5 \u01b4\n \3!\3!\3!\3!\5!\u01ba")
        buf.write("\n!\3\"\3\"\5\"\u01be\n\"\3#\3#\3#\3#\6#\u01c4\n#\r#\16")
        buf.write("#\u01c5\3$\3$\3$\5$\u01cb\n$\3$\3$\5$\u01cf\n$\3%\3%\3")
        buf.write("%\3%\3%\3%\5%\u01d7\n%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3-\2\5\668:.\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVX\2\2\2\u0201\2]\3\2\2\2\4h\3\2\2\2\6m\3\2\2\2\b\u0086")
        buf.write("\3\2\2\2\n\u008a\3\2\2\2\f\u008c\3\2\2\2\16\u00a4\3\2")
        buf.write("\2\2\20\u00a6\3\2\2\2\22\u00b5\3\2\2\2\24\u00be\3\2\2")
        buf.write("\2\26\u00c2\3\2\2\2\30\u00d3\3\2\2\2\32\u00d5\3\2\2\2")
        buf.write("\34\u00ea\3\2\2\2\36\u00f9\3\2\2\2 \u0100\3\2\2\2\"\u0112")
        buf.write("\3\2\2\2$\u0115\3\2\2\2&\u0118\3\2\2\2(\u0120\3\2\2\2")
        buf.write("*\u0128\3\2\2\2,\u012e\3\2\2\2.\u0133\3\2\2\2\60\u0137")
        buf.write("\3\2\2\2\62\u013f\3\2\2\2\64\u016e\3\2\2\2\66\u0170\3")
        buf.write("\2\2\28\u017e\3\2\2\2:\u0192\3\2\2\2<\u01ac\3\2\2\2>\u01b3")
        buf.write("\3\2\2\2@\u01b9\3\2\2\2B\u01bd\3\2\2\2D\u01c3\3\2\2\2")
        buf.write("F\u01ce\3\2\2\2H\u01d6\3\2\2\2J\u01d8\3\2\2\2L\u01da\3")
        buf.write("\2\2\2N\u01dc\3\2\2\2P\u01de\3\2\2\2R\u01e0\3\2\2\2T\u01e2")
        buf.write("\3\2\2\2V\u01e4\3\2\2\2X\u01e6\3\2\2\2Z\\\5\4\3\2[Z\3")
        buf.write("\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^c\3\2\2\2_]\3\2")
        buf.write("\2\2`b\5\20\t\2a`\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2")
        buf.write("\2df\3\2\2\2ec\3\2\2\2fg\7\2\2\3g\3\3\2\2\2hi\7%\2\2i")
        buf.write("j\7\21\2\2jk\5\6\4\2kl\7\22\2\2l\5\3\2\2\2mp\5\b\5\2n")
        buf.write("o\7*\2\2oq\5\n\6\2pn\3\2\2\2pq\3\2\2\2qz\3\2\2\2rs\7\24")
        buf.write("\2\2sv\5\b\5\2tu\7*\2\2uw\5\n\6\2vt\3\2\2\2vw\3\2\2\2")
        buf.write("wy\3\2\2\2xr\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\7")
        buf.write("\3\2\2\2|z\3\2\2\2}\u0087\7B\2\2~\u0082\7B\2\2\177\u0080")
        buf.write("\7\r\2\2\u0080\u0081\7C\2\2\u0081\u0083\7\16\2\2\u0082")
        buf.write("\177\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0087\3\2\2\2\u0086}\3\2\2\2\u0086")
        buf.write("~\3\2\2\2\u0087\t\3\2\2\2\u0088\u008b\5\16\b\2\u0089\u008b")
        buf.write("\5\f\7\2\u008a\u0088\3\2\2\2\u008a\u0089\3\2\2\2\u008b")
        buf.write("\13\3\2\2\2\u008c\u0099\7\17\2\2\u008d\u0098\5\f\7\2\u008e")
        buf.write("\u0093\5\16\b\2\u008f\u0090\7\24\2\2\u0090\u0092\5\16")
        buf.write("\b\2\u0091\u008f\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091")
        buf.write("\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0098\3\2\2\2\u0095")
        buf.write("\u0093\3\2\2\2\u0096\u0098\7\24\2\2\u0097\u008d\3\2\2")
        buf.write("\2\u0097\u008e\3\2\2\2\u0097\u0096\3\2\2\2\u0098\u009b")
        buf.write("\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\7\20\2")
        buf.write("\2\u009d\r\3\2\2\2\u009e\u00a5\7C\2\2\u009f\u00a5\7D\2")
        buf.write("\2\u00a0\u00a5\7E\2\2\u00a1\u00a5\7\'\2\2\u00a2\u00a5")
        buf.write("\7(\2\2\u00a3\u00a5\5\f\7\2\u00a4\u009e\3\2\2\2\u00a4")
        buf.write("\u009f\3\2\2\2\u00a4\u00a0\3\2\2\2\u00a4\u00a1\3\2\2\2")
        buf.write("\u00a4\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\17\3\2")
        buf.write("\2\2\u00a6\u00a7\7 \2\2\u00a7\u00a8\7\21\2\2\u00a8\u00aa")
        buf.write("\7B\2\2\u00a9\u00ab\5\24\13\2\u00aa\u00a9\3\2\2\2\u00aa")
        buf.write("\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\7\25\2")
        buf.write("\2\u00ad\u00ae\7\21\2\2\u00ae\u00af\5\22\n\2\u00af\u00b0")
        buf.write("\7\33\2\2\u00b0\u00b1\7\23\2\2\u00b1\21\3\2\2\2\u00b2")
        buf.write("\u00b4\5,\27\2\u00b3\u00b2\3\2\2\2\u00b4\u00b7\3\2\2\2")
        buf.write("\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00bb\3")
        buf.write("\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00ba\5\30\r\2\u00b9")
        buf.write("\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2")
        buf.write("\u00bb\u00bc\3\2\2\2\u00bc\23\3\2\2\2\u00bd\u00bb\3\2")
        buf.write("\2\2\u00be\u00bf\7\"\2\2\u00bf\u00c0\7\21\2\2\u00c0\u00c1")
        buf.write("\5\26\f\2\u00c1\25\3\2\2\2\u00c2\u00c7\5\b\5\2\u00c3\u00c4")
        buf.write("\7\24\2\2\u00c4\u00c6\5\b\5\2\u00c5\u00c3\3\2\2\2\u00c6")
        buf.write("\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\27\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00d4\5\60")
        buf.write("\31\2\u00cb\u00d4\5\32\16\2\u00cc\u00d4\5\34\17\2\u00cd")
        buf.write("\u00d4\5\36\20\2\u00ce\u00d4\5 \21\2\u00cf\u00d4\5\"\22")
        buf.write("\2\u00d0\u00d4\5$\23\2\u00d1\u00d4\5&\24\2\u00d2\u00d4")
        buf.write("\5*\26\2\u00d3\u00ca\3\2\2\2\u00d3\u00cb\3\2\2\2\u00d3")
        buf.write("\u00cc\3\2\2\2\u00d3\u00cd\3\2\2\2\u00d3\u00ce\3\2\2\2")
        buf.write("\u00d3\u00cf\3\2\2\2\u00d3\u00d0\3\2\2\2\u00d3\u00d1\3")
        buf.write("\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\31\3\2\2\2\u00d5\u00d6")
        buf.write("\7!\2\2\u00d6\u00d7\5\64\33\2\u00d7\u00d8\7$\2\2\u00d8")
        buf.write("\u00e0\5\22\n\2\u00d9\u00da\7\32\2\2\u00da\u00db\5\64")
        buf.write("\33\2\u00db\u00dc\7$\2\2\u00dc\u00dd\5\22\n\2\u00dd\u00df")
        buf.write("\3\2\2\2\u00de\u00d9\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0")
        buf.write("\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e5\3\2\2\2")
        buf.write("\u00e2\u00e0\3\2\2\2\u00e3\u00e4\7\31\2\2\u00e4\u00e6")
        buf.write("\5\22\n\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\u00e8\7\34\2\2\u00e8\u00e9\7\23\2")
        buf.write("\2\u00e9\33\3\2\2\2\u00ea\u00eb\7\37\2\2\u00eb\u00ec\7")
        buf.write("\13\2\2\u00ec\u00ed\7B\2\2\u00ed\u00ee\7*\2\2\u00ee\u00ef")
        buf.write("\5\64\33\2\u00ef\u00f0\7\24\2\2\u00f0\u00f1\5\64\33\2")
        buf.write("\u00f1\u00f2\7\24\2\2\u00f2\u00f3\5\64\33\2\u00f3\u00f4")
        buf.write("\7\f\2\2\u00f4\u00f5\7\30\2\2\u00f5\u00f6\5\22\n\2\u00f6")
        buf.write("\u00f7\7\35\2\2\u00f7\u00f8\7\23\2\2\u00f8\35\3\2\2\2")
        buf.write("\u00f9\u00fa\7&\2\2\u00fa\u00fb\5\64\33\2\u00fb\u00fc")
        buf.write("\7\30\2\2\u00fc\u00fd\5\22\n\2\u00fd\u00fe\7\36\2\2\u00fe")
        buf.write("\u00ff\7\23\2\2\u00ff\37\3\2\2\2\u0100\u0104\7\30\2\2")
        buf.write("\u0101\u0103\5,\27\2\u0102\u0101\3\2\2\2\u0103\u0106\3")
        buf.write("\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u010a")
        buf.write("\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0109\5\30\r\2\u0108")
        buf.write("\u0107\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2")
        buf.write("\u010a\u010b\3\2\2\2\u010b\u010d\3\2\2\2\u010c\u010a\3")
        buf.write("\2\2\2\u010d\u010e\7&\2\2\u010e\u010f\5\64\33\2\u010f")
        buf.write("\u0110\7)\2\2\u0110\u0111\7\23\2\2\u0111!\3\2\2\2\u0112")
        buf.write("\u0113\7\26\2\2\u0113\u0114\7\22\2\2\u0114#\3\2\2\2\u0115")
        buf.write("\u0116\7\27\2\2\u0116\u0117\7\22\2\2\u0117%\3\2\2\2\u0118")
        buf.write("\u0119\7B\2\2\u0119\u011b\7\13\2\2\u011a\u011c\5(\25\2")
        buf.write("\u011b\u011a\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d\3")
        buf.write("\2\2\2\u011d\u011e\7\f\2\2\u011e\u011f\7\22\2\2\u011f")
        buf.write("\'\3\2\2\2\u0120\u0125\5\64\33\2\u0121\u0122\7\24\2\2")
        buf.write("\u0122\u0124\5\64\33\2\u0123\u0121\3\2\2\2\u0124\u0127")
        buf.write("\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write(")\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u012a\7#\2\2\u0129")
        buf.write("\u012b\5\64\33\2\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2")
        buf.write("\2\u012b\u012c\3\2\2\2\u012c\u012d\7\22\2\2\u012d+\3\2")
        buf.write("\2\2\u012e\u012f\7%\2\2\u012f\u0130\7\21\2\2\u0130\u0131")
        buf.write("\5\6\4\2\u0131\u0132\7\22\2\2\u0132-\3\2\2\2\u0133\u0134")
        buf.write("\5\62\32\2\u0134\u0135\7*\2\2\u0135\u0136\5\64\33\2\u0136")
        buf.write("/\3\2\2\2\u0137\u0138\5\62\32\2\u0138\u0139\7*\2\2\u0139")
        buf.write("\u013a\5\64\33\2\u013a\u013b\7\22\2\2\u013b\61\3\2\2\2")
        buf.write("\u013c\u0140\7B\2\2\u013d\u013e\7B\2\2\u013e\u0140\5D")
        buf.write("#\2\u013f\u013c\3\2\2\2\u013f\u013d\3\2\2\2\u0140\63\3")
        buf.write("\2\2\2\u0141\u0142\5\66\34\2\u0142\u0143\7\60\2\2\u0143")
        buf.write("\u0144\5\66\34\2\u0144\u016f\3\2\2\2\u0145\u0146\5\66")
        buf.write("\34\2\u0146\u0147\7\61\2\2\u0147\u0148\5\66\34\2\u0148")
        buf.write("\u016f\3\2\2\2\u0149\u014a\5\66\34\2\u014a\u014b\7\63")
        buf.write("\2\2\u014b\u014c\5\66\34\2\u014c\u016f\3\2\2\2\u014d\u014e")
        buf.write("\5\66\34\2\u014e\u014f\7\62\2\2\u014f\u0150\5\66\34\2")
        buf.write("\u0150\u016f\3\2\2\2\u0151\u0152\5\66\34\2\u0152\u0153")
        buf.write("\7\65\2\2\u0153\u0154\5\66\34\2\u0154\u016f\3\2\2\2\u0155")
        buf.write("\u0156\5\66\34\2\u0156\u0157\7\64\2\2\u0157\u0158\5\66")
        buf.write("\34\2\u0158\u016f\3\2\2\2\u0159\u015a\5\66\34\2\u015a")
        buf.write("\u015b\7>\2\2\u015b\u015c\5\66\34\2\u015c\u016f\3\2\2")
        buf.write("\2\u015d\u015e\5\66\34\2\u015e\u015f\7;\2\2\u015f\u0160")
        buf.write("\5\66\34\2\u0160\u016f\3\2\2\2\u0161\u0162\5\66\34\2\u0162")
        buf.write("\u0163\7:\2\2\u0163\u0164\5\66\34\2\u0164\u016f\3\2\2")
        buf.write("\2\u0165\u0166\5\66\34\2\u0166\u0167\7=\2\2\u0167\u0168")
        buf.write("\5\66\34\2\u0168\u016f\3\2\2\2\u0169\u016a\5\66\34\2\u016a")
        buf.write("\u016b\7<\2\2\u016b\u016c\5\66\34\2\u016c\u016f\3\2\2")
        buf.write("\2\u016d\u016f\5\66\34\2\u016e\u0141\3\2\2\2\u016e\u0145")
        buf.write("\3\2\2\2\u016e\u0149\3\2\2\2\u016e\u014d\3\2\2\2\u016e")
        buf.write("\u0151\3\2\2\2\u016e\u0155\3\2\2\2\u016e\u0159\3\2\2\2")
        buf.write("\u016e\u015d\3\2\2\2\u016e\u0161\3\2\2\2\u016e\u0165\3")
        buf.write("\2\2\2\u016e\u0169\3\2\2\2\u016e\u016d\3\2\2\2\u016f\65")
        buf.write("\3\2\2\2\u0170\u0171\b\34\1\2\u0171\u0172\58\35\2\u0172")
        buf.write("\u017b\3\2\2\2\u0173\u0174\f\5\2\2\u0174\u0175\7@\2\2")
        buf.write("\u0175\u017a\58\35\2\u0176\u0177\f\4\2\2\u0177\u0178\7")
        buf.write("A\2\2\u0178\u017a\58\35\2\u0179\u0173\3\2\2\2\u0179\u0176")
        buf.write("\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b")
        buf.write("\u017c\3\2\2\2\u017c\67\3\2\2\2\u017d\u017b\3\2\2\2\u017e")
        buf.write("\u017f\b\35\1\2\u017f\u0180\5:\36\2\u0180\u018f\3\2\2")
        buf.write("\2\u0181\u0182\f\7\2\2\u0182\u0183\7+\2\2\u0183\u018e")
        buf.write("\5:\36\2\u0184\u0185\f\6\2\2\u0185\u0186\7,\2\2\u0186")
        buf.write("\u018e\5:\36\2\u0187\u0188\f\5\2\2\u0188\u0189\7\66\2")
        buf.write("\2\u0189\u018e\5:\36\2\u018a\u018b\f\4\2\2\u018b\u018c")
        buf.write("\7\67\2\2\u018c\u018e\5:\36\2\u018d\u0181\3\2\2\2\u018d")
        buf.write("\u0184\3\2\2\2\u018d\u0187\3\2\2\2\u018d\u018a\3\2\2\2")
        buf.write("\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3")
        buf.write("\2\2\2\u01909\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0193")
        buf.write("\b\36\1\2\u0193\u0194\5<\37\2\u0194\u01a6\3\2\2\2\u0195")
        buf.write("\u0196\f\b\2\2\u0196\u0197\7-\2\2\u0197\u01a5\5<\37\2")
        buf.write("\u0198\u0199\f\7\2\2\u0199\u019a\7.\2\2\u019a\u01a5\5")
        buf.write("<\37\2\u019b\u019c\f\6\2\2\u019c\u019d\7/\2\2\u019d\u01a5")
        buf.write("\5<\37\2\u019e\u019f\f\5\2\2\u019f\u01a0\78\2\2\u01a0")
        buf.write("\u01a5\5<\37\2\u01a1\u01a2\f\4\2\2\u01a2\u01a3\79\2\2")
        buf.write("\u01a3\u01a5\5<\37\2\u01a4\u0195\3\2\2\2\u01a4\u0198\3")
        buf.write("\2\2\2\u01a4\u019b\3\2\2\2\u01a4\u019e\3\2\2\2\u01a4\u01a1")
        buf.write("\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6")
        buf.write("\u01a7\3\2\2\2\u01a7;\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9")
        buf.write("\u01aa\7?\2\2\u01aa\u01ad\5<\37\2\u01ab\u01ad\5> \2\u01ac")
        buf.write("\u01a9\3\2\2\2\u01ac\u01ab\3\2\2\2\u01ad=\3\2\2\2\u01ae")
        buf.write("\u01af\7,\2\2\u01af\u01b4\5> \2\u01b0\u01b1\7\67\2\2\u01b1")
        buf.write("\u01b4\5> \2\u01b2\u01b4\5@!\2\u01b3\u01ae\3\2\2\2\u01b3")
        buf.write("\u01b0\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4?\3\2\2\2\u01b5")
        buf.write("\u01b6\5B\"\2\u01b6\u01b7\5D#\2\u01b7\u01ba\3\2\2\2\u01b8")
        buf.write("\u01ba\5F$\2\u01b9\u01b5\3\2\2\2\u01b9\u01b8\3\2\2\2\u01ba")
        buf.write("A\3\2\2\2\u01bb\u01be\7B\2\2\u01bc\u01be\5F$\2\u01bd\u01bb")
        buf.write("\3\2\2\2\u01bd\u01bc\3\2\2\2\u01beC\3\2\2\2\u01bf\u01c0")
        buf.write("\7\r\2\2\u01c0\u01c1\5\64\33\2\u01c1\u01c2\7\16\2\2\u01c2")
        buf.write("\u01c4\3\2\2\2\u01c3\u01bf\3\2\2\2\u01c4\u01c5\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6E\3\2\2")
        buf.write("\2\u01c7\u01c8\7B\2\2\u01c8\u01ca\7\13\2\2\u01c9\u01cb")
        buf.write("\5(\25\2\u01ca\u01c9\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb")
        buf.write("\u01cc\3\2\2\2\u01cc\u01cf\7\f\2\2\u01cd\u01cf\5H%\2\u01ce")
        buf.write("\u01c7\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cfG\3\2\2\2\u01d0")
        buf.write("\u01d7\5\16\b\2\u01d1\u01d7\7B\2\2\u01d2\u01d3\7\13\2")
        buf.write("\2\u01d3\u01d4\5\64\33\2\u01d4\u01d5\7\f\2\2\u01d5\u01d7")
        buf.write("\3\2\2\2\u01d6\u01d0\3\2\2\2\u01d6\u01d1\3\2\2\2\u01d6")
        buf.write("\u01d2\3\2\2\2\u01d7I\3\2\2\2\u01d8\u01d9\7\3\2\2\u01d9")
        buf.write("K\3\2\2\2\u01da\u01db\7\4\2\2\u01dbM\3\2\2\2\u01dc\u01dd")
        buf.write("\7\5\2\2\u01ddO\3\2\2\2\u01de\u01df\7\6\2\2\u01dfQ\3\2")
        buf.write("\2\2\u01e0\u01e1\7\7\2\2\u01e1S\3\2\2\2\u01e2\u01e3\7")
        buf.write("\b\2\2\u01e3U\3\2\2\2\u01e4\u01e5\7\t\2\2\u01e5W\3\2\2")
        buf.write("\2\u01e6\u01e7\7\n\2\2\u01e7Y\3\2\2\2*]cpvz\u0084\u0086")
        buf.write("\u008a\u0093\u0097\u0099\u00a4\u00aa\u00b5\u00bb\u00c7")
        buf.write("\u00d3\u00e0\u00e5\u0104\u010a\u011b\u0125\u012a\u013f")
        buf.write("\u016e\u0179\u017b\u018d\u018f\u01a4\u01a6\u01ac\u01b3")
        buf.write("\u01b9\u01bd\u01c5\u01ca\u01ce\u01d6")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int_of_float'", "'float_to_int'", "'int_of_string'", 
                     "'string_of_int'", "'float_of_string'", "'string_of_float'", 
                     "'bool_of_string'", "'string_of_bool'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "':'", "';'", "'.'", "','", 
                     "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
                     "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
                     "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", 
                     "'Then'", "'Var'", "'While'", "'True'", "'False'", 
                     "'EndDo'", "'='", "'+'", "'-'", "'*'", "'\\'", "'\\%'", 
                     "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'+.'", 
                     "'-.'", "'*.'", "'\\.'", "'>.'", "'<.'", "'>=.'", "'<=.'", 
                     "'=/='", "'!'", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "LP", "RP", "LSB", "RSB", "LCB", "RCB", 
                      "COLON", "SEMICOLON", "DOT", "COMMA", "BODY", "BREAK", 
                      "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                      "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", 
                      "ENDDO", "EQUAL", "ADD_OP_INT", "SUB_OP_INT", "MUL_OP_INT", 
                      "DIV_OP_INT", "MOD_OP_INT", "EQUAL_OP_INT", "NOT_EQUAL_OP_INT", 
                      "GREATER_OP_INT", "LESS_OP_INT", "GREATER_EQUAL_OP_INT", 
                      "LESS_EQUAL_OP_INT", "ADD_OP_FLOAT", "SUB_OP_FLOAT", 
                      "MUL_OP_FLOAT", "DIV_OP_FLOAT", "GREATER_OP_FLOAT", 
                      "LESS_OP_FLOAT", "GREATER_EQUAL_OP_FLOAT", "LESS_EQUAL_OP_FLOAT", 
                      "NOT_EQUAL_OP_FLOAT", "NOT_OP", "AND_OP", "OR_OP", 
                      "IDENTIFIER", "INTEGER", "FLOAT", "STRING", "WS", 
                      "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_glo_variable_dec = 1
    RULE_list_var = 2
    RULE_variable_id = 3
    RULE_value = 4
    RULE_array = 5
    RULE_primary_type = 6
    RULE_function_dec = 7
    RULE_list_sta = 8
    RULE_parameter_dec = 9
    RULE_list_param = 10
    RULE_statement = 11
    RULE_if_sta = 12
    RULE_for_sta = 13
    RULE_while_sta = 14
    RULE_do_while_sta = 15
    RULE_break_sta = 16
    RULE_continue_sta = 17
    RULE_call_sta = 18
    RULE_list_exp = 19
    RULE_return_sta = 20
    RULE_variable_dec = 21
    RULE_assignment_exp = 22
    RULE_assignment_sta = 23
    RULE_left_operand = 24
    RULE_exp = 25
    RULE_exp1 = 26
    RULE_exp2 = 27
    RULE_exp3 = 28
    RULE_exp4 = 29
    RULE_exp5 = 30
    RULE_exp6 = 31
    RULE_name_var = 32
    RULE_index_operators = 33
    RULE_exp7 = 34
    RULE_exp8 = 35
    RULE_int_of_float = 36
    RULE_float_to_int = 37
    RULE_int_of_string = 38
    RULE_string_of_int = 39
    RULE_float_of_string = 40
    RULE_string_of_float = 41
    RULE_bool_of_string = 42
    RULE_string_of_bool = 43

    ruleNames =  [ "program", "glo_variable_dec", "list_var", "variable_id", 
                   "value", "array", "primary_type", "function_dec", "list_sta", 
                   "parameter_dec", "list_param", "statement", "if_sta", 
                   "for_sta", "while_sta", "do_while_sta", "break_sta", 
                   "continue_sta", "call_sta", "list_exp", "return_sta", 
                   "variable_dec", "assignment_exp", "assignment_sta", "left_operand", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "name_var", "index_operators", "exp7", "exp8", "int_of_float", 
                   "float_to_int", "int_of_string", "string_of_int", "float_of_string", 
                   "string_of_float", "bool_of_string", "string_of_bool" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    LP=9
    RP=10
    LSB=11
    RSB=12
    LCB=13
    RCB=14
    COLON=15
    SEMICOLON=16
    DOT=17
    COMMA=18
    BODY=19
    BREAK=20
    CONTINUE=21
    DO=22
    ELSE=23
    ELSEIF=24
    ENDBODY=25
    ENDIF=26
    ENDFOR=27
    ENDWHILE=28
    FOR=29
    FUNCTION=30
    IF=31
    PARAMETER=32
    RETURN=33
    THEN=34
    VAR=35
    WHILE=36
    TRUE=37
    FALSE=38
    ENDDO=39
    EQUAL=40
    ADD_OP_INT=41
    SUB_OP_INT=42
    MUL_OP_INT=43
    DIV_OP_INT=44
    MOD_OP_INT=45
    EQUAL_OP_INT=46
    NOT_EQUAL_OP_INT=47
    GREATER_OP_INT=48
    LESS_OP_INT=49
    GREATER_EQUAL_OP_INT=50
    LESS_EQUAL_OP_INT=51
    ADD_OP_FLOAT=52
    SUB_OP_FLOAT=53
    MUL_OP_FLOAT=54
    DIV_OP_FLOAT=55
    GREATER_OP_FLOAT=56
    LESS_OP_FLOAT=57
    GREATER_EQUAL_OP_FLOAT=58
    LESS_EQUAL_OP_FLOAT=59
    NOT_EQUAL_OP_FLOAT=60
    NOT_OP=61
    AND_OP=62
    OR_OP=63
    IDENTIFIER=64
    INTEGER=65
    FLOAT=66
    STRING=67
    WS=68
    COMMENT=69
    ERROR_CHAR=70
    UNCLOSE_STRING=71
    ILLEGAL_ESCAPE=72
    UNTERMINATED_COMMENT=73

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def glo_variable_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Glo_variable_decContext)
            else:
                return self.getTypedRuleContext(BKITParser.Glo_variable_decContext,i)


        def function_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Function_decContext)
            else:
                return self.getTypedRuleContext(BKITParser.Function_decContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 88
                self.glo_variable_dec()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 94
                self.function_dec()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Glo_variable_decContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def list_var(self):
            return self.getTypedRuleContext(BKITParser.List_varContext,0)


        def SEMICOLON(self):
            return self.getToken(BKITParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_glo_variable_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlo_variable_dec" ):
                return visitor.visitGlo_variable_dec(self)
            else:
                return visitor.visitChildren(self)




    def glo_variable_dec(self):

        localctx = BKITParser.Glo_variable_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_glo_variable_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(BKITParser.VAR)
            self.state = 103
            self.match(BKITParser.COLON)
            self.state = 104
            self.list_var()
            self.state = 105
            self.match(BKITParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_idContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_idContext,i)


        def EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.EQUAL)
            else:
                return self.getToken(BKITParser.EQUAL, i)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ValueContext)
            else:
                return self.getTypedRuleContext(BKITParser.ValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_list_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_var" ):
                return visitor.visitList_var(self)
            else:
                return visitor.visitChildren(self)




    def list_var(self):

        localctx = BKITParser.List_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.variable_id()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.EQUAL:
                self.state = 108
                self.match(BKITParser.EQUAL)
                self.state = 109
                self.value()


            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 112
                self.match(BKITParser.COMMA)
                self.state = 113
                self.variable_id()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKITParser.EQUAL:
                    self.state = 114
                    self.match(BKITParser.EQUAL)
                    self.state = 115
                    self.value()


                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INTEGER)
            else:
                return self.getToken(BKITParser.INTEGER, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_variable_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_id" ):
                return visitor.visitVariable_id(self)
            else:
                return visitor.visitChildren(self)




    def variable_id(self):

        localctx = BKITParser.Variable_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_id)
        self._la = 0 # Token type
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(BKITParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(BKITParser.IDENTIFIER)
                self.state = 128 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 125
                    self.match(BKITParser.LSB)
                    self.state = 126
                    self.match(BKITParser.INTEGER)
                    self.state = 127
                    self.match(BKITParser.RSB)
                    self.state = 130 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BKITParser.LSB):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_type(self):
            return self.getTypedRuleContext(BKITParser.Primary_typeContext,0)


        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = BKITParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.primary_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKITParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKITParser.RCB, 0)

        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ArrayContext)
            else:
                return self.getTypedRuleContext(BKITParser.ArrayContext,i)


        def primary_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Primary_typeContext)
            else:
                return self.getTypedRuleContext(BKITParser.Primary_typeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(BKITParser.LCB)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 13)) & ~0x3f) == 0 and ((1 << (_la - 13)) & ((1 << (BKITParser.LCB - 13)) | (1 << (BKITParser.COMMA - 13)) | (1 << (BKITParser.TRUE - 13)) | (1 << (BKITParser.FALSE - 13)) | (1 << (BKITParser.INTEGER - 13)) | (1 << (BKITParser.FLOAT - 13)) | (1 << (BKITParser.STRING - 13)))) != 0):
                self.state = 149
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 139
                    self.array()
                    pass

                elif la_ == 2:
                    self.state = 140
                    self.primary_type()
                    self.state = 145
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 141
                            self.match(BKITParser.COMMA)
                            self.state = 142
                            self.primary_type() 
                        self.state = 147
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                    pass

                elif la_ == 3:
                    self.state = 148
                    self.match(BKITParser.COMMA)
                    pass


                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self.match(BKITParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_primary_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_type" ):
                return visitor.visitPrimary_type(self)
            else:
                return visitor.visitChildren(self)




    def primary_type(self):

        localctx = BKITParser.Primary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_primary_type)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(BKITParser.INTEGER)
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.match(BKITParser.STRING)
                pass
            elif token in [BKITParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 159
                self.match(BKITParser.TRUE)
                pass
            elif token in [BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 160
                self.match(BKITParser.FALSE)
                pass
            elif token in [BKITParser.LCB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 161
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_decContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COLON)
            else:
                return self.getToken(BKITParser.COLON, i)

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def list_sta(self):
            return self.getTypedRuleContext(BKITParser.List_staContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def parameter_dec(self):
            return self.getTypedRuleContext(BKITParser.Parameter_decContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_dec" ):
                return visitor.visitFunction_dec(self)
            else:
                return visitor.visitChildren(self)




    def function_dec(self):

        localctx = BKITParser.Function_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(BKITParser.FUNCTION)
            self.state = 165
            self.match(BKITParser.COLON)
            self.state = 166
            self.match(BKITParser.IDENTIFIER)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 167
                self.parameter_dec()


            self.state = 170
            self.match(BKITParser.BODY)
            self.state = 171
            self.match(BKITParser.COLON)
            self.state = 172
            self.list_sta()
            self.state = 173
            self.match(BKITParser.ENDBODY)
            self.state = 174
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_staContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_decContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_decContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_list_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_sta" ):
                return visitor.visitList_sta(self)
            else:
                return visitor.visitChildren(self)




    def list_sta(self):

        localctx = BKITParser.List_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_sta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 176
                self.variable_dec()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (BKITParser.BREAK - 20)) | (1 << (BKITParser.CONTINUE - 20)) | (1 << (BKITParser.DO - 20)) | (1 << (BKITParser.FOR - 20)) | (1 << (BKITParser.IF - 20)) | (1 << (BKITParser.RETURN - 20)) | (1 << (BKITParser.WHILE - 20)) | (1 << (BKITParser.IDENTIFIER - 20)))) != 0):
                self.state = 182
                self.statement()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_decContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def list_param(self):
            return self.getTypedRuleContext(BKITParser.List_paramContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_parameter_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_dec" ):
                return visitor.visitParameter_dec(self)
            else:
                return visitor.visitChildren(self)




    def parameter_dec(self):

        localctx = BKITParser.Parameter_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameter_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(BKITParser.PARAMETER)
            self.state = 189
            self.match(BKITParser.COLON)
            self.state = 190
            self.list_param()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_idContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_idContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_list_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_param" ):
                return visitor.visitList_param(self)
            else:
                return visitor.visitChildren(self)




    def list_param(self):

        localctx = BKITParser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.variable_id()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 193
                self.match(BKITParser.COMMA)
                self.state = 194
                self.variable_id()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_sta(self):
            return self.getTypedRuleContext(BKITParser.Assignment_staContext,0)


        def if_sta(self):
            return self.getTypedRuleContext(BKITParser.If_staContext,0)


        def for_sta(self):
            return self.getTypedRuleContext(BKITParser.For_staContext,0)


        def while_sta(self):
            return self.getTypedRuleContext(BKITParser.While_staContext,0)


        def do_while_sta(self):
            return self.getTypedRuleContext(BKITParser.Do_while_staContext,0)


        def break_sta(self):
            return self.getTypedRuleContext(BKITParser.Break_staContext,0)


        def continue_sta(self):
            return self.getTypedRuleContext(BKITParser.Continue_staContext,0)


        def call_sta(self):
            return self.getTypedRuleContext(BKITParser.Call_staContext,0)


        def return_sta(self):
            return self.getTypedRuleContext(BKITParser.Return_staContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKITParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.assignment_sta()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.if_sta()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.for_sta()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 203
                self.while_sta()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 204
                self.do_while_sta()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 205
                self.break_sta()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 206
                self.continue_sta()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 207
                self.call_sta()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 208
                self.return_sta()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_staContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def list_sta(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.List_staContext)
            else:
                return self.getTypedRuleContext(BKITParser.List_staContext,i)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ELSEIF)
            else:
                return self.getToken(BKITParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_sta" ):
                return visitor.visitIf_sta(self)
            else:
                return visitor.visitChildren(self)




    def if_sta(self):

        localctx = BKITParser.If_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if_sta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(BKITParser.IF)
            self.state = 212
            self.exp()
            self.state = 213
            self.match(BKITParser.THEN)
            self.state = 214
            self.list_sta()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 215
                self.match(BKITParser.ELSEIF)
                self.state = 216
                self.exp()
                self.state = 217
                self.match(BKITParser.THEN)
                self.state = 218
                self.list_sta()
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 225
                self.match(BKITParser.ELSE)
                self.state = 226
                self.list_sta()


            self.state = 229
            self.match(BKITParser.ENDIF)
            self.state = 230
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_staContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def list_sta(self):
            return self.getTypedRuleContext(BKITParser.List_staContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_sta" ):
                return visitor.visitFor_sta(self)
            else:
                return visitor.visitChildren(self)




    def for_sta(self):

        localctx = BKITParser.For_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_for_sta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(BKITParser.FOR)
            self.state = 233
            self.match(BKITParser.LP)
            self.state = 234
            self.match(BKITParser.IDENTIFIER)
            self.state = 235
            self.match(BKITParser.EQUAL)
            self.state = 236
            self.exp()
            self.state = 237
            self.match(BKITParser.COMMA)
            self.state = 238
            self.exp()
            self.state = 239
            self.match(BKITParser.COMMA)
            self.state = 240
            self.exp()
            self.state = 241
            self.match(BKITParser.RP)
            self.state = 242
            self.match(BKITParser.DO)
            self.state = 243
            self.list_sta()
            self.state = 244
            self.match(BKITParser.ENDFOR)
            self.state = 245
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_staContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def list_sta(self):
            return self.getTypedRuleContext(BKITParser.List_staContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_sta" ):
                return visitor.visitWhile_sta(self)
            else:
                return visitor.visitChildren(self)




    def while_sta(self):

        localctx = BKITParser.While_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_while_sta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(BKITParser.WHILE)
            self.state = 248
            self.exp()
            self.state = 249
            self.match(BKITParser.DO)
            self.state = 250
            self.list_sta()
            self.state = 251
            self.match(BKITParser.ENDWHILE)
            self.state = 252
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_staContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def variable_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_decContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_decContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_do_while_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_sta" ):
                return visitor.visitDo_while_sta(self)
            else:
                return visitor.visitChildren(self)




    def do_while_sta(self):

        localctx = BKITParser.Do_while_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_do_while_sta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(BKITParser.DO)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 255
                self.variable_dec()
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 264
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 261
                    self.statement() 
                self.state = 266
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 267
            self.match(BKITParser.WHILE)
            self.state = 268
            self.exp()
            self.state = 269
            self.match(BKITParser.ENDDO)
            self.state = 270
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_staContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(BKITParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_sta" ):
                return visitor.visitBreak_sta(self)
            else:
                return visitor.visitChildren(self)




    def break_sta(self):

        localctx = BKITParser.Break_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_break_sta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(BKITParser.BREAK)
            self.state = 273
            self.match(BKITParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_staContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(BKITParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_sta" ):
                return visitor.visitContinue_sta(self)
            else:
                return visitor.visitChildren(self)




    def continue_sta(self):

        localctx = BKITParser.Continue_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_continue_sta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(BKITParser.CONTINUE)
            self.state = 276
            self.match(BKITParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_staContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def SEMICOLON(self):
            return self.getToken(BKITParser.SEMICOLON, 0)

        def list_exp(self):
            return self.getTypedRuleContext(BKITParser.List_expContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_sta" ):
                return visitor.visitCall_sta(self)
            else:
                return visitor.visitChildren(self)




    def call_sta(self):

        localctx = BKITParser.Call_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_call_sta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(BKITParser.IDENTIFIER)
            self.state = 279
            self.match(BKITParser.LP)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (BKITParser.LP - 9)) | (1 << (BKITParser.LCB - 9)) | (1 << (BKITParser.TRUE - 9)) | (1 << (BKITParser.FALSE - 9)) | (1 << (BKITParser.SUB_OP_INT - 9)) | (1 << (BKITParser.SUB_OP_FLOAT - 9)) | (1 << (BKITParser.NOT_OP - 9)) | (1 << (BKITParser.IDENTIFIER - 9)) | (1 << (BKITParser.INTEGER - 9)) | (1 << (BKITParser.FLOAT - 9)) | (1 << (BKITParser.STRING - 9)))) != 0):
                self.state = 280
                self.list_exp()


            self.state = 283
            self.match(BKITParser.RP)
            self.state = 284
            self.match(BKITParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_list_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_exp" ):
                return visitor.visitList_exp(self)
            else:
                return visitor.visitChildren(self)




    def list_exp(self):

        localctx = BKITParser.List_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_list_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.exp()
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 287
                self.match(BKITParser.COMMA)
                self.state = 288
                self.exp()
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_staContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(BKITParser.SEMICOLON, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_sta" ):
                return visitor.visitReturn_sta(self)
            else:
                return visitor.visitChildren(self)




    def return_sta(self):

        localctx = BKITParser.Return_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_return_sta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(BKITParser.RETURN)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (BKITParser.LP - 9)) | (1 << (BKITParser.LCB - 9)) | (1 << (BKITParser.TRUE - 9)) | (1 << (BKITParser.FALSE - 9)) | (1 << (BKITParser.SUB_OP_INT - 9)) | (1 << (BKITParser.SUB_OP_FLOAT - 9)) | (1 << (BKITParser.NOT_OP - 9)) | (1 << (BKITParser.IDENTIFIER - 9)) | (1 << (BKITParser.INTEGER - 9)) | (1 << (BKITParser.FLOAT - 9)) | (1 << (BKITParser.STRING - 9)))) != 0):
                self.state = 295
                self.exp()


            self.state = 298
            self.match(BKITParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_decContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def list_var(self):
            return self.getTypedRuleContext(BKITParser.List_varContext,0)


        def SEMICOLON(self):
            return self.getToken(BKITParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_variable_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_dec" ):
                return visitor.visitVariable_dec(self)
            else:
                return visitor.visitChildren(self)




    def variable_dec(self):

        localctx = BKITParser.Variable_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_variable_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(BKITParser.VAR)
            self.state = 301
            self.match(BKITParser.COLON)
            self.state = 302
            self.list_var()
            self.state = 303
            self.match(BKITParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_operand(self):
            return self.getTypedRuleContext(BKITParser.Left_operandContext,0)


        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assignment_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_exp" ):
                return visitor.visitAssignment_exp(self)
            else:
                return visitor.visitChildren(self)




    def assignment_exp(self):

        localctx = BKITParser.Assignment_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assignment_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.left_operand()
            self.state = 306
            self.match(BKITParser.EQUAL)
            self.state = 307
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_staContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_operand(self):
            return self.getTypedRuleContext(BKITParser.Left_operandContext,0)


        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SEMICOLON(self):
            return self.getToken(BKITParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assignment_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_sta" ):
                return visitor.visitAssignment_sta(self)
            else:
                return visitor.visitChildren(self)




    def assignment_sta(self):

        localctx = BKITParser.Assignment_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assignment_sta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.left_operand()
            self.state = 310
            self.match(BKITParser.EQUAL)
            self.state = 311
            self.exp()
            self.state = 312
            self.match(BKITParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_operandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_left_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_operand" ):
                return visitor.visitLeft_operand(self)
            else:
                return visitor.visitChildren(self)




    def left_operand(self):

        localctx = BKITParser.Left_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_left_operand)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(BKITParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.match(BKITParser.IDENTIFIER)
                self.state = 316
                self.index_operators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def EQUAL_OP_INT(self):
            return self.getToken(BKITParser.EQUAL_OP_INT, 0)

        def NOT_EQUAL_OP_INT(self):
            return self.getToken(BKITParser.NOT_EQUAL_OP_INT, 0)

        def LESS_OP_INT(self):
            return self.getToken(BKITParser.LESS_OP_INT, 0)

        def GREATER_OP_INT(self):
            return self.getToken(BKITParser.GREATER_OP_INT, 0)

        def LESS_EQUAL_OP_INT(self):
            return self.getToken(BKITParser.LESS_EQUAL_OP_INT, 0)

        def GREATER_EQUAL_OP_INT(self):
            return self.getToken(BKITParser.GREATER_EQUAL_OP_INT, 0)

        def NOT_EQUAL_OP_FLOAT(self):
            return self.getToken(BKITParser.NOT_EQUAL_OP_FLOAT, 0)

        def LESS_OP_FLOAT(self):
            return self.getToken(BKITParser.LESS_OP_FLOAT, 0)

        def GREATER_OP_FLOAT(self):
            return self.getToken(BKITParser.GREATER_OP_FLOAT, 0)

        def LESS_EQUAL_OP_FLOAT(self):
            return self.getToken(BKITParser.LESS_EQUAL_OP_FLOAT, 0)

        def GREATER_EQUAL_OP_FLOAT(self):
            return self.getToken(BKITParser.GREATER_EQUAL_OP_FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.exp1(0)
                self.state = 320
                self.match(BKITParser.EQUAL_OP_INT)
                self.state = 321
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.exp1(0)
                self.state = 324
                self.match(BKITParser.NOT_EQUAL_OP_INT)
                self.state = 325
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.exp1(0)
                self.state = 328
                self.match(BKITParser.LESS_OP_INT)
                self.state = 329
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 331
                self.exp1(0)
                self.state = 332
                self.match(BKITParser.GREATER_OP_INT)
                self.state = 333
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 335
                self.exp1(0)
                self.state = 336
                self.match(BKITParser.LESS_EQUAL_OP_INT)
                self.state = 337
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 339
                self.exp1(0)
                self.state = 340
                self.match(BKITParser.GREATER_EQUAL_OP_INT)
                self.state = 341
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 343
                self.exp1(0)
                self.state = 344
                self.match(BKITParser.NOT_EQUAL_OP_FLOAT)
                self.state = 345
                self.exp1(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 347
                self.exp1(0)
                self.state = 348
                self.match(BKITParser.LESS_OP_FLOAT)
                self.state = 349
                self.exp1(0)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 351
                self.exp1(0)
                self.state = 352
                self.match(BKITParser.GREATER_OP_FLOAT)
                self.state = 353
                self.exp1(0)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 355
                self.exp1(0)
                self.state = 356
                self.match(BKITParser.LESS_EQUAL_OP_FLOAT)
                self.state = 357
                self.exp1(0)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 359
                self.exp1(0)
                self.state = 360
                self.match(BKITParser.GREATER_EQUAL_OP_FLOAT)
                self.state = 361
                self.exp1(0)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 363
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def AND_OP(self):
            return self.getToken(BKITParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(BKITParser.OR_OP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 375
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 369
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 370
                        self.match(BKITParser.AND_OP)
                        self.state = 371
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 372
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 373
                        self.match(BKITParser.OR_OP)
                        self.state = 374
                        self.exp2(0)
                        pass

             
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def ADD_OP_INT(self):
            return self.getToken(BKITParser.ADD_OP_INT, 0)

        def SUB_OP_INT(self):
            return self.getToken(BKITParser.SUB_OP_INT, 0)

        def ADD_OP_FLOAT(self):
            return self.getToken(BKITParser.ADD_OP_FLOAT, 0)

        def SUB_OP_FLOAT(self):
            return self.getToken(BKITParser.SUB_OP_FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 397
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 395
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 383
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 384
                        self.match(BKITParser.ADD_OP_INT)
                        self.state = 385
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 386
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 387
                        self.match(BKITParser.SUB_OP_INT)
                        self.state = 388
                        self.exp3(0)
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 389
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 390
                        self.match(BKITParser.ADD_OP_FLOAT)
                        self.state = 391
                        self.exp3(0)
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 392
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 393
                        self.match(BKITParser.SUB_OP_FLOAT)
                        self.state = 394
                        self.exp3(0)
                        pass

             
                self.state = 399
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MUL_OP_INT(self):
            return self.getToken(BKITParser.MUL_OP_INT, 0)

        def DIV_OP_INT(self):
            return self.getToken(BKITParser.DIV_OP_INT, 0)

        def MOD_OP_INT(self):
            return self.getToken(BKITParser.MOD_OP_INT, 0)

        def MUL_OP_FLOAT(self):
            return self.getToken(BKITParser.MUL_OP_FLOAT, 0)

        def DIV_OP_FLOAT(self):
            return self.getToken(BKITParser.DIV_OP_FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 420
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 418
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 403
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 404
                        self.match(BKITParser.MUL_OP_INT)
                        self.state = 405
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 406
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 407
                        self.match(BKITParser.DIV_OP_INT)
                        self.state = 408
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 409
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 410
                        self.match(BKITParser.MOD_OP_INT)
                        self.state = 411
                        self.exp4()
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 412
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 413
                        self.match(BKITParser.MUL_OP_FLOAT)
                        self.state = 414
                        self.exp4()
                        pass

                    elif la_ == 5:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 415
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 416
                        self.match(BKITParser.DIV_OP_FLOAT)
                        self.state = 417
                        self.exp4()
                        pass

             
                self.state = 422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_OP(self):
            return self.getToken(BKITParser.NOT_OP, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp4)
        try:
            self.state = 426
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(BKITParser.NOT_OP)
                self.state = 424
                self.exp4()
                pass
            elif token in [BKITParser.LP, BKITParser.LCB, BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB_OP_INT, BKITParser.SUB_OP_FLOAT, BKITParser.IDENTIFIER, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OP_INT(self):
            return self.getToken(BKITParser.SUB_OP_INT, 0)

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def SUB_OP_FLOAT(self):
            return self.getToken(BKITParser.SUB_OP_FLOAT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp5)
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB_OP_INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.match(BKITParser.SUB_OP_INT)
                self.state = 429
                self.exp5()
                pass
            elif token in [BKITParser.SUB_OP_FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.match(BKITParser.SUB_OP_FLOAT)
                self.state = 431
                self.exp5()
                pass
            elif token in [BKITParser.LP, BKITParser.LCB, BKITParser.TRUE, BKITParser.FALSE, BKITParser.IDENTIFIER, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 432
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_var(self):
            return self.getTypedRuleContext(BKITParser.Name_varContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def exp7(self):
            return self.getTypedRuleContext(BKITParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKITParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp6)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.name_var()
                self.state = 436
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
                self.exp7()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def exp7(self):
            return self.getTypedRuleContext(BKITParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_name_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_var" ):
                return visitor.visitName_var(self)
            else:
                return visitor.visitChildren(self)




    def name_var(self):

        localctx = BKITParser.Name_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_name_var)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.match(BKITParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.exp7()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = BKITParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_index_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 445
                    self.match(BKITParser.LSB)
                    self.state = 446
                    self.exp()
                    self.state = 447
                    self.match(BKITParser.RSB)

                else:
                    raise NoViableAltException(self)
                self.state = 451 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def list_exp(self):
            return self.getTypedRuleContext(BKITParser.List_expContext,0)


        def exp8(self):
            return self.getTypedRuleContext(BKITParser.Exp8Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKITParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(BKITParser.IDENTIFIER)
                self.state = 454
                self.match(BKITParser.LP)
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (BKITParser.LP - 9)) | (1 << (BKITParser.LCB - 9)) | (1 << (BKITParser.TRUE - 9)) | (1 << (BKITParser.FALSE - 9)) | (1 << (BKITParser.SUB_OP_INT - 9)) | (1 << (BKITParser.SUB_OP_FLOAT - 9)) | (1 << (BKITParser.NOT_OP - 9)) | (1 << (BKITParser.IDENTIFIER - 9)) | (1 << (BKITParser.INTEGER - 9)) | (1 << (BKITParser.FLOAT - 9)) | (1 << (BKITParser.STRING - 9)))) != 0):
                    self.state = 455
                    self.list_exp()


                self.state = 458
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
                self.exp8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_type(self):
            return self.getTypedRuleContext(BKITParser.Primary_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = BKITParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp8)
        try:
            self.state = 468
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LCB, BKITParser.TRUE, BKITParser.FALSE, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.primary_type()
                pass
            elif token in [BKITParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.match(BKITParser.IDENTIFIER)
                pass
            elif token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
                self.match(BKITParser.LP)
                self.state = 465
                self.exp()
                self.state = 466
                self.match(BKITParser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_of_floatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_int_of_float

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_of_float" ):
                return visitor.visitInt_of_float(self)
            else:
                return visitor.visitChildren(self)




    def int_of_float(self):

        localctx = BKITParser.Int_of_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_int_of_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(BKITParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_to_intContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_float_to_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_to_int" ):
                return visitor.visitFloat_to_int(self)
            else:
                return visitor.visitChildren(self)




    def float_to_int(self):

        localctx = BKITParser.Float_to_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_float_to_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(BKITParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_of_stringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_int_of_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_of_string" ):
                return visitor.visitInt_of_string(self)
            else:
                return visitor.visitChildren(self)




    def int_of_string(self):

        localctx = BKITParser.Int_of_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_int_of_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(BKITParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_of_intContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_string_of_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_of_int" ):
                return visitor.visitString_of_int(self)
            else:
                return visitor.visitChildren(self)




    def string_of_int(self):

        localctx = BKITParser.String_of_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_string_of_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(BKITParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_of_stringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_float_of_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_of_string" ):
                return visitor.visitFloat_of_string(self)
            else:
                return visitor.visitChildren(self)




    def float_of_string(self):

        localctx = BKITParser.Float_of_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_float_of_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(BKITParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_of_floatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_string_of_float

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_of_float" ):
                return visitor.visitString_of_float(self)
            else:
                return visitor.visitChildren(self)




    def string_of_float(self):

        localctx = BKITParser.String_of_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_string_of_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(BKITParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_of_stringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_bool_of_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_of_string" ):
                return visitor.visitBool_of_string(self)
            else:
                return visitor.visitChildren(self)




    def bool_of_string(self):

        localctx = BKITParser.Bool_of_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_bool_of_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(BKITParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_of_boolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_string_of_bool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_of_bool" ):
                return visitor.visitString_of_bool(self)
            else:
                return visitor.visitChildren(self)




    def string_of_bool(self):

        localctx = BKITParser.String_of_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_string_of_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.match(BKITParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.exp1_sempred
        self._predicates[27] = self.exp2_sempred
        self._predicates[28] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




