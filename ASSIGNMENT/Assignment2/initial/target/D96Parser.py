# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u023c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\3\2\6\2p\n\2\r\2\16\2q")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\6\3~\n\3\r\3")
        buf.write("\16\3\177\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\6\3\u0090\n\3\r\3\16\3\u0091\3\3\3\3\5\3")
        buf.write("\u0096\n\3\3\4\3\4\5\4\u009a\n\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\u00a2\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00ab")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00b4\n\7\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\7\t\u00bd\n\t\f\t\16\t\u00c0\13\t")
        buf.write("\3\n\3\n\3\13\3\13\3\13\7\13\u00c7\n\13\f\13\16\13\u00ca")
        buf.write("\13\13\3\f\3\f\3\f\3\f\3\f\5\f\u00d1\n\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00e0\n\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00ec\n\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\7")
        buf.write("\20\u00f6\n\20\f\20\16\20\u00f9\13\20\3\21\3\21\6\21\u00fd")
        buf.write("\n\21\r\21\16\21\u00fe\3\21\3\21\3\21\3\21\5\21\u0105")
        buf.write("\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u0110\n\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3")
        buf.write("\25\3\25\5\25\u011c\n\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\5\27\u0129\n\27\3\30\3\30\3")
        buf.write("\30\3\30\5\30\u012f\n\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\5\32\u013c\n\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\5\37\u0156\n\37\3\37\3\37\3\37\3 \3 \5 \u015d\n \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\5\"\u017e\n\"\3#\3#\3#\3#\3#\5#\u0185\n#\3$\3$")
        buf.write("\3$\3$\3$\5$\u018c\n$\3%\3%\3%\3%\3%\3%\7%\u0194\n%\f")
        buf.write("%\16%\u0197\13%\3&\3&\3&\3&\3&\3&\7&\u019f\n&\f&\16&\u01a2")
        buf.write("\13&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u01aa\n\'\f\'\16\'\u01ad")
        buf.write("\13\'\3(\3(\3(\5(\u01b2\n(\3)\3)\3)\5)\u01b7\n)\3*\3*")
        buf.write("\3*\3*\5*\u01bd\n*\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u01c8")
        buf.write("\n+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\7,\u01dc\n,\f,\16,\u01df\13,\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01f3\n-\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0200\n.\3/\3/\3/\3/\3/\5")
        buf.write("/\u0207\n/\3\60\3\60\3\60\3\60\5\60\u020d\n\60\3\61\3")
        buf.write("\61\3\61\7\61\u0212\n\61\f\61\16\61\u0215\13\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\62\3\62\5\62\u021e\n\62\3\63\3\63")
        buf.write("\5\63\u0222\n\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3")
        buf.write("\65\3\65\3\65\5\65\u022e\n\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\2\6HJLV8\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjl\2\b\3\2;<\3\29:\4\2\62")
        buf.write("\64\668\3\2\60\61\3\2*+\3\2,.\2\u024b\2o\3\2\2\2\4\u0095")
        buf.write("\3\2\2\2\6\u0099\3\2\2\2\b\u00a1\3\2\2\2\n\u00aa\3\2\2")
        buf.write("\2\f\u00b3\3\2\2\2\16\u00b5\3\2\2\2\20\u00b9\3\2\2\2\22")
        buf.write("\u00c1\3\2\2\2\24\u00c3\3\2\2\2\26\u00d0\3\2\2\2\30\u00df")
        buf.write("\3\2\2\2\32\u00eb\3\2\2\2\34\u00ed\3\2\2\2\36\u00f2\3")
        buf.write("\2\2\2 \u0104\3\2\2\2\"\u010f\3\2\2\2$\u0111\3\2\2\2&")
        buf.write("\u0114\3\2\2\2(\u011b\3\2\2\2*\u011d\3\2\2\2,\u0128\3")
        buf.write("\2\2\2.\u012e\3\2\2\2\60\u0130\3\2\2\2\62\u013b\3\2\2")
        buf.write("\2\64\u013d\3\2\2\2\66\u0143\3\2\2\28\u0146\3\2\2\2:\u0149")
        buf.write("\3\2\2\2<\u014c\3\2\2\2>\u015a\3\2\2\2@\u0160\3\2\2\2")
        buf.write("B\u017d\3\2\2\2D\u0184\3\2\2\2F\u018b\3\2\2\2H\u018d\3")
        buf.write("\2\2\2J\u0198\3\2\2\2L\u01a3\3\2\2\2N\u01b1\3\2\2\2P\u01b6")
        buf.write("\3\2\2\2R\u01bc\3\2\2\2T\u01c7\3\2\2\2V\u01c9\3\2\2\2")
        buf.write("X\u01f2\3\2\2\2Z\u01ff\3\2\2\2\\\u0206\3\2\2\2^\u020c")
        buf.write("\3\2\2\2`\u0213\3\2\2\2b\u021d\3\2\2\2d\u0221\3\2\2\2")
        buf.write("f\u0223\3\2\2\2h\u022d\3\2\2\2j\u022f\3\2\2\2l\u0234\3")
        buf.write("\2\2\2np\5\4\3\2on\3\2\2\2pq\3\2\2\2qo\3\2\2\2qr\3\2\2")
        buf.write("\2rs\3\2\2\2st\7\2\2\3t\3\3\2\2\2uv\7\21\2\2vw\7;\2\2")
        buf.write("wx\7\t\2\2x\u0096\7\n\2\2yz\7\21\2\2z{\7;\2\2{}\7\t\2")
        buf.write("\2|~\5\6\4\2}|\3\2\2\2~\177\3\2\2\2\177}\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\7\n\2\2\u0082")
        buf.write("\u0096\3\2\2\2\u0083\u0084\7\21\2\2\u0084\u0085\7;\2\2")
        buf.write("\u0085\u0086\7\16\2\2\u0086\u0087\7;\2\2\u0087\u0088\7")
        buf.write("\t\2\2\u0088\u0096\7\n\2\2\u0089\u008a\7\21\2\2\u008a")
        buf.write("\u008b\7;\2\2\u008b\u008c\7\16\2\2\u008c\u008d\7;\2\2")
        buf.write("\u008d\u008f\7\t\2\2\u008e\u0090\5\6\4\2\u008f\u008e\3")
        buf.write("\2\2\2\u0090\u0091\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\7\n\2\2\u0094")
        buf.write("\u0096\3\2\2\2\u0095u\3\2\2\2\u0095y\3\2\2\2\u0095\u0083")
        buf.write("\3\2\2\2\u0095\u0089\3\2\2\2\u0096\5\3\2\2\2\u0097\u009a")
        buf.write("\5\b\5\2\u0098\u009a\5\30\r\2\u0099\u0097\3\2\2\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a\7\3\2\2\2\u009b\u009c\5\n\6\2\u009c")
        buf.write("\u009d\7\r\2\2\u009d\u00a2\3\2\2\2\u009e\u009f\5\f\7\2")
        buf.write("\u009f\u00a0\7\r\2\2\u00a0\u00a2\3\2\2\2\u00a1\u009b\3")
        buf.write("\2\2\2\u00a1\u009e\3\2\2\2\u00a2\t\3\2\2\2\u00a3\u00a4")
        buf.write("\7\22\2\2\u00a4\u00a5\5\16\b\2\u00a5\u00a6\7\65\2\2\u00a6")
        buf.write("\u00a7\5\24\13\2\u00a7\u00ab\3\2\2\2\u00a8\u00a9\7\22")
        buf.write("\2\2\u00a9\u00ab\5\16\b\2\u00aa\u00a3\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00ab\13\3\2\2\2\u00ac\u00ad\7\23\2\2\u00ad\u00ae")
        buf.write("\5\16\b\2\u00ae\u00af\7\65\2\2\u00af\u00b0\5\24\13\2\u00b0")
        buf.write("\u00b4\3\2\2\2\u00b1\u00b2\7\23\2\2\u00b2\u00b4\5\16\b")
        buf.write("\2\u00b3\u00ac\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\r\3\2")
        buf.write("\2\2\u00b5\u00b6\5\20\t\2\u00b6\u00b7\7\16\2\2\u00b7\u00b8")
        buf.write("\5\26\f\2\u00b8\17\3\2\2\2\u00b9\u00be\5\22\n\2\u00ba")
        buf.write("\u00bb\7\20\2\2\u00bb\u00bd\5\22\n\2\u00bc\u00ba\3\2\2")
        buf.write("\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf")
        buf.write("\3\2\2\2\u00bf\21\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c2")
        buf.write("\t\2\2\2\u00c2\23\3\2\2\2\u00c3\u00c8\5D#\2\u00c4\u00c5")
        buf.write("\7\20\2\2\u00c5\u00c7\5D#\2\u00c6\u00c4\3\2\2\2\u00c7")
        buf.write("\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2")
        buf.write("\u00c9\25\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00d1\7\26")
        buf.write("\2\2\u00cc\u00d1\7\27\2\2\u00cd\u00d1\7\31\2\2\u00ce\u00d1")
        buf.write("\7\30\2\2\u00cf\u00d1\5l\67\2\u00d0\u00cb\3\2\2\2\u00d0")
        buf.write("\u00cc\3\2\2\2\u00d0\u00cd\3\2\2\2\u00d0\u00ce\3\2\2\2")
        buf.write("\u00d0\u00cf\3\2\2\2\u00d1\27\3\2\2\2\u00d2\u00e0\5\32")
        buf.write("\16\2\u00d3\u00e0\5\34\17\2\u00d4\u00d5\5\22\n\2\u00d5")
        buf.write("\u00d6\7\7\2\2\u00d6\u00d7\7\b\2\2\u00d7\u00d8\5 \21\2")
        buf.write("\u00d8\u00e0\3\2\2\2\u00d9\u00da\5\22\n\2\u00da\u00db")
        buf.write("\7\7\2\2\u00db\u00dc\5\36\20\2\u00dc\u00dd\7\b\2\2\u00dd")
        buf.write("\u00de\5 \21\2\u00de\u00e0\3\2\2\2\u00df\u00d2\3\2\2\2")
        buf.write("\u00df\u00d3\3\2\2\2\u00df\u00d4\3\2\2\2\u00df\u00d9\3")
        buf.write("\2\2\2\u00e0\31\3\2\2\2\u00e1\u00e2\7$\2\2\u00e2\u00e3")
        buf.write("\7\7\2\2\u00e3\u00e4\7\b\2\2\u00e4\u00ec\5 \21\2\u00e5")
        buf.write("\u00e6\7$\2\2\u00e6\u00e7\7\7\2\2\u00e7\u00e8\5\36\20")
        buf.write("\2\u00e8\u00e9\7\b\2\2\u00e9\u00ea\5 \21\2\u00ea\u00ec")
        buf.write("\3\2\2\2\u00eb\u00e1\3\2\2\2\u00eb\u00e5\3\2\2\2\u00ec")
        buf.write("\33\3\2\2\2\u00ed\u00ee\7%\2\2\u00ee\u00ef\7\7\2\2\u00ef")
        buf.write("\u00f0\7\b\2\2\u00f0\u00f1\5 \21\2\u00f1\35\3\2\2\2\u00f2")
        buf.write("\u00f7\5\16\b\2\u00f3\u00f4\7\r\2\2\u00f4\u00f6\5\16\b")
        buf.write("\2\u00f5\u00f3\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7\u00f5")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\37\3\2\2\2\u00f9\u00f7")
        buf.write("\3\2\2\2\u00fa\u00fc\7\t\2\2\u00fb\u00fd\5\"\22\2\u00fc")
        buf.write("\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00fc\3\2\2\2")
        buf.write("\u00fe\u00ff\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\7")
        buf.write("\n\2\2\u0101\u0105\3\2\2\2\u0102\u0103\7\t\2\2\u0103\u0105")
        buf.write("\7\n\2\2\u0104\u00fa\3\2\2\2\u0104\u0102\3\2\2\2\u0105")
        buf.write("!\3\2\2\2\u0106\u0110\5$\23\2\u0107\u0110\5.\30\2\u0108")
        buf.write("\u0110\5\b\5\2\u0109\u0110\58\35\2\u010a\u0110\5:\36\2")
        buf.write("\u010b\u0110\5<\37\2\u010c\u0110\5> \2\u010d\u0110\5@")
        buf.write("!\2\u010e\u0110\5 \21\2\u010f\u0106\3\2\2\2\u010f\u0107")
        buf.write("\3\2\2\2\u010f\u0108\3\2\2\2\u010f\u0109\3\2\2\2\u010f")
        buf.write("\u010a\3\2\2\2\u010f\u010b\3\2\2\2\u010f\u010c\3\2\2\2")
        buf.write("\u010f\u010d\3\2\2\2\u010f\u010e\3\2\2\2\u0110#\3\2\2")
        buf.write("\2\u0111\u0112\5&\24\2\u0112\u0113\7\r\2\2\u0113%\3\2")
        buf.write("\2\2\u0114\u0115\5(\25\2\u0115\u0116\7\65\2\2\u0116\u0117")
        buf.write("\5D#\2\u0117\'\3\2\2\2\u0118\u011c\7;\2\2\u0119\u011c")
        buf.write("\5*\26\2\u011a\u011c\5,\27\2\u011b\u0118\3\2\2\2\u011b")
        buf.write("\u0119\3\2\2\2\u011b\u011a\3\2\2\2\u011c)\3\2\2\2\u011d")
        buf.write("\u011e\5V,\2\u011e\u011f\5T+\2\u011f+\3\2\2\2\u0120\u0121")
        buf.write("\5D#\2\u0121\u0122\7(\2\2\u0122\u0123\7;\2\2\u0123\u0129")
        buf.write("\3\2\2\2\u0124\u0125\5D#\2\u0125\u0126\7\17\2\2\u0126")
        buf.write("\u0127\7<\2\2\u0127\u0129\3\2\2\2\u0128\u0120\3\2\2\2")
        buf.write("\u0128\u0124\3\2\2\2\u0129-\3\2\2\2\u012a\u012b\5\60\31")
        buf.write("\2\u012b\u012c\5\62\32\2\u012c\u012f\3\2\2\2\u012d\u012f")
        buf.write("\5\60\31\2\u012e\u012a\3\2\2\2\u012e\u012d\3\2\2\2\u012f")
        buf.write("/\3\2\2\2\u0130\u0131\7\35\2\2\u0131\u0132\7\7\2\2\u0132")
        buf.write("\u0133\5D#\2\u0133\u0134\7\b\2\2\u0134\u0135\5 \21\2\u0135")
        buf.write("\61\3\2\2\2\u0136\u0137\5\64\33\2\u0137\u0138\5\62\32")
        buf.write("\2\u0138\u013c\3\2\2\2\u0139\u013c\5\64\33\2\u013a\u013c")
        buf.write("\5\66\34\2\u013b\u0136\3\2\2\2\u013b\u0139\3\2\2\2\u013b")
        buf.write("\u013a\3\2\2\2\u013c\63\3\2\2\2\u013d\u013e\7\36\2\2\u013e")
        buf.write("\u013f\7\7\2\2\u013f\u0140\5D#\2\u0140\u0141\7\b\2\2\u0141")
        buf.write("\u0142\5 \21\2\u0142\65\3\2\2\2\u0143\u0144\7\37\2\2\u0144")
        buf.write("\u0145\5 \21\2\u0145\67\3\2\2\2\u0146\u0147\7\33\2\2\u0147")
        buf.write("\u0148\7\r\2\2\u01489\3\2\2\2\u0149\u014a\7\34\2\2\u014a")
        buf.write("\u014b\7\r\2\2\u014b;\3\2\2\2\u014c\u014d\7 \2\2\u014d")
        buf.write("\u014e\7\7\2\2\u014e\u014f\7;\2\2\u014f\u0150\7&\2\2\u0150")
        buf.write("\u0151\7\4\2\2\u0151\u0152\7)\2\2\u0152\u0155\7\4\2\2")
        buf.write("\u0153\u0154\7\'\2\2\u0154\u0156\7\4\2\2\u0155\u0153\3")
        buf.write("\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158")
        buf.write("\7\b\2\2\u0158\u0159\5 \21\2\u0159=\3\2\2\2\u015a\u015c")
        buf.write("\7!\2\2\u015b\u015d\5D#\2\u015c\u015b\3\2\2\2\u015c\u015d")
        buf.write("\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\7\r\2\2\u015f")
        buf.write("?\3\2\2\2\u0160\u0161\5B\"\2\u0161\u0162\7\r\2\2\u0162")
        buf.write("A\3\2\2\2\u0163\u0164\5D#\2\u0164\u0165\7(\2\2\u0165\u0166")
        buf.write("\7;\2\2\u0166\u0167\7\7\2\2\u0167\u0168\7\b\2\2\u0168")
        buf.write("\u017e\3\2\2\2\u0169\u016a\5D#\2\u016a\u016b\7(\2\2\u016b")
        buf.write("\u016c\7;\2\2\u016c\u016d\7\7\2\2\u016d\u016e\5\24\13")
        buf.write("\2\u016e\u016f\7\b\2\2\u016f\u017e\3\2\2\2\u0170\u0171")
        buf.write("\5D#\2\u0171\u0172\7\17\2\2\u0172\u0173\7<\2\2\u0173\u0174")
        buf.write("\7\7\2\2\u0174\u0175\7\b\2\2\u0175\u017e\3\2\2\2\u0176")
        buf.write("\u0177\5D#\2\u0177\u0178\7\17\2\2\u0178\u0179\7<\2\2\u0179")
        buf.write("\u017a\7\7\2\2\u017a\u017b\5\24\13\2\u017b\u017c\7\b\2")
        buf.write("\2\u017c\u017e\3\2\2\2\u017d\u0163\3\2\2\2\u017d\u0169")
        buf.write("\3\2\2\2\u017d\u0170\3\2\2\2\u017d\u0176\3\2\2\2\u017e")
        buf.write("C\3\2\2\2\u017f\u0180\5F$\2\u0180\u0181\t\3\2\2\u0181")
        buf.write("\u0182\5F$\2\u0182\u0185\3\2\2\2\u0183\u0185\5F$\2\u0184")
        buf.write("\u017f\3\2\2\2\u0184\u0183\3\2\2\2\u0185E\3\2\2\2\u0186")
        buf.write("\u0187\5H%\2\u0187\u0188\t\4\2\2\u0188\u0189\5H%\2\u0189")
        buf.write("\u018c\3\2\2\2\u018a\u018c\5H%\2\u018b\u0186\3\2\2\2\u018b")
        buf.write("\u018a\3\2\2\2\u018cG\3\2\2\2\u018d\u018e\b%\1\2\u018e")
        buf.write("\u018f\5J&\2\u018f\u0195\3\2\2\2\u0190\u0191\f\4\2\2\u0191")
        buf.write("\u0192\t\5\2\2\u0192\u0194\5J&\2\u0193\u0190\3\2\2\2\u0194")
        buf.write("\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196I\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u0199\b&\1\2")
        buf.write("\u0199\u019a\5L\'\2\u019a\u01a0\3\2\2\2\u019b\u019c\f")
        buf.write("\4\2\2\u019c\u019d\t\6\2\2\u019d\u019f\5L\'\2\u019e\u019b")
        buf.write("\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0")
        buf.write("\u01a1\3\2\2\2\u01a1K\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3")
        buf.write("\u01a4\b\'\1\2\u01a4\u01a5\5N(\2\u01a5\u01ab\3\2\2\2\u01a6")
        buf.write("\u01a7\f\4\2\2\u01a7\u01a8\t\7\2\2\u01a8\u01aa\5N(\2\u01a9")
        buf.write("\u01a6\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2")
        buf.write("\u01ab\u01ac\3\2\2\2\u01acM\3\2\2\2\u01ad\u01ab\3\2\2")
        buf.write("\2\u01ae\u01af\7/\2\2\u01af\u01b2\5N(\2\u01b0\u01b2\5")
        buf.write("P)\2\u01b1\u01ae\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2O\3")
        buf.write("\2\2\2\u01b3\u01b4\7+\2\2\u01b4\u01b7\5P)\2\u01b5\u01b7")
        buf.write("\5R*\2\u01b6\u01b3\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7Q")
        buf.write("\3\2\2\2\u01b8\u01b9\5V,\2\u01b9\u01ba\5T+\2\u01ba\u01bd")
        buf.write("\3\2\2\2\u01bb\u01bd\5V,\2\u01bc\u01b8\3\2\2\2\u01bc\u01bb")
        buf.write("\3\2\2\2\u01bdS\3\2\2\2\u01be\u01bf\7\13\2\2\u01bf\u01c0")
        buf.write("\5D#\2\u01c0\u01c1\7\f\2\2\u01c1\u01c2\5T+\2\u01c2\u01c8")
        buf.write("\3\2\2\2\u01c3\u01c4\7\13\2\2\u01c4\u01c5\5D#\2\u01c5")
        buf.write("\u01c6\7\f\2\2\u01c6\u01c8\3\2\2\2\u01c7\u01be\3\2\2\2")
        buf.write("\u01c7\u01c3\3\2\2\2\u01c8U\3\2\2\2\u01c9\u01ca\b,\1\2")
        buf.write("\u01ca\u01cb\5X-\2\u01cb\u01dd\3\2\2\2\u01cc\u01cd\f\6")
        buf.write("\2\2\u01cd\u01ce\7(\2\2\u01ce\u01dc\7;\2\2\u01cf\u01d0")
        buf.write("\f\5\2\2\u01d0\u01d1\7(\2\2\u01d1\u01d2\7;\2\2\u01d2\u01d3")
        buf.write("\7\7\2\2\u01d3\u01dc\7\b\2\2\u01d4\u01d5\f\4\2\2\u01d5")
        buf.write("\u01d6\7(\2\2\u01d6\u01d7\7;\2\2\u01d7\u01d8\7\7\2\2\u01d8")
        buf.write("\u01d9\5\24\13\2\u01d9\u01da\7\b\2\2\u01da\u01dc\3\2\2")
        buf.write("\2\u01db\u01cc\3\2\2\2\u01db\u01cf\3\2\2\2\u01db\u01d4")
        buf.write("\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd")
        buf.write("\u01de\3\2\2\2\u01deW\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0")
        buf.write("\u01e1\5Z.\2\u01e1\u01e2\7\17\2\2\u01e2\u01e3\7<\2\2\u01e3")
        buf.write("\u01f3\3\2\2\2\u01e4\u01e5\5Z.\2\u01e5\u01e6\7\17\2\2")
        buf.write("\u01e6\u01e7\7<\2\2\u01e7\u01e8\7\7\2\2\u01e8\u01e9\7")
        buf.write("\b\2\2\u01e9\u01f3\3\2\2\2\u01ea\u01eb\5Z.\2\u01eb\u01ec")
        buf.write("\7\17\2\2\u01ec\u01ed\7<\2\2\u01ed\u01ee\7\7\2\2\u01ee")
        buf.write("\u01ef\5\24\13\2\u01ef\u01f0\7\b\2\2\u01f0\u01f3\3\2\2")
        buf.write("\2\u01f1\u01f3\5Z.\2\u01f2\u01e0\3\2\2\2\u01f2\u01e4\3")
        buf.write("\2\2\2\u01f2\u01ea\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3Y")
        buf.write("\3\2\2\2\u01f4\u01f5\7#\2\2\u01f5\u01f6\7;\2\2\u01f6\u01f7")
        buf.write("\7\7\2\2\u01f7\u0200\7\b\2\2\u01f8\u01f9\7#\2\2\u01f9")
        buf.write("\u01fa\7;\2\2\u01fa\u01fb\7\7\2\2\u01fb\u01fc\5\24\13")
        buf.write("\2\u01fc\u01fd\7\b\2\2\u01fd\u0200\3\2\2\2\u01fe\u0200")
        buf.write("\5\\/\2\u01ff\u01f4\3\2\2\2\u01ff\u01f8\3\2\2\2\u01ff")
        buf.write("\u01fe\3\2\2\2\u0200[\3\2\2\2\u0201\u0202\7\7\2\2\u0202")
        buf.write("\u0203\5D#\2\u0203\u0204\7\b\2\2\u0204\u0207\3\2\2\2\u0205")
        buf.write("\u0207\5^\60\2\u0206\u0201\3\2\2\2\u0206\u0205\3\2\2\2")
        buf.write("\u0207]\3\2\2\2\u0208\u020d\7;\2\2\u0209\u020d\5b\62\2")
        buf.write("\u020a\u020d\7\"\2\2\u020b\u020d\7\32\2\2\u020c\u0208")
        buf.write("\3\2\2\2\u020c\u0209\3\2\2\2\u020c\u020a\3\2\2\2\u020c")
        buf.write("\u020b\3\2\2\2\u020d_\3\2\2\2\u020e\u020f\5b\62\2\u020f")
        buf.write("\u0210\7\20\2\2\u0210\u0212\3\2\2\2\u0211\u020e\3\2\2")
        buf.write("\2\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214")
        buf.write("\3\2\2\2\u0214\u0216\3\2\2\2\u0215\u0213\3\2\2\2\u0216")
        buf.write("\u0217\5b\62\2\u0217a\3\2\2\2\u0218\u021e\7\4\2\2\u0219")
        buf.write("\u021e\7\3\2\2\u021a\u021e\7\5\2\2\u021b\u021e\7\6\2\2")
        buf.write("\u021c\u021e\5d\63\2\u021d\u0218\3\2\2\2\u021d\u0219\3")
        buf.write("\2\2\2\u021d\u021a\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021c")
        buf.write("\3\2\2\2\u021ec\3\2\2\2\u021f\u0222\5f\64\2\u0220\u0222")
        buf.write("\5j\66\2\u0221\u021f\3\2\2\2\u0221\u0220\3\2\2\2\u0222")
        buf.write("e\3\2\2\2\u0223\u0224\7\25\2\2\u0224\u0225\7\7\2\2\u0225")
        buf.write("\u0226\5h\65\2\u0226\u0227\7\b\2\2\u0227g\3\2\2\2\u0228")
        buf.write("\u0229\5j\66\2\u0229\u022a\7\20\2\2\u022a\u022b\5h\65")
        buf.write("\2\u022b\u022e\3\2\2\2\u022c\u022e\5j\66\2\u022d\u0228")
        buf.write("\3\2\2\2\u022d\u022c\3\2\2\2\u022ei\3\2\2\2\u022f\u0230")
        buf.write("\7\25\2\2\u0230\u0231\7\7\2\2\u0231\u0232\5\24\13\2\u0232")
        buf.write("\u0233\7\b\2\2\u0233k\3\2\2\2\u0234\u0235\7\25\2\2\u0235")
        buf.write("\u0236\7\13\2\2\u0236\u0237\5\26\f\2\u0237\u0238\7\20")
        buf.write("\2\2\u0238\u0239\7\4\2\2\u0239\u023a\7\f\2\2\u023am\3")
        buf.write("\2\2\2-q\177\u0091\u0095\u0099\u00a1\u00aa\u00b3\u00be")
        buf.write("\u00c8\u00d0\u00df\u00eb\u00f7\u00fe\u0104\u010f\u011b")
        buf.write("\u0128\u012e\u013b\u0155\u015c\u017d\u0184\u018b\u0195")
        buf.write("\u01a0\u01ab\u01b1\u01b6\u01bc\u01c7\u01db\u01dd\u01f2")
        buf.write("\u01ff\u0206\u020c\u0213\u021d\u0221\u022d")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "':'", "'::'", "','", "'Class'", "'Val'", "'Var'", 
                     "<INVALID>", "'Array'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Null'", "'Break'", "'Continue'", "'If'", 
                     "'Elseif'", "'Else'", "'Foreach'", "'Return'", "'self'", 
                     "'New'", "'Constructor'", "'Destructor'", "'In'", "'By'", 
                     "'.'", "'..'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'<='", "'>='", "'!='", "'='", "'=='", 
                     "'<'", "'>'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>", "FLOAT_LITERAL", "INTEGER_LITERAL", "BOOLEAN_LITERAL", 
                      "STRING_LITERAL", "LB", "RB", "LP", "RP", "LSB", "RSB", 
                      "SEMI", "COL", "DCOL", "COM", "CLASS", "VAL", "VAR", 
                      "BLOCK_COMMENT", "ARRAY", "INT", "FLOAT", "BOOLEAN", 
                      "STRING", "NULL", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "RETURN", "SELF", "NEW", "CONSTRUCTOR", 
                      "DESTRUCTOR", "IN", "BY", "DOT", "DDOT", "OP_ADD", 
                      "OP_SUB", "OP_MUL", "OP_DIV", "OP_MOD", "OP_NOT", 
                      "OP_AND", "OP_OR", "OP_LTE", "OP_GTE", "OP_NEQ", "OP_AS", 
                      "OP_EQ", "OP_LT", "OP_GT", "OP_EQ_STR", "OP_ADD_STR", 
                      "IDEN", "DOL_IDEN", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_mem_decl = 2
    RULE_attr_decl = 3
    RULE_immutable_attr = 4
    RULE_mutable_attr = 5
    RULE_id_list_type = 6
    RULE_id_list = 7
    RULE_iden_dol = 8
    RULE_expr_list = 9
    RULE_data_type = 10
    RULE_method_decl = 11
    RULE_constr_decl = 12
    RULE_destr_decl = 13
    RULE_params_list = 14
    RULE_block_stmt = 15
    RULE_block_item = 16
    RULE_assign_stmt = 17
    RULE_assign_lhs = 18
    RULE_lhs = 19
    RULE_array_operator = 20
    RULE_field_access = 21
    RULE_if_stmt = 22
    RULE_if_element = 23
    RULE_else_stmt = 24
    RULE_elif_element = 25
    RULE_else_element = 26
    RULE_break_stmt = 27
    RULE_continue_stmt = 28
    RULE_forin_stmt = 29
    RULE_return_stmt = 30
    RULE_method_invocation_stmt = 31
    RULE_method_invocation = 32
    RULE_expr = 33
    RULE_expr1 = 34
    RULE_expr2 = 35
    RULE_expr3 = 36
    RULE_expr4 = 37
    RULE_expr5 = 38
    RULE_expr6 = 39
    RULE_expr7 = 40
    RULE_index_operators = 41
    RULE_expr8 = 42
    RULE_expr9 = 43
    RULE_expr10 = 44
    RULE_expr11 = 45
    RULE_operands = 46
    RULE_list_literal = 47
    RULE_literal = 48
    RULE_array = 49
    RULE_muldi_arr = 50
    RULE_array_list = 51
    RULE_indx_arr = 52
    RULE_array_type = 53

    ruleNames =  [ "program", "class_decl", "mem_decl", "attr_decl", "immutable_attr", 
                   "mutable_attr", "id_list_type", "id_list", "iden_dol", 
                   "expr_list", "data_type", "method_decl", "constr_decl", 
                   "destr_decl", "params_list", "block_stmt", "block_item", 
                   "assign_stmt", "assign_lhs", "lhs", "array_operator", 
                   "field_access", "if_stmt", "if_element", "else_stmt", 
                   "elif_element", "else_element", "break_stmt", "continue_stmt", 
                   "forin_stmt", "return_stmt", "method_invocation_stmt", 
                   "method_invocation", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "index_operators", 
                   "expr8", "expr9", "expr10", "expr11", "operands", "list_literal", 
                   "literal", "array", "muldi_arr", "array_list", "indx_arr", 
                   "array_type" ]

    EOF = Token.EOF
    FLOAT_LITERAL=1
    INTEGER_LITERAL=2
    BOOLEAN_LITERAL=3
    STRING_LITERAL=4
    LB=5
    RB=6
    LP=7
    RP=8
    LSB=9
    RSB=10
    SEMI=11
    COL=12
    DCOL=13
    COM=14
    CLASS=15
    VAL=16
    VAR=17
    BLOCK_COMMENT=18
    ARRAY=19
    INT=20
    FLOAT=21
    BOOLEAN=22
    STRING=23
    NULL=24
    BREAK=25
    CONTINUE=26
    IF=27
    ELSEIF=28
    ELSE=29
    FOREACH=30
    RETURN=31
    SELF=32
    NEW=33
    CONSTRUCTOR=34
    DESTRUCTOR=35
    IN=36
    BY=37
    DOT=38
    DDOT=39
    OP_ADD=40
    OP_SUB=41
    OP_MUL=42
    OP_DIV=43
    OP_MOD=44
    OP_NOT=45
    OP_AND=46
    OP_OR=47
    OP_LTE=48
    OP_GTE=49
    OP_NEQ=50
    OP_AS=51
    OP_EQ=52
    OP_LT=53
    OP_GT=54
    OP_EQ_STR=55
    OP_ADD_STR=56
    IDEN=57
    DOL_IDEN=58
    WS=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61
    ERROR_CHAR=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 108
                self.class_decl()
                self.state = 111 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 113
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def IDEN(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDEN)
            else:
                return self.getToken(D96Parser.IDEN, i)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def mem_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Mem_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Mem_declContext,i)


        def COL(self):
            return self.getToken(D96Parser.COL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(D96Parser.CLASS)
                self.state = 116
                self.match(D96Parser.IDEN)
                self.state = 117
                self.match(D96Parser.LP)
                self.state = 118
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(D96Parser.CLASS)
                self.state = 120
                self.match(D96Parser.IDEN)
                self.state = 121
                self.match(D96Parser.LP)
                self.state = 123 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 122
                    self.mem_decl()
                    self.state = 125 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDEN) | (1 << D96Parser.DOL_IDEN))) != 0)):
                        break

                self.state = 127
                self.match(D96Parser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.match(D96Parser.CLASS)
                self.state = 130
                self.match(D96Parser.IDEN)
                self.state = 131
                self.match(D96Parser.COL)
                self.state = 132
                self.match(D96Parser.IDEN)
                self.state = 133
                self.match(D96Parser.LP)
                self.state = 134
                self.match(D96Parser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.match(D96Parser.CLASS)
                self.state = 136
                self.match(D96Parser.IDEN)
                self.state = 137
                self.match(D96Parser.COL)
                self.state = 138
                self.match(D96Parser.IDEN)
                self.state = 139
                self.match(D96Parser.LP)
                self.state = 141 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 140
                    self.mem_decl()
                    self.state = 143 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDEN) | (1 << D96Parser.DOL_IDEN))) != 0)):
                        break

                self.state = 145
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mem_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_decl(self):
            return self.getTypedRuleContext(D96Parser.Attr_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(D96Parser.Method_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mem_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMem_decl" ):
                return visitor.visitMem_decl(self)
            else:
                return visitor.visitChildren(self)




    def mem_decl(self):

        localctx = D96Parser.Mem_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mem_decl)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.attr_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.IDEN, D96Parser.DOL_IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.method_decl()
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


    class Attr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def immutable_attr(self):
            return self.getTypedRuleContext(D96Parser.Immutable_attrContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def mutable_attr(self):
            return self.getTypedRuleContext(D96Parser.Mutable_attrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl" ):
                return visitor.visitAttr_decl(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl(self):

        localctx = D96Parser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attr_decl)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.immutable_attr()
                self.state = 154
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.mutable_attr()
                self.state = 157
                self.match(D96Parser.SEMI)
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


    class Immutable_attrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def id_list_type(self):
            return self.getTypedRuleContext(D96Parser.Id_list_typeContext,0)


        def OP_AS(self):
            return self.getToken(D96Parser.OP_AS, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_immutable_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutable_attr" ):
                return visitor.visitImmutable_attr(self)
            else:
                return visitor.visitChildren(self)




    def immutable_attr(self):

        localctx = D96Parser.Immutable_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_immutable_attr)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(D96Parser.VAL)
                self.state = 162
                self.id_list_type()
                self.state = 163
                self.match(D96Parser.OP_AS)
                self.state = 164
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(D96Parser.VAL)
                self.state = 167
                self.id_list_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mutable_attrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def id_list_type(self):
            return self.getTypedRuleContext(D96Parser.Id_list_typeContext,0)


        def OP_AS(self):
            return self.getToken(D96Parser.OP_AS, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mutable_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutable_attr" ):
                return visitor.visitMutable_attr(self)
            else:
                return visitor.visitChildren(self)




    def mutable_attr(self):

        localctx = D96Parser.Mutable_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mutable_attr)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(D96Parser.VAR)
                self.state = 171
                self.id_list_type()
                self.state = 172
                self.match(D96Parser.OP_AS)
                self.state = 173
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(D96Parser.VAR)
                self.state = 176
                self.id_list_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_list_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def COL(self):
            return self.getToken(D96Parser.COL, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_id_list_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list_type" ):
                return visitor.visitId_list_type(self)
            else:
                return visitor.visitChildren(self)




    def id_list_type(self):

        localctx = D96Parser.Id_list_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_id_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.id_list()
            self.state = 180
            self.match(D96Parser.COL)
            self.state = 181
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iden_dol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Iden_dolContext)
            else:
                return self.getTypedRuleContext(D96Parser.Iden_dolContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COM)
            else:
                return self.getToken(D96Parser.COM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = D96Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.iden_dol()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COM:
                self.state = 184
                self.match(D96Parser.COM)
                self.state = 185
                self.iden_dol()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Iden_dolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_iden_dol

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIden_dol" ):
                return visitor.visitIden_dol(self)
            else:
                return visitor.visitChildren(self)




    def iden_dol(self):

        localctx = D96Parser.Iden_dolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_iden_dol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            _la = self._input.LA(1)
            if not(_la==D96Parser.IDEN or _la==D96Parser.DOL_IDEN):
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


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COM)
            else:
                return self.getToken(D96Parser.COM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.expr()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COM:
                self.state = 194
                self.match(D96Parser.COM)
                self.state = 195
                self.expr()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_data_type)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 205
                self.array_type()
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


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constr_decl(self):
            return self.getTypedRuleContext(D96Parser.Constr_declContext,0)


        def destr_decl(self):
            return self.getTypedRuleContext(D96Parser.Destr_declContext,0)


        def iden_dol(self):
            return self.getTypedRuleContext(D96Parser.Iden_dolContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def params_list(self):
            return self.getTypedRuleContext(D96Parser.Params_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = D96Parser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method_decl)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.constr_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.destr_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.iden_dol()
                self.state = 211
                self.match(D96Parser.LB)
                self.state = 212
                self.match(D96Parser.RB)
                self.state = 213
                self.block_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 215
                self.iden_dol()
                self.state = 216
                self.match(D96Parser.LB)
                self.state = 217
                self.params_list()
                self.state = 218
                self.match(D96Parser.RB)
                self.state = 219
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def params_list(self):
            return self.getTypedRuleContext(D96Parser.Params_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstr_decl" ):
                return visitor.visitConstr_decl(self)
            else:
                return visitor.visitChildren(self)




    def constr_decl(self):

        localctx = D96Parser.Constr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_constr_decl)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(D96Parser.CONSTRUCTOR)
                self.state = 224
                self.match(D96Parser.LB)
                self.state = 225
                self.match(D96Parser.RB)
                self.state = 226
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(D96Parser.CONSTRUCTOR)
                self.state = 228
                self.match(D96Parser.LB)
                self.state = 229
                self.params_list()
                self.state = 230
                self.match(D96Parser.RB)
                self.state = 231
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestr_decl" ):
                return visitor.visitDestr_decl(self)
            else:
                return visitor.visitChildren(self)




    def destr_decl(self):

        localctx = D96Parser.Destr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_destr_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(D96Parser.DESTRUCTOR)
            self.state = 236
            self.match(D96Parser.LB)
            self.state = 237
            self.match(D96Parser.RB)
            self.state = 238
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Id_list_typeContext)
            else:
                return self.getTypedRuleContext(D96Parser.Id_list_typeContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_params_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list" ):
                return visitor.visitParams_list(self)
            else:
                return visitor.visitChildren(self)




    def params_list(self):

        localctx = D96Parser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.id_list_type()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 241
                self.match(D96Parser.SEMI)
                self.state = 242
                self.id_list_type()
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_itemContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_itemContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(D96Parser.LP)
                self.state = 250 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 249
                    self.block_item()
                    self.state = 252 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0)):
                        break

                self.state = 254
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(D96Parser.LP)
                self.state = 257
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def attr_decl(self):
            return self.getTypedRuleContext(D96Parser.Attr_declContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmtContext,0)


        def forin_stmt(self):
            return self.getTypedRuleContext(D96Parser.Forin_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def method_invocation_stmt(self):
            return self.getTypedRuleContext(D96Parser.Method_invocation_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_block_item

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_item" ):
                return visitor.visitBlock_item(self)
            else:
                return visitor.visitChildren(self)




    def block_item(self):

        localctx = D96Parser.Block_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_block_item)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self.attr_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 263
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 264
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 265
                self.forin_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 266
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 267
                self.method_invocation_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 268
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhsContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.assign_lhs()
            self.state = 272
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def OP_AS(self):
            return self.getToken(D96Parser.OP_AS, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs" ):
                return visitor.visitAssign_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_lhs(self):

        localctx = D96Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assign_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.lhs()
            self.state = 275
            self.match(D96Parser.OP_AS)
            self.state = 276
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def array_operator(self):
            return self.getTypedRuleContext(D96Parser.Array_operatorContext,0)


        def field_access(self):
            return self.getTypedRuleContext(D96Parser.Field_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_lhs)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(D96Parser.IDEN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.array_operator()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.field_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_operator" ):
                return visitor.visitArray_operator(self)
            else:
                return visitor.visitChildren(self)




    def array_operator(self):

        localctx = D96Parser.Array_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.expr8(0)
            self.state = 284
            self.index_operators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def DCOL(self):
            return self.getToken(D96Parser.DCOL, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_field_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_access" ):
                return visitor.visitField_access(self)
            else:
                return visitor.visitChildren(self)




    def field_access(self):

        localctx = D96Parser.Field_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_field_access)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.expr()
                self.state = 287
                self.match(D96Parser.DOT)
                self.state = 288
                self.match(D96Parser.IDEN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.expr()
                self.state = 291
                self.match(D96Parser.DCOL)
                self.state = 292
                self.match(D96Parser.DOL_IDEN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_element(self):
            return self.getTypedRuleContext(D96Parser.If_elementContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(D96Parser.Else_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_if_stmt)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.if_element()
                self.state = 297
                self.else_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.if_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_element" ):
                return visitor.visitIf_element(self)
            else:
                return visitor.visitChildren(self)




    def if_element(self):

        localctx = D96Parser.If_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(D96Parser.IF)
            self.state = 303
            self.match(D96Parser.LB)
            self.state = 304
            self.expr()
            self.state = 305
            self.match(D96Parser.RB)
            self.state = 306
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_element(self):
            return self.getTypedRuleContext(D96Parser.Elif_elementContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(D96Parser.Else_stmtContext,0)


        def else_element(self):
            return self.getTypedRuleContext(D96Parser.Else_elementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = D96Parser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_else_stmt)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.elif_element()
                self.state = 309
                self.else_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.elif_element()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.else_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elif_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_element" ):
                return visitor.visitElif_element(self)
            else:
                return visitor.visitChildren(self)




    def elif_element(self):

        localctx = D96Parser.Elif_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elif_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(D96Parser.ELSEIF)
            self.state = 316
            self.match(D96Parser.LB)
            self.state = 317
            self.expr()
            self.state = 318
            self.match(D96Parser.RB)
            self.state = 319
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_element" ):
                return visitor.visitElse_element(self)
            else:
                return visitor.visitChildren(self)




    def else_element(self):

        localctx = D96Parser.Else_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_else_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(D96Parser.ELSE)
            self.state = 322
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(D96Parser.BREAK)
            self.state = 325
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(D96Parser.CONTINUE)
            self.state = 328
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forin_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.INTEGER_LITERAL)
            else:
                return self.getToken(D96Parser.INTEGER_LITERAL, i)

        def DDOT(self):
            return self.getToken(D96Parser.DDOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forin_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForin_stmt" ):
                return visitor.visitForin_stmt(self)
            else:
                return visitor.visitChildren(self)




    def forin_stmt(self):

        localctx = D96Parser.Forin_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forin_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(D96Parser.FOREACH)
            self.state = 331
            self.match(D96Parser.LB)
            self.state = 332
            self.match(D96Parser.IDEN)
            self.state = 333
            self.match(D96Parser.IN)
            self.state = 334
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 335
            self.match(D96Parser.DDOT)
            self.state = 336
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 337
                self.match(D96Parser.BY)
                self.state = 338
                self.match(D96Parser.INTEGER_LITERAL)


            self.state = 341
            self.match(D96Parser.RB)
            self.state = 342
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(D96Parser.RETURN)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 345
                self.expr()


            self.state = 348
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Method_invocationContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_stmt" ):
                return visitor.visitMethod_invocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_stmt(self):

        localctx = D96Parser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.method_invocation()
            self.state = 351
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def DCOL(self):
            return self.getToken(D96Parser.DCOL, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation" ):
                return visitor.visitMethod_invocation(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation(self):

        localctx = D96Parser.Method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_method_invocation)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.expr()
                self.state = 354
                self.match(D96Parser.DOT)
                self.state = 355
                self.match(D96Parser.IDEN)
                self.state = 356
                self.match(D96Parser.LB)
                self.state = 357
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.expr()
                self.state = 360
                self.match(D96Parser.DOT)
                self.state = 361
                self.match(D96Parser.IDEN)
                self.state = 362
                self.match(D96Parser.LB)
                self.state = 363
                self.expr_list()
                self.state = 364
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 366
                self.expr()
                self.state = 367
                self.match(D96Parser.DCOL)
                self.state = 368
                self.match(D96Parser.DOL_IDEN)
                self.state = 369
                self.match(D96Parser.LB)
                self.state = 370
                self.match(D96Parser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 372
                self.expr()
                self.state = 373
                self.match(D96Parser.DCOL)
                self.state = 374
                self.match(D96Parser.DOL_IDEN)
                self.state = 375
                self.match(D96Parser.LB)
                self.state = 376
                self.expr_list()
                self.state = 377
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def OP_EQ_STR(self):
            return self.getToken(D96Parser.OP_EQ_STR, 0)

        def OP_ADD_STR(self):
            return self.getToken(D96Parser.OP_ADD_STR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.expr1()
                self.state = 382
                _la = self._input.LA(1)
                if not(_la==D96Parser.OP_EQ_STR or _la==D96Parser.OP_ADD_STR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 383
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


        def OP_LTE(self):
            return self.getToken(D96Parser.OP_LTE, 0)

        def OP_GTE(self):
            return self.getToken(D96Parser.OP_GTE, 0)

        def OP_NEQ(self):
            return self.getToken(D96Parser.OP_NEQ, 0)

        def OP_LT(self):
            return self.getToken(D96Parser.OP_LT, 0)

        def OP_GT(self):
            return self.getToken(D96Parser.OP_GT, 0)

        def OP_EQ(self):
            return self.getToken(D96Parser.OP_EQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.expr2(0)
                self.state = 389
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_LTE) | (1 << D96Parser.OP_GTE) | (1 << D96Parser.OP_NEQ) | (1 << D96Parser.OP_EQ) | (1 << D96Parser.OP_LT) | (1 << D96Parser.OP_GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 390
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def OP_AND(self):
            return self.getToken(D96Parser.OP_AND, 0)

        def OP_OR(self):
            return self.getToken(D96Parser.OP_OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 403
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 398
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 399
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_AND or _la==D96Parser.OP_OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 400
                    self.expr3(0) 
                self.state = 405
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def OP_ADD(self):
            return self.getToken(D96Parser.OP_ADD, 0)

        def OP_SUB(self):
            return self.getToken(D96Parser.OP_SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 414
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 409
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 410
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_ADD or _la==D96Parser.OP_SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 411
                    self.expr4(0) 
                self.state = 416
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def OP_MUL(self):
            return self.getToken(D96Parser.OP_MUL, 0)

        def OP_DIV(self):
            return self.getToken(D96Parser.OP_DIV, 0)

        def OP_MOD(self):
            return self.getToken(D96Parser.OP_MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 420
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 421
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_MUL) | (1 << D96Parser.OP_DIV) | (1 << D96Parser.OP_MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 422
                    self.expr5() 
                self.state = 427
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_NOT(self):
            return self.getToken(D96Parser.OP_NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr5)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.match(D96Parser.OP_NOT)
                self.state = 429
                self.expr5()
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.OP_SUB, D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.expr6()
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_SUB(self):
            return self.getToken(D96Parser.OP_SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr6)
        try:
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.match(D96Parser.OP_SUB)
                self.state = 434
                self.expr6()
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.expr7()
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = D96Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr7)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.expr8(0)
                self.state = 439
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.expr8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = D96Parser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_index_operators)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.match(D96Parser.LSB)
                self.state = 445
                self.expr()
                self.state = 446
                self.match(D96Parser.RSB)
                self.state = 447
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                self.match(D96Parser.LSB)
                self.state = 450
                self.expr()
                self.state = 451
                self.match(D96Parser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 475
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 473
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 458
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 459
                        self.match(D96Parser.DOT)
                        self.state = 460
                        self.match(D96Parser.IDEN)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 461
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 462
                        self.match(D96Parser.DOT)
                        self.state = 463
                        self.match(D96Parser.IDEN)
                        self.state = 464
                        self.match(D96Parser.LB)
                        self.state = 465
                        self.match(D96Parser.RB)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 466
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 467
                        self.match(D96Parser.DOT)
                        self.state = 468
                        self.match(D96Parser.IDEN)
                        self.state = 469
                        self.match(D96Parser.LB)
                        self.state = 470
                        self.expr_list()
                        self.state = 471
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 477
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def DCOL(self):
            return self.getToken(D96Parser.DCOL, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr9)
        try:
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.expr10()
                self.state = 479
                self.match(D96Parser.DCOL)
                self.state = 480
                self.match(D96Parser.DOL_IDEN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
                self.expr10()
                self.state = 483
                self.match(D96Parser.DCOL)
                self.state = 484
                self.match(D96Parser.DOL_IDEN)
                self.state = 485
                self.match(D96Parser.LB)
                self.state = 486
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 488
                self.expr10()
                self.state = 489
                self.match(D96Parser.DCOL)
                self.state = 490
                self.match(D96Parser.DOL_IDEN)
                self.state = 491
                self.match(D96Parser.LB)
                self.state = 492
                self.expr_list()
                self.state = 493
                self.match(D96Parser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 495
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def expr11(self):
            return self.getTypedRuleContext(D96Parser.Expr11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr10)
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.match(D96Parser.NEW)
                self.state = 499
                self.match(D96Parser.IDEN)
                self.state = 500
                self.match(D96Parser.LB)
                self.state = 501
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.match(D96Parser.NEW)
                self.state = 503
                self.match(D96Parser.IDEN)
                self.state = 504
                self.match(D96Parser.LB)
                self.state = 505
                self.expr_list()
                self.state = 506
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 508
                self.expr11()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = D96Parser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr11)
        try:
            self.state = 516
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.match(D96Parser.LB)
                self.state = 512
                self.expr()
                self.state = 513
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.operands()
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


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_operands)
        try:
            self.state = 522
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.match(D96Parser.IDEN)
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 519
                self.literal()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 520
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 521
                self.match(D96Parser.NULL)
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


    class List_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.LiteralContext)
            else:
                return self.getTypedRuleContext(D96Parser.LiteralContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COM)
            else:
                return self.getToken(D96Parser.COM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_list_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal" ):
                return visitor.visitList_literal(self)
            else:
                return visitor.visitChildren(self)




    def list_literal(self):

        localctx = D96Parser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_list_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 524
                    self.literal()
                    self.state = 525
                    self.match(D96Parser.COM) 
                self.state = 531
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

            self.state = 532
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(D96Parser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(D96Parser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def array(self):
            return self.getTypedRuleContext(D96Parser.ArrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_literal)
        try:
            self.state = 539
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 534
                self.match(D96Parser.INTEGER_LITERAL)
                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 535
                self.match(D96Parser.FLOAT_LITERAL)
                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 536
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 537
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 538
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def muldi_arr(self):
            return self.getTypedRuleContext(D96Parser.Muldi_arrContext,0)


        def indx_arr(self):
            return self.getTypedRuleContext(D96Parser.Indx_arrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = D96Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_array)
        try:
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.muldi_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 542
                self.indx_arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Muldi_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def array_list(self):
            return self.getTypedRuleContext(D96Parser.Array_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_muldi_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMuldi_arr" ):
                return visitor.visitMuldi_arr(self)
            else:
                return visitor.visitChildren(self)




    def muldi_arr(self):

        localctx = D96Parser.Muldi_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_muldi_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.match(D96Parser.ARRAY)
            self.state = 546
            self.match(D96Parser.LB)
            self.state = 547
            self.array_list()
            self.state = 548
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indx_arr(self):
            return self.getTypedRuleContext(D96Parser.Indx_arrContext,0)


        def COM(self):
            return self.getToken(D96Parser.COM, 0)

        def array_list(self):
            return self.getTypedRuleContext(D96Parser.Array_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = D96Parser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_array_list)
        try:
            self.state = 555
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 550
                self.indx_arr()
                self.state = 551
                self.match(D96Parser.COM)
                self.state = 552
                self.array_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 554
                self.indx_arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indx_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_indx_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndx_arr" ):
                return visitor.visitIndx_arr(self)
            else:
                return visitor.visitChildren(self)




    def indx_arr(self):

        localctx = D96Parser.Indx_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_indx_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(D96Parser.ARRAY)
            self.state = 558
            self.match(D96Parser.LB)
            self.state = 559
            self.expr_list()
            self.state = 560
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def COM(self):
            return self.getToken(D96Parser.COM, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.match(D96Parser.ARRAY)
            self.state = 563
            self.match(D96Parser.LSB)
            self.state = 564
            self.data_type()
            self.state = 565
            self.match(D96Parser.COM)
            self.state = 566
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 567
            self.match(D96Parser.RSB)
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
        self._predicates[35] = self.expr2_sempred
        self._predicates[36] = self.expr3_sempred
        self._predicates[37] = self.expr4_sempred
        self._predicates[42] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




