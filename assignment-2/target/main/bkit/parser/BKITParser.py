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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u01e5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\7\2Z\n\2\f")
        buf.write("\2\16\2]\13\2\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\6\3j\n\3\r\3\16\3k\3\3\3\3\3\4\3\4\3\4\7\4s\n")
        buf.write("\4\f\4\16\4v\13\4\3\5\3\5\5\5z\n\5\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\6\b\u0087\n\b\r\b\16\b\u0088")
        buf.write("\5\b\u008b\n\b\3\t\3\t\3\n\3\n\6\n\u0091\n\n\r\n\16\n")
        buf.write("\u0092\3\n\3\n\3\13\3\13\3\13\5\13\u009a\n\13\3\13\3\13")
        buf.write("\3\13\7\13\u009f\n\13\f\13\16\13\u00a2\13\13\5\13\u00a4")
        buf.write("\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00ab\n\f\3\r\5\r\u00ae")
        buf.write("\n\r\3\r\3\r\3\16\5\16\u00b3\n\16\3\16\3\16\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\5\20\u00bd\n\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\21\7\21\u00c6\n\21\f\21\16\21\u00c9\13")
        buf.write("\21\3\21\7\21\u00cc\n\21\f\21\16\21\u00cf\13\21\3\22\3")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\7\23\u00d8\n\23\f\23\16\23")
        buf.write("\u00db\13\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\5\24\u00e6\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\7\25\u00f1\n\25\f\25\16\25\u00f4\13\25\3\25")
        buf.write("\3\25\5\25\u00f8\n\25\3\25\3\25\3\25\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\5\34\u0125\n\34\3\34\3\34\3\34\3")
        buf.write("\35\3\35\3\35\7\35\u012d\n\35\f\35\16\35\u0130\13\35\3")
        buf.write("\36\3\36\5\36\u0134\n\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3!\5!\u0145\n!\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\5\"\u0174\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\7#\u017f")
        buf.write("\n#\f#\16#\u0182\13#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\7$\u0193\n$\f$\16$\u0196\13$\3%\3%\3%\3%")
        buf.write("\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\7%\u01aa\n")
        buf.write("%\f%\16%\u01ad\13%\3&\3&\3&\5&\u01b2\n&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u01b9\n\'\3(\3(\3(\3(\5(\u01bf\n(\3)\3)\5)")
        buf.write("\u01c3\n)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\7*\u01cf\n*\f")
        buf.write("*\16*\u01d2\13*\3+\3+\3+\5+\u01d7\n+\3+\3+\5+\u01db\n")
        buf.write("+\3,\3,\3,\3,\3,\3,\5,\u01e3\n,\3,\2\6DFHR-\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTV\2\5\3\2#$\3\2./\3\2\37 \2\u01fc\2[\3\2\2")
        buf.write("\2\4f\3\2\2\2\6o\3\2\2\2\by\3\2\2\2\n{\3\2\2\2\f\177\3")
        buf.write("\2\2\2\16\u008a\3\2\2\2\20\u008c\3\2\2\2\22\u008e\3\2")
        buf.write("\2\2\24\u00a3\3\2\2\2\26\u00aa\3\2\2\2\30\u00ad\3\2\2")
        buf.write("\2\32\u00b2\3\2\2\2\34\u00b6\3\2\2\2\36\u00b8\3\2\2\2")
        buf.write(" \u00c7\3\2\2\2\"\u00d0\3\2\2\2$\u00d4\3\2\2\2&\u00e5")
        buf.write("\3\2\2\2(\u00e7\3\2\2\2*\u00fc\3\2\2\2,\u00fe\3\2\2\2")
        buf.write(".\u010d\3\2\2\2\60\u0114\3\2\2\2\62\u011b\3\2\2\2\64\u011e")
        buf.write("\3\2\2\2\66\u0121\3\2\2\28\u0129\3\2\2\2:\u0131\3\2\2")
        buf.write("\2<\u0137\3\2\2\2>\u013c\3\2\2\2@\u0144\3\2\2\2B\u0173")
        buf.write("\3\2\2\2D\u0175\3\2\2\2F\u0183\3\2\2\2H\u0197\3\2\2\2")
        buf.write("J\u01b1\3\2\2\2L\u01b8\3\2\2\2N\u01be\3\2\2\2P\u01c2\3")
        buf.write("\2\2\2R\u01c4\3\2\2\2T\u01da\3\2\2\2V\u01e2\3\2\2\2XZ")
        buf.write("\5\4\3\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\a\3")
        buf.write("\2\2\2][\3\2\2\2^`\5\36\20\2_^\3\2\2\2`c\3\2\2\2a_\3\2")
        buf.write("\2\2ab\3\2\2\2bd\3\2\2\2ca\3\2\2\2de\7\2\2\3e\3\3\2\2")
        buf.write("\2fg\7\35\2\2gi\7\t\2\2hj\5\6\4\2ih\3\2\2\2jk\3\2\2\2")
        buf.write("ki\3\2\2\2kl\3\2\2\2lm\3\2\2\2mn\7\n\2\2n\5\3\2\2\2ot")
        buf.write("\5\b\5\2pq\7\f\2\2qs\5\b\5\2rp\3\2\2\2sv\3\2\2\2tr\3\2")
        buf.write("\2\2tu\3\2\2\2u\7\3\2\2\2vt\3\2\2\2wz\5\f\7\2xz\5\n\6")
        buf.write("\2yw\3\2\2\2yx\3\2\2\2z\t\3\2\2\2{|\5\16\b\2|}\7\"\2\2")
        buf.write("}~\5\20\t\2~\13\3\2\2\2\177\u0080\5\16\b\2\u0080\r\3\2")
        buf.write("\2\2\u0081\u008b\7<\2\2\u0082\u0086\7<\2\2\u0083\u0084")
        buf.write("\7\5\2\2\u0084\u0085\7:\2\2\u0085\u0087\7\6\2\2\u0086")
        buf.write("\u0083\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0086\3\2\2\2")
        buf.write("\u0088\u0089\3\2\2\2\u0089\u008b\3\2\2\2\u008a\u0081\3")
        buf.write("\2\2\2\u008a\u0082\3\2\2\2\u008b\17\3\2\2\2\u008c\u008d")
        buf.write("\5\26\f\2\u008d\21\3\2\2\2\u008e\u0090\7\7\2\2\u008f\u0091")
        buf.write("\5\24\13\2\u0090\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092")
        buf.write("\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0094\u0095\7\b\2\2\u0095\23\3\2\2\2\u0096\u0099\5\22")
        buf.write("\n\2\u0097\u0098\7\f\2\2\u0098\u009a\5\22\n\2\u0099\u0097")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u00a4\3\2\2\2\u009b")
        buf.write("\u00a0\5\20\t\2\u009c\u009d\7\f\2\2\u009d\u009f\5\20\t")
        buf.write("\2\u009e\u009c\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a3\u0096\3\2\2\2\u00a3\u009b\3\2\2\2")
        buf.write("\u00a4\25\3\2\2\2\u00a5\u00ab\7:\2\2\u00a6\u00ab\7;\2")
        buf.write("\2\u00a7\u00ab\7=\2\2\u00a8\u00ab\5\34\17\2\u00a9\u00ab")
        buf.write("\5\22\n\2\u00aa\u00a5\3\2\2\2\u00aa\u00a6\3\2\2\2\u00aa")
        buf.write("\u00a7\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2")
        buf.write("\u00ab\27\3\2\2\2\u00ac\u00ae\t\2\2\2\u00ad\u00ac\3\2")
        buf.write("\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0")
        buf.write("\7:\2\2\u00b0\31\3\2\2\2\u00b1\u00b3\t\3\2\2\u00b2\u00b1")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4")
        buf.write("\u00b5\7;\2\2\u00b5\33\3\2\2\2\u00b6\u00b7\t\4\2\2\u00b7")
        buf.write("\35\3\2\2\2\u00b8\u00b9\7\30\2\2\u00b9\u00ba\7\t\2\2\u00ba")
        buf.write("\u00bc\7<\2\2\u00bb\u00bd\5\"\22\2\u00bc\u00bb\3\2\2\2")
        buf.write("\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\7")
        buf.write("\r\2\2\u00bf\u00c0\7\t\2\2\u00c0\u00c1\5 \21\2\u00c1\u00c2")
        buf.write("\7\23\2\2\u00c2\u00c3\7\13\2\2\u00c3\37\3\2\2\2\u00c4")
        buf.write("\u00c6\5<\37\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3\2\2\2")
        buf.write("\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00cd\3")
        buf.write("\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cc\5&\24\2\u00cb\u00ca")
        buf.write("\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce!\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0")
        buf.write("\u00d1\7\32\2\2\u00d1\u00d2\7\t\2\2\u00d2\u00d3\5$\23")
        buf.write("\2\u00d3#\3\2\2\2\u00d4\u00d9\5\16\b\2\u00d5\u00d6\7\f")
        buf.write("\2\2\u00d6\u00d8\5\16\b\2\u00d7\u00d5\3\2\2\2\u00d8\u00db")
        buf.write("\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("%\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00e6\5> \2\u00dd")
        buf.write("\u00e6\5(\25\2\u00de\u00e6\5,\27\2\u00df\u00e6\5.\30\2")
        buf.write("\u00e0\u00e6\5\60\31\2\u00e1\u00e6\5\62\32\2\u00e2\u00e6")
        buf.write("\5\64\33\2\u00e3\u00e6\5\66\34\2\u00e4\u00e6\5:\36\2\u00e5")
        buf.write("\u00dc\3\2\2\2\u00e5\u00dd\3\2\2\2\u00e5\u00de\3\2\2\2")
        buf.write("\u00e5\u00df\3\2\2\2\u00e5\u00e0\3\2\2\2\u00e5\u00e1\3")
        buf.write("\2\2\2\u00e5\u00e2\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4")
        buf.write("\3\2\2\2\u00e6\'\3\2\2\2\u00e7\u00e8\7\31\2\2\u00e8\u00e9")
        buf.write("\5B\"\2\u00e9\u00ea\7\34\2\2\u00ea\u00f2\5 \21\2\u00eb")
        buf.write("\u00ec\7\22\2\2\u00ec\u00ed\5B\"\2\u00ed\u00ee\7\34\2")
        buf.write("\2\u00ee\u00ef\5 \21\2\u00ef\u00f1\3\2\2\2\u00f0\u00eb")
        buf.write("\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2")
        buf.write("\u00f3\3\2\2\2\u00f3\u00f7\3\2\2\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f5\u00f6\7\21\2\2\u00f6\u00f8\5*\26\2\u00f7\u00f5")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write("\u00fa\7\24\2\2\u00fa\u00fb\7\13\2\2\u00fb)\3\2\2\2\u00fc")
        buf.write("\u00fd\5 \21\2\u00fd+\3\2\2\2\u00fe\u00ff\7\27\2\2\u00ff")
        buf.write("\u0100\7\3\2\2\u0100\u0101\7<\2\2\u0101\u0102\7\"\2\2")
        buf.write("\u0102\u0103\5B\"\2\u0103\u0104\7\f\2\2\u0104\u0105\5")
        buf.write("B\"\2\u0105\u0106\7\f\2\2\u0106\u0107\5B\"\2\u0107\u0108")
        buf.write("\7\4\2\2\u0108\u0109\7\20\2\2\u0109\u010a\5 \21\2\u010a")
        buf.write("\u010b\7\25\2\2\u010b\u010c\7\13\2\2\u010c-\3\2\2\2\u010d")
        buf.write("\u010e\7\36\2\2\u010e\u010f\5B\"\2\u010f\u0110\7\20\2")
        buf.write("\2\u0110\u0111\5 \21\2\u0111\u0112\7\26\2\2\u0112\u0113")
        buf.write("\7\13\2\2\u0113/\3\2\2\2\u0114\u0115\7\20\2\2\u0115\u0116")
        buf.write("\5 \21\2\u0116\u0117\7\36\2\2\u0117\u0118\5B\"\2\u0118")
        buf.write("\u0119\7!\2\2\u0119\u011a\7\13\2\2\u011a\61\3\2\2\2\u011b")
        buf.write("\u011c\7\16\2\2\u011c\u011d\7\n\2\2\u011d\63\3\2\2\2\u011e")
        buf.write("\u011f\7\17\2\2\u011f\u0120\7\n\2\2\u0120\65\3\2\2\2\u0121")
        buf.write("\u0122\7<\2\2\u0122\u0124\7\3\2\2\u0123\u0125\58\35\2")
        buf.write("\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0126\3")
        buf.write("\2\2\2\u0126\u0127\7\4\2\2\u0127\u0128\7\n\2\2\u0128\67")
        buf.write("\3\2\2\2\u0129\u012e\5B\"\2\u012a\u012b\7\f\2\2\u012b")
        buf.write("\u012d\5B\"\2\u012c\u012a\3\2\2\2\u012d\u0130\3\2\2\2")
        buf.write("\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f9\3\2\2")
        buf.write("\2\u0130\u012e\3\2\2\2\u0131\u0133\7\33\2\2\u0132\u0134")
        buf.write("\5B\"\2\u0133\u0132\3\2\2\2\u0133\u0134\3\2\2\2\u0134")
        buf.write("\u0135\3\2\2\2\u0135\u0136\7\n\2\2\u0136;\3\2\2\2\u0137")
        buf.write("\u0138\7\35\2\2\u0138\u0139\7\t\2\2\u0139\u013a\5\6\4")
        buf.write("\2\u013a\u013b\7\n\2\2\u013b=\3\2\2\2\u013c\u013d\5@!")
        buf.write("\2\u013d\u013e\7\"\2\2\u013e\u013f\5B\"\2\u013f\u0140")
        buf.write("\7\n\2\2\u0140?\3\2\2\2\u0141\u0145\7<\2\2\u0142\u0143")
        buf.write("\7<\2\2\u0143\u0145\5R*\2\u0144\u0141\3\2\2\2\u0144\u0142")
        buf.write("\3\2\2\2\u0145A\3\2\2\2\u0146\u0147\5D#\2\u0147\u0148")
        buf.write("\7(\2\2\u0148\u0149\5D#\2\u0149\u0174\3\2\2\2\u014a\u014b")
        buf.write("\5D#\2\u014b\u014c\7)\2\2\u014c\u014d\5D#\2\u014d\u0174")
        buf.write("\3\2\2\2\u014e\u014f\5D#\2\u014f\u0150\7+\2\2\u0150\u0151")
        buf.write("\5D#\2\u0151\u0174\3\2\2\2\u0152\u0153\5D#\2\u0153\u0154")
        buf.write("\7*\2\2\u0154\u0155\5D#\2\u0155\u0174\3\2\2\2\u0156\u0157")
        buf.write("\5D#\2\u0157\u0158\7-\2\2\u0158\u0159\5D#\2\u0159\u0174")
        buf.write("\3\2\2\2\u015a\u015b\5D#\2\u015b\u015c\7,\2\2\u015c\u015d")
        buf.write("\5D#\2\u015d\u0174\3\2\2\2\u015e\u015f\5D#\2\u015f\u0160")
        buf.write("\7\66\2\2\u0160\u0161\5D#\2\u0161\u0174\3\2\2\2\u0162")
        buf.write("\u0163\5D#\2\u0163\u0164\7\63\2\2\u0164\u0165\5D#\2\u0165")
        buf.write("\u0174\3\2\2\2\u0166\u0167\5D#\2\u0167\u0168\7\62\2\2")
        buf.write("\u0168\u0169\5D#\2\u0169\u0174\3\2\2\2\u016a\u016b\5D")
        buf.write("#\2\u016b\u016c\7\65\2\2\u016c\u016d\5D#\2\u016d\u0174")
        buf.write("\3\2\2\2\u016e\u016f\5D#\2\u016f\u0170\7\64\2\2\u0170")
        buf.write("\u0171\5D#\2\u0171\u0174\3\2\2\2\u0172\u0174\5D#\2\u0173")
        buf.write("\u0146\3\2\2\2\u0173\u014a\3\2\2\2\u0173\u014e\3\2\2\2")
        buf.write("\u0173\u0152\3\2\2\2\u0173\u0156\3\2\2\2\u0173\u015a\3")
        buf.write("\2\2\2\u0173\u015e\3\2\2\2\u0173\u0162\3\2\2\2\u0173\u0166")
        buf.write("\3\2\2\2\u0173\u016a\3\2\2\2\u0173\u016e\3\2\2\2\u0173")
        buf.write("\u0172\3\2\2\2\u0174C\3\2\2\2\u0175\u0176\b#\1\2\u0176")
        buf.write("\u0177\5F$\2\u0177\u0180\3\2\2\2\u0178\u0179\f\5\2\2\u0179")
        buf.write("\u017a\78\2\2\u017a\u017f\5F$\2\u017b\u017c\f\4\2\2\u017c")
        buf.write("\u017d\79\2\2\u017d\u017f\5F$\2\u017e\u0178\3\2\2\2\u017e")
        buf.write("\u017b\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0180\u0181\3\2\2\2\u0181E\3\2\2\2\u0182\u0180\3\2\2")
        buf.write("\2\u0183\u0184\b$\1\2\u0184\u0185\5H%\2\u0185\u0194\3")
        buf.write("\2\2\2\u0186\u0187\f\7\2\2\u0187\u0188\7#\2\2\u0188\u0193")
        buf.write("\5H%\2\u0189\u018a\f\6\2\2\u018a\u018b\7$\2\2\u018b\u0193")
        buf.write("\5H%\2\u018c\u018d\f\5\2\2\u018d\u018e\7.\2\2\u018e\u0193")
        buf.write("\5H%\2\u018f\u0190\f\4\2\2\u0190\u0191\7/\2\2\u0191\u0193")
        buf.write("\5H%\2\u0192\u0186\3\2\2\2\u0192\u0189\3\2\2\2\u0192\u018c")
        buf.write("\3\2\2\2\u0192\u018f\3\2\2\2\u0193\u0196\3\2\2\2\u0194")
        buf.write("\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195G\3\2\2\2\u0196")
        buf.write("\u0194\3\2\2\2\u0197\u0198\b%\1\2\u0198\u0199\5J&\2\u0199")
        buf.write("\u01ab\3\2\2\2\u019a\u019b\f\b\2\2\u019b\u019c\7%\2\2")
        buf.write("\u019c\u01aa\5J&\2\u019d\u019e\f\7\2\2\u019e\u019f\7&")
        buf.write("\2\2\u019f\u01aa\5J&\2\u01a0\u01a1\f\6\2\2\u01a1\u01a2")
        buf.write("\7\'\2\2\u01a2\u01aa\5J&\2\u01a3\u01a4\f\5\2\2\u01a4\u01a5")
        buf.write("\7\60\2\2\u01a5\u01aa\5J&\2\u01a6\u01a7\f\4\2\2\u01a7")
        buf.write("\u01a8\7\61\2\2\u01a8\u01aa\5J&\2\u01a9\u019a\3\2\2\2")
        buf.write("\u01a9\u019d\3\2\2\2\u01a9\u01a0\3\2\2\2\u01a9\u01a3\3")
        buf.write("\2\2\2\u01a9\u01a6\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01acI\3\2\2\2\u01ad\u01ab")
        buf.write("\3\2\2\2\u01ae\u01af\7\67\2\2\u01af\u01b2\5J&\2\u01b0")
        buf.write("\u01b2\5L\'\2\u01b1\u01ae\3\2\2\2\u01b1\u01b0\3\2\2\2")
        buf.write("\u01b2K\3\2\2\2\u01b3\u01b4\7$\2\2\u01b4\u01b9\5L\'\2")
        buf.write("\u01b5\u01b6\7/\2\2\u01b6\u01b9\5L\'\2\u01b7\u01b9\5N")
        buf.write("(\2\u01b8\u01b3\3\2\2\2\u01b8\u01b5\3\2\2\2\u01b8\u01b7")
        buf.write("\3\2\2\2\u01b9M\3\2\2\2\u01ba\u01bb\5P)\2\u01bb\u01bc")
        buf.write("\5R*\2\u01bc\u01bf\3\2\2\2\u01bd\u01bf\5T+\2\u01be\u01ba")
        buf.write("\3\2\2\2\u01be\u01bd\3\2\2\2\u01bfO\3\2\2\2\u01c0\u01c3")
        buf.write("\7<\2\2\u01c1\u01c3\5T+\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1")
        buf.write("\3\2\2\2\u01c3Q\3\2\2\2\u01c4\u01c5\b*\1\2\u01c5\u01c6")
        buf.write("\7\5\2\2\u01c6\u01c7\5B\"\2\u01c7\u01c8\7\6\2\2\u01c8")
        buf.write("\u01d0\3\2\2\2\u01c9\u01ca\f\3\2\2\u01ca\u01cb\7\5\2\2")
        buf.write("\u01cb\u01cc\5B\"\2\u01cc\u01cd\7\6\2\2\u01cd\u01cf\3")
        buf.write("\2\2\2\u01ce\u01c9\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce")
        buf.write("\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1S\3\2\2\2\u01d2\u01d0")
        buf.write("\3\2\2\2\u01d3\u01d4\7<\2\2\u01d4\u01d6\7\3\2\2\u01d5")
        buf.write("\u01d7\58\35\2\u01d6\u01d5\3\2\2\2\u01d6\u01d7\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8\u01db\7\4\2\2\u01d9\u01db\5")
        buf.write("V,\2\u01da\u01d3\3\2\2\2\u01da\u01d9\3\2\2\2\u01dbU\3")
        buf.write("\2\2\2\u01dc\u01e3\5\26\f\2\u01dd\u01e3\7<\2\2\u01de\u01df")
        buf.write("\7\3\2\2\u01df\u01e0\5B\"\2\u01e0\u01e1\7\4\2\2\u01e1")
        buf.write("\u01e3\3\2\2\2\u01e2\u01dc\3\2\2\2\u01e2\u01dd\3\2\2\2")
        buf.write("\u01e2\u01de\3\2\2\2\u01e3W\3\2\2\2*[akty\u0088\u008a")
        buf.write("\u0092\u0099\u00a0\u00a3\u00aa\u00ad\u00b2\u00bc\u00c7")
        buf.write("\u00cd\u00d9\u00e5\u00f2\u00f7\u0124\u012e\u0133\u0144")
        buf.write("\u0173\u017e\u0180\u0192\u0194\u01a9\u01ab\u01b1\u01b8")
        buf.write("\u01be\u01c2\u01d0\u01d6\u01da\u01e2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "':'", "';'", "'.'", "','", "'Body'", "'Break'", "'Continue'", 
                     "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", 
                     "'EndFor'", "'EndWhile'", "'For'", "'Function'", "'If'", 
                     "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
                     "'True'", "'False'", "'EndDo'", "'='", "'+'", "'-'", 
                     "'*'", "'\\'", "'%'", "'=='", "'!='", "'>'", "'<'", 
                     "'>='", "'<='", "'+.'", "'-.'", "'*.'", "'\\.'", "'>.'", 
                     "'<.'", "'>=.'", "'<=.'", "'=/='", "'!'", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "LP", "RP", "LSB", "RSB", "LCB", "RCB", 
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
                      "INTEGER", "FLOAT", "IDENTIFIER", "STRING", "WS", 
                      "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_glo_variable_dec = 1
    RULE_list_var = 2
    RULE_var_elem = 3
    RULE_var_init = 4
    RULE_var = 5
    RULE_variable_id = 6
    RULE_value = 7
    RULE_array = 8
    RULE_array_elem = 9
    RULE_literal = 10
    RULE_unary_int = 11
    RULE_unary_float = 12
    RULE_boolean = 13
    RULE_function_dec = 14
    RULE_list_sta = 15
    RULE_parameter_dec = 16
    RULE_list_param = 17
    RULE_statement = 18
    RULE_if_sta = 19
    RULE_list_else_sta = 20
    RULE_for_sta = 21
    RULE_while_sta = 22
    RULE_do_while_sta = 23
    RULE_break_sta = 24
    RULE_continue_sta = 25
    RULE_call_sta = 26
    RULE_list_exp = 27
    RULE_return_sta = 28
    RULE_variable_dec = 29
    RULE_assignment_sta = 30
    RULE_left_operand = 31
    RULE_exp = 32
    RULE_exp1 = 33
    RULE_exp2 = 34
    RULE_exp3 = 35
    RULE_exp4 = 36
    RULE_exp5 = 37
    RULE_exp6 = 38
    RULE_name_index_op = 39
    RULE_index_operators = 40
    RULE_function_call = 41
    RULE_exp8 = 42

    ruleNames =  [ "program", "glo_variable_dec", "list_var", "var_elem", 
                   "var_init", "var", "variable_id", "value", "array", "array_elem", 
                   "literal", "unary_int", "unary_float", "boolean", "function_dec", 
                   "list_sta", "parameter_dec", "list_param", "statement", 
                   "if_sta", "list_else_sta", "for_sta", "while_sta", "do_while_sta", 
                   "break_sta", "continue_sta", "call_sta", "list_exp", 
                   "return_sta", "variable_dec", "assignment_sta", "left_operand", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "name_index_op", "index_operators", "function_call", 
                   "exp8" ]

    EOF = Token.EOF
    LP=1
    RP=2
    LSB=3
    RSB=4
    LCB=5
    RCB=6
    COLON=7
    SEMICOLON=8
    DOT=9
    COMMA=10
    BODY=11
    BREAK=12
    CONTINUE=13
    DO=14
    ELSE=15
    ELSEIF=16
    ENDBODY=17
    ENDIF=18
    ENDFOR=19
    ENDWHILE=20
    FOR=21
    FUNCTION=22
    IF=23
    PARAMETER=24
    RETURN=25
    THEN=26
    VAR=27
    WHILE=28
    TRUE=29
    FALSE=30
    ENDDO=31
    EQUAL=32
    ADD_OP_INT=33
    SUB_OP_INT=34
    MUL_OP_INT=35
    DIV_OP_INT=36
    MOD_OP_INT=37
    EQUAL_OP_INT=38
    NOT_EQUAL_OP_INT=39
    GREATER_OP_INT=40
    LESS_OP_INT=41
    GREATER_EQUAL_OP_INT=42
    LESS_EQUAL_OP_INT=43
    ADD_OP_FLOAT=44
    SUB_OP_FLOAT=45
    MUL_OP_FLOAT=46
    DIV_OP_FLOAT=47
    GREATER_OP_FLOAT=48
    LESS_OP_FLOAT=49
    GREATER_EQUAL_OP_FLOAT=50
    LESS_EQUAL_OP_FLOAT=51
    NOT_EQUAL_OP_FLOAT=52
    NOT_OP=53
    AND_OP=54
    OR_OP=55
    INTEGER=56
    FLOAT=57
    IDENTIFIER=58
    STRING=59
    WS=60
    COMMENT=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    UNTERMINATED_COMMENT=65

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
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 86
                self.glo_variable_dec()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 92
                self.function_dec()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
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

        def SEMICOLON(self):
            return self.getToken(BKITParser.SEMICOLON, 0)

        def list_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.List_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.List_varContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(BKITParser.VAR)
            self.state = 101
            self.match(BKITParser.COLON)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.list_var()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.IDENTIFIER):
                    break

            self.state = 107
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

        def var_elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_elemContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_elemContext,i)


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
            self.state = 109
            self.var_elem()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 110
                self.match(BKITParser.COMMA)
                self.state = 111
                self.var_elem()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_elemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(BKITParser.VarContext,0)


        def var_init(self):
            return self.getTypedRuleContext(BKITParser.Var_initContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_elem" ):
                return visitor.visitVar_elem(self)
            else:
                return visitor.visitChildren(self)




    def var_elem(self):

        localctx = BKITParser.Var_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_elem)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.var_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_id(self):
            return self.getTypedRuleContext(BKITParser.Variable_idContext,0)


        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def value(self):
            return self.getTypedRuleContext(BKITParser.ValueContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_init" ):
                return visitor.visitVar_init(self)
            else:
                return visitor.visitChildren(self)




    def var_init(self):

        localctx = BKITParser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.variable_id()
            self.state = 122
            self.match(BKITParser.EQUAL)
            self.state = 123
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_id(self):
            return self.getTypedRuleContext(BKITParser.Variable_idContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = BKITParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.variable_id()
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
        self.enterRule(localctx, 12, self.RULE_variable_id)
        self._la = 0 # Token type
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(BKITParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(BKITParser.IDENTIFIER)
                self.state = 132 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 129
                    self.match(BKITParser.LSB)
                    self.state = 130
                    self.match(BKITParser.INTEGER)
                    self.state = 131
                    self.match(BKITParser.RSB)
                    self.state = 134 
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

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = BKITParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.literal()
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

        def array_elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Array_elemContext)
            else:
                return self.getTypedRuleContext(BKITParser.Array_elemContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(BKITParser.LCB)
            self.state = 142 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 141
                self.array_elem()
                self.state = 144 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.LCB) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.STRING))) != 0)):
                    break

            self.state = 146
            self.match(BKITParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ArrayContext)
            else:
                return self.getTypedRuleContext(BKITParser.ArrayContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ValueContext)
            else:
                return self.getTypedRuleContext(BKITParser.ValueContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_array_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_elem" ):
                return visitor.visitArray_elem(self)
            else:
                return visitor.visitChildren(self)




    def array_elem(self):

        localctx = BKITParser.Array_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_elem)
        self._la = 0 # Token type
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.array()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKITParser.COMMA:
                    self.state = 149
                    self.match(BKITParser.COMMA)
                    self.state = 150
                    self.array()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.value()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 154
                    self.match(BKITParser.COMMA)
                    self.state = 155
                    self.value()
                    self.state = 160
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def boolean(self):
            return self.getTypedRuleContext(BKITParser.BooleanContext,0)


        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_literal)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(BKITParser.INTEGER)
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.match(BKITParser.STRING)
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.boolean()
                pass
            elif token in [BKITParser.LCB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
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


    class Unary_intContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def SUB_OP_INT(self):
            return self.getToken(BKITParser.SUB_OP_INT, 0)

        def ADD_OP_INT(self):
            return self.getToken(BKITParser.ADD_OP_INT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_unary_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_int" ):
                return visitor.visitUnary_int(self)
            else:
                return visitor.visitChildren(self)




    def unary_int(self):

        localctx = BKITParser.Unary_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_unary_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ADD_OP_INT or _la==BKITParser.SUB_OP_INT:
                self.state = 170
                _la = self._input.LA(1)
                if not(_la==BKITParser.ADD_OP_INT or _la==BKITParser.SUB_OP_INT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 173
            self.match(BKITParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_floatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def SUB_OP_FLOAT(self):
            return self.getToken(BKITParser.SUB_OP_FLOAT, 0)

        def ADD_OP_FLOAT(self):
            return self.getToken(BKITParser.ADD_OP_FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_unary_float

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_float" ):
                return visitor.visitUnary_float(self)
            else:
                return visitor.visitChildren(self)




    def unary_float(self):

        localctx = BKITParser.Unary_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_unary_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ADD_OP_FLOAT or _la==BKITParser.SUB_OP_FLOAT:
                self.state = 175
                _la = self._input.LA(1)
                if not(_la==BKITParser.ADD_OP_FLOAT or _la==BKITParser.SUB_OP_FLOAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 178
            self.match(BKITParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_boolean

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = BKITParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            _la = self._input.LA(1)
            if not(_la==BKITParser.TRUE or _la==BKITParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self.enterRule(localctx, 28, self.RULE_function_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(BKITParser.FUNCTION)
            self.state = 183
            self.match(BKITParser.COLON)
            self.state = 184
            self.match(BKITParser.IDENTIFIER)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 185
                self.parameter_dec()


            self.state = 188
            self.match(BKITParser.BODY)
            self.state = 189
            self.match(BKITParser.COLON)
            self.state = 190
            self.list_sta()
            self.state = 191
            self.match(BKITParser.ENDBODY)
            self.state = 192
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
        self.enterRule(localctx, 30, self.RULE_list_sta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 194
                self.variable_dec()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 200
                    self.statement() 
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_parameter_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(BKITParser.PARAMETER)
            self.state = 207
            self.match(BKITParser.COLON)
            self.state = 208
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
        self.enterRule(localctx, 34, self.RULE_list_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.variable_id()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 211
                self.match(BKITParser.COMMA)
                self.state = 212
                self.variable_id()
                self.state = 217
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
        self.enterRule(localctx, 36, self.RULE_statement)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.assignment_sta()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.if_sta()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.for_sta()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 221
                self.while_sta()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 222
                self.do_while_sta()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 223
                self.break_sta()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 224
                self.continue_sta()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 225
                self.call_sta()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 226
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

        def list_else_sta(self):
            return self.getTypedRuleContext(BKITParser.List_else_staContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_sta" ):
                return visitor.visitIf_sta(self)
            else:
                return visitor.visitChildren(self)




    def if_sta(self):

        localctx = BKITParser.If_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_if_sta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(BKITParser.IF)
            self.state = 230
            self.exp()
            self.state = 231
            self.match(BKITParser.THEN)
            self.state = 232
            self.list_sta()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 233
                self.match(BKITParser.ELSEIF)
                self.state = 234
                self.exp()
                self.state = 235
                self.match(BKITParser.THEN)
                self.state = 236
                self.list_sta()
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 243
                self.match(BKITParser.ELSE)
                self.state = 244
                self.list_else_sta()


            self.state = 247
            self.match(BKITParser.ENDIF)
            self.state = 248
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_else_staContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_sta(self):
            return self.getTypedRuleContext(BKITParser.List_staContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_else_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_else_sta" ):
                return visitor.visitList_else_sta(self)
            else:
                return visitor.visitChildren(self)




    def list_else_sta(self):

        localctx = BKITParser.List_else_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_list_else_sta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.list_sta()
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
        self.enterRule(localctx, 42, self.RULE_for_sta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(BKITParser.FOR)
            self.state = 253
            self.match(BKITParser.LP)
            self.state = 254
            self.match(BKITParser.IDENTIFIER)
            self.state = 255
            self.match(BKITParser.EQUAL)
            self.state = 256
            self.exp()
            self.state = 257
            self.match(BKITParser.COMMA)
            self.state = 258
            self.exp()
            self.state = 259
            self.match(BKITParser.COMMA)
            self.state = 260
            self.exp()
            self.state = 261
            self.match(BKITParser.RP)
            self.state = 262
            self.match(BKITParser.DO)
            self.state = 263
            self.list_sta()
            self.state = 264
            self.match(BKITParser.ENDFOR)
            self.state = 265
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
        self.enterRule(localctx, 44, self.RULE_while_sta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(BKITParser.WHILE)
            self.state = 268
            self.exp()
            self.state = 269
            self.match(BKITParser.DO)
            self.state = 270
            self.list_sta()
            self.state = 271
            self.match(BKITParser.ENDWHILE)
            self.state = 272
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

        def list_sta(self):
            return self.getTypedRuleContext(BKITParser.List_staContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_while_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_sta" ):
                return visitor.visitDo_while_sta(self)
            else:
                return visitor.visitChildren(self)




    def do_while_sta(self):

        localctx = BKITParser.Do_while_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_do_while_sta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(BKITParser.DO)
            self.state = 275
            self.list_sta()
            self.state = 276
            self.match(BKITParser.WHILE)
            self.state = 277
            self.exp()
            self.state = 278
            self.match(BKITParser.ENDDO)
            self.state = 279
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
        self.enterRule(localctx, 48, self.RULE_break_sta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(BKITParser.BREAK)
            self.state = 282
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
        self.enterRule(localctx, 50, self.RULE_continue_sta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(BKITParser.CONTINUE)
            self.state = 285
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
        self.enterRule(localctx, 52, self.RULE_call_sta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(BKITParser.IDENTIFIER)
            self.state = 288
            self.match(BKITParser.LP)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.LP) | (1 << BKITParser.LCB) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB_OP_INT) | (1 << BKITParser.SUB_OP_FLOAT) | (1 << BKITParser.NOT_OP) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.STRING))) != 0):
                self.state = 289
                self.list_exp()


            self.state = 292
            self.match(BKITParser.RP)
            self.state = 293
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
        self.enterRule(localctx, 54, self.RULE_list_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.exp()
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 296
                self.match(BKITParser.COMMA)
                self.state = 297
                self.exp()
                self.state = 302
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
        self.enterRule(localctx, 56, self.RULE_return_sta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(BKITParser.RETURN)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.LP) | (1 << BKITParser.LCB) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB_OP_INT) | (1 << BKITParser.SUB_OP_FLOAT) | (1 << BKITParser.NOT_OP) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.STRING))) != 0):
                self.state = 304
                self.exp()


            self.state = 307
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
        self.enterRule(localctx, 58, self.RULE_variable_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(BKITParser.VAR)
            self.state = 310
            self.match(BKITParser.COLON)
            self.state = 311
            self.list_var()
            self.state = 312
            self.match(BKITParser.SEMICOLON)
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
        self.enterRule(localctx, 60, self.RULE_assignment_sta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.left_operand()
            self.state = 315
            self.match(BKITParser.EQUAL)
            self.state = 316
            self.exp()
            self.state = 317
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
        self.enterRule(localctx, 62, self.RULE_left_operand)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(BKITParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(BKITParser.IDENTIFIER)
                self.state = 321
                self.index_operators(0)
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
        self.enterRule(localctx, 64, self.RULE_exp)
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.exp1(0)
                self.state = 325
                self.match(BKITParser.EQUAL_OP_INT)
                self.state = 326
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.exp1(0)
                self.state = 329
                self.match(BKITParser.NOT_EQUAL_OP_INT)
                self.state = 330
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 332
                self.exp1(0)
                self.state = 333
                self.match(BKITParser.LESS_OP_INT)
                self.state = 334
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 336
                self.exp1(0)
                self.state = 337
                self.match(BKITParser.GREATER_OP_INT)
                self.state = 338
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 340
                self.exp1(0)
                self.state = 341
                self.match(BKITParser.LESS_EQUAL_OP_INT)
                self.state = 342
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 344
                self.exp1(0)
                self.state = 345
                self.match(BKITParser.GREATER_EQUAL_OP_INT)
                self.state = 346
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 348
                self.exp1(0)
                self.state = 349
                self.match(BKITParser.NOT_EQUAL_OP_FLOAT)
                self.state = 350
                self.exp1(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 352
                self.exp1(0)
                self.state = 353
                self.match(BKITParser.LESS_OP_FLOAT)
                self.state = 354
                self.exp1(0)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 356
                self.exp1(0)
                self.state = 357
                self.match(BKITParser.GREATER_OP_FLOAT)
                self.state = 358
                self.exp1(0)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 360
                self.exp1(0)
                self.state = 361
                self.match(BKITParser.LESS_EQUAL_OP_FLOAT)
                self.state = 362
                self.exp1(0)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 364
                self.exp1(0)
                self.state = 365
                self.match(BKITParser.GREATER_EQUAL_OP_FLOAT)
                self.state = 366
                self.exp1(0)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 368
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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 382
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 380
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 374
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 375
                        self.match(BKITParser.AND_OP)
                        self.state = 376
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 377
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 378
                        self.match(BKITParser.OR_OP)
                        self.state = 379
                        self.exp2(0)
                        pass

             
                self.state = 384
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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 402
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 400
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 388
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 389
                        self.match(BKITParser.ADD_OP_INT)
                        self.state = 390
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 391
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 392
                        self.match(BKITParser.SUB_OP_INT)
                        self.state = 393
                        self.exp3(0)
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 394
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 395
                        self.match(BKITParser.ADD_OP_FLOAT)
                        self.state = 396
                        self.exp3(0)
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 397
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 398
                        self.match(BKITParser.SUB_OP_FLOAT)
                        self.state = 399
                        self.exp3(0)
                        pass

             
                self.state = 404
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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 423
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 408
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 409
                        self.match(BKITParser.MUL_OP_INT)
                        self.state = 410
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 411
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 412
                        self.match(BKITParser.DIV_OP_INT)
                        self.state = 413
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 414
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 415
                        self.match(BKITParser.MOD_OP_INT)
                        self.state = 416
                        self.exp4()
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 417
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 418
                        self.match(BKITParser.MUL_OP_FLOAT)
                        self.state = 419
                        self.exp4()
                        pass

                    elif la_ == 5:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 420
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 421
                        self.match(BKITParser.DIV_OP_FLOAT)
                        self.state = 422
                        self.exp4()
                        pass

             
                self.state = 427
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
        self.enterRule(localctx, 72, self.RULE_exp4)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.match(BKITParser.NOT_OP)
                self.state = 429
                self.exp4()
                pass
            elif token in [BKITParser.LP, BKITParser.LCB, BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB_OP_INT, BKITParser.SUB_OP_FLOAT, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.IDENTIFIER, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
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
        self.enterRule(localctx, 74, self.RULE_exp5)
        try:
            self.state = 438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB_OP_INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.match(BKITParser.SUB_OP_INT)
                self.state = 434
                self.exp5()
                pass
            elif token in [BKITParser.SUB_OP_FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.match(BKITParser.SUB_OP_FLOAT)
                self.state = 436
                self.exp5()
                pass
            elif token in [BKITParser.LP, BKITParser.LCB, BKITParser.TRUE, BKITParser.FALSE, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.IDENTIFIER, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
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

        def name_index_op(self):
            return self.getTypedRuleContext(BKITParser.Name_index_opContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKITParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exp6)
        try:
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.name_index_op()
                self.state = 441
                self.index_operators(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_index_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKITParser.IDENTIFIER, 0)

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_name_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_index_op" ):
                return visitor.visitName_index_op(self)
            else:
                return visitor.visitChildren(self)




    def name_index_op(self):

        localctx = BKITParser.Name_index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_name_index_op)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(BKITParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.function_call()
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

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)



    def index_operators(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Index_operatorsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_index_operators, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(BKITParser.LSB)
            self.state = 452
            self.exp()
            self.state = 453
            self.match(BKITParser.RSB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Index_operatorsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operators)
                    self.state = 455
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 456
                    self.match(BKITParser.LSB)
                    self.state = 457
                    self.exp()
                    self.state = 458
                    self.match(BKITParser.RSB) 
                self.state = 464
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Function_callContext(ParserRuleContext):

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
            return BKITParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.match(BKITParser.IDENTIFIER)
                self.state = 466
                self.match(BKITParser.LP)
                self.state = 468
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.LP) | (1 << BKITParser.LCB) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB_OP_INT) | (1 << BKITParser.SUB_OP_FLOAT) | (1 << BKITParser.NOT_OP) | (1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.IDENTIFIER) | (1 << BKITParser.STRING))) != 0):
                    self.state = 467
                    self.list_exp()


                self.state = 470
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
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

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


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
        self.enterRule(localctx, 84, self.RULE_exp8)
        try:
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LCB, BKITParser.TRUE, BKITParser.FALSE, BKITParser.INTEGER, BKITParser.FLOAT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.literal()
                pass
            elif token in [BKITParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.match(BKITParser.IDENTIFIER)
                pass
            elif token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 476
                self.match(BKITParser.LP)
                self.state = 477
                self.exp()
                self.state = 478
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[33] = self.exp1_sempred
        self._predicates[34] = self.exp2_sempred
        self._predicates[35] = self.exp3_sempred
        self._predicates[40] = self.index_operators_sempred
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
         

    def index_operators_sempred(self, localctx:Index_operatorsContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 1)
         




