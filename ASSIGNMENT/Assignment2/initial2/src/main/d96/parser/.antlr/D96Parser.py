# Generated from d:\BK COURSE\HK212\PPL\Assignment\Assignment2\initial2\src\main\d96\parser\D96.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0204\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\6\2j\n\2\r\2\16\2k\3\2\3\2\3\3\3\3\3\3\3\3\7\3t\n")
        buf.write("\3\f\3\16\3w\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\u0080")
        buf.write("\n\3\f\3\16\3\u0083\13\3\3\3\5\3\u0086\n\3\3\4\3\4\5\4")
        buf.write("\u008a\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0092\n\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\5\6\u009b\n\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7\u00a4\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7")
        buf.write("\t\u00ad\n\t\f\t\16\t\u00b0\13\t\3\n\3\n\3\13\3\13\3\13")
        buf.write("\7\13\u00b7\n\13\f\13\16\13\u00ba\13\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\5\f\u00c2\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00c9")
        buf.write("\n\r\3\r\3\r\3\r\5\r\u00ce\n\r\3\16\3\16\3\16\5\16\u00d3")
        buf.write("\n\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\7\20\u00e0\n\20\f\20\16\20\u00e3\13\20\3\21\3\21")
        buf.write("\3\22\3\22\7\22\u00e9\n\22\f\22\16\22\u00ec\13\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00f9\n\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3")
        buf.write("\26\3\26\5\26\u0105\n\26\3\27\3\27\3\27\3\27\3\27\6\27")
        buf.write("\u010c\n\27\r\27\16\27\u010d\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\5\30\u0118\n\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\5\31\u0120\n\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\5\32\u0128\n\32\3\32\3\32\5\32\u012c\n\32\3\33\3\33\3")
        buf.write("\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\5\35\u013d\n\35\3\35\3\35\3\35\3\36\3\36\5")
        buf.write("\36\u0144\n\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \5 \u0150\n \3 \3 \5 \u0154\n \3 \3 \3!\3!\3!\3!\3!\5")
        buf.write("!\u015d\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0164\n\"\3#\3#\3#")
        buf.write("\3#\3#\3#\7#\u016c\n#\f#\16#\u016f\13#\3$\3$\3$\3$\3$")
        buf.write("\3$\7$\u0177\n$\f$\16$\u017a\13$\3%\3%\3%\3%\3%\3%\7%")
        buf.write("\u0182\n%\f%\16%\u0185\13%\3&\3&\3&\5&\u018a\n&\3\'\3")
        buf.write("\'\3\'\5\'\u018f\n\'\3(\3(\3(\3(\3(\6(\u0196\n(\r(\16")
        buf.write("(\u0197\3(\5(\u019b\n(\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01a5")
        buf.write("\n)\3)\5)\u01a8\n)\7)\u01aa\n)\f)\16)\u01ad\13)\3*\3*")
        buf.write("\3*\3*\3*\3*\3*\3*\5*\u01b7\n*\3*\5*\u01ba\n*\7*\u01bc")
        buf.write("\n*\f*\16*\u01bf\13*\3+\3+\3+\3+\5+\u01c5\n+\3+\3+\5+")
        buf.write("\u01c9\n+\3,\3,\3,\3,\3,\5,\u01d0\n,\3-\3-\3-\3-\5-\u01d6")
        buf.write("\n-\3.\3.\3.\7.\u01db\n.\f.\16.\u01de\13.\3/\3/\3/\3/")
        buf.write("\3/\5/\u01e5\n/\3\60\3\60\5\60\u01e9\n\60\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\62\3\62\3\62\7\62\u01f3\n\62\f\62\16\62")
        buf.write("\u01f6\13\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\2\7DFHPR\65\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdf\2\b\3\2;<\3\29:\4\2\62\64\668\3\2\60\61")
        buf.write("\3\2*+\3\2,.\2\u0214\2i\3\2\2\2\4\u0085\3\2\2\2\6\u0089")
        buf.write("\3\2\2\2\b\u0091\3\2\2\2\n\u009a\3\2\2\2\f\u00a3\3\2\2")
        buf.write("\2\16\u00a5\3\2\2\2\20\u00a9\3\2\2\2\22\u00b1\3\2\2\2")
        buf.write("\24\u00b3\3\2\2\2\26\u00c1\3\2\2\2\30\u00cd\3\2\2\2\32")
        buf.write("\u00cf\3\2\2\2\34\u00d7\3\2\2\2\36\u00dc\3\2\2\2 \u00e4")
        buf.write("\3\2\2\2\"\u00e6\3\2\2\2$\u00f8\3\2\2\2&\u00fa\3\2\2\2")
        buf.write("(\u00fd\3\2\2\2*\u0104\3\2\2\2,\u0106\3\2\2\2.\u0117\3")
        buf.write("\2\2\2\60\u0119\3\2\2\2\62\u012b\3\2\2\2\64\u012d\3\2")
        buf.write("\2\2\66\u0130\3\2\2\28\u0133\3\2\2\2:\u0141\3\2\2\2<\u0147")
        buf.write("\3\2\2\2>\u014a\3\2\2\2@\u015c\3\2\2\2B\u0163\3\2\2\2")
        buf.write("D\u0165\3\2\2\2F\u0170\3\2\2\2H\u017b\3\2\2\2J\u0189\3")
        buf.write("\2\2\2L\u018e\3\2\2\2N\u019a\3\2\2\2P\u019c\3\2\2\2R\u01ae")
        buf.write("\3\2\2\2T\u01c8\3\2\2\2V\u01cf\3\2\2\2X\u01d5\3\2\2\2")
        buf.write("Z\u01d7\3\2\2\2\\\u01e4\3\2\2\2^\u01e8\3\2\2\2`\u01ea")
        buf.write("\3\2\2\2b\u01ef\3\2\2\2d\u01f7\3\2\2\2f\u01fc\3\2\2\2")
        buf.write("hj\5\4\3\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2\2lm\3")
        buf.write("\2\2\2mn\7\2\2\3n\3\3\2\2\2op\7\21\2\2pq\7;\2\2qu\7\t")
        buf.write("\2\2rt\5\6\4\2sr\3\2\2\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2")
        buf.write("vx\3\2\2\2wu\3\2\2\2x\u0086\7\n\2\2yz\7\21\2\2z{\7;\2")
        buf.write("\2{|\7\16\2\2|}\7;\2\2}\u0081\7\t\2\2~\u0080\5\6\4\2\177")
        buf.write("~\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3\2\2\2\u0081")
        buf.write("\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081\3\2\2\2")
        buf.write("\u0084\u0086\7\n\2\2\u0085o\3\2\2\2\u0085y\3\2\2\2\u0086")
        buf.write("\5\3\2\2\2\u0087\u008a\5\b\5\2\u0088\u008a\5\30\r\2\u0089")
        buf.write("\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a\7\3\2\2\2\u008b")
        buf.write("\u008c\5\n\6\2\u008c\u008d\7\r\2\2\u008d\u0092\3\2\2\2")
        buf.write("\u008e\u008f\5\f\7\2\u008f\u0090\7\r\2\2\u0090\u0092\3")
        buf.write("\2\2\2\u0091\u008b\3\2\2\2\u0091\u008e\3\2\2\2\u0092\t")
        buf.write("\3\2\2\2\u0093\u0094\7\22\2\2\u0094\u0095\5\16\b\2\u0095")
        buf.write("\u0096\7\65\2\2\u0096\u0097\5\24\13\2\u0097\u009b\3\2")
        buf.write("\2\2\u0098\u0099\7\22\2\2\u0099\u009b\5\16\b\2\u009a\u0093")
        buf.write("\3\2\2\2\u009a\u0098\3\2\2\2\u009b\13\3\2\2\2\u009c\u009d")
        buf.write("\7\23\2\2\u009d\u009e\5\16\b\2\u009e\u009f\7\65\2\2\u009f")
        buf.write("\u00a0\5\24\13\2\u00a0\u00a4\3\2\2\2\u00a1\u00a2\7\23")
        buf.write("\2\2\u00a2\u00a4\5\16\b\2\u00a3\u009c\3\2\2\2\u00a3\u00a1")
        buf.write("\3\2\2\2\u00a4\r\3\2\2\2\u00a5\u00a6\5\20\t\2\u00a6\u00a7")
        buf.write("\7\16\2\2\u00a7\u00a8\5\26\f\2\u00a8\17\3\2\2\2\u00a9")
        buf.write("\u00ae\5\22\n\2\u00aa\u00ab\7\20\2\2\u00ab\u00ad\5\22")
        buf.write("\n\2\u00ac\u00aa\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac")
        buf.write("\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\21\3\2\2\2\u00b0\u00ae")
        buf.write("\3\2\2\2\u00b1\u00b2\t\2\2\2\u00b2\23\3\2\2\2\u00b3\u00b8")
        buf.write("\5@!\2\u00b4\u00b5\7\20\2\2\u00b5\u00b7\5@!\2\u00b6\u00b4")
        buf.write("\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8")
        buf.write("\u00b9\3\2\2\2\u00b9\25\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb")
        buf.write("\u00c2\7\26\2\2\u00bc\u00c2\7\27\2\2\u00bd\u00c2\7\31")
        buf.write("\2\2\u00be\u00c2\7\30\2\2\u00bf\u00c2\5f\64\2\u00c0\u00c2")
        buf.write("\7;\2\2\u00c1\u00bb\3\2\2\2\u00c1\u00bc\3\2\2\2\u00c1")
        buf.write("\u00bd\3\2\2\2\u00c1\u00be\3\2\2\2\u00c1\u00bf\3\2\2\2")
        buf.write("\u00c1\u00c0\3\2\2\2\u00c2\27\3\2\2\2\u00c3\u00ce\5\32")
        buf.write("\16\2\u00c4\u00ce\5\34\17\2\u00c5\u00c6\5\22\n\2\u00c6")
        buf.write("\u00c8\7\7\2\2\u00c7\u00c9\5\36\20\2\u00c8\u00c7\3\2\2")
        buf.write("\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb")
        buf.write("\7\b\2\2\u00cb\u00cc\5\"\22\2\u00cc\u00ce\3\2\2\2\u00cd")
        buf.write("\u00c3\3\2\2\2\u00cd\u00c4\3\2\2\2\u00cd\u00c5\3\2\2\2")
        buf.write("\u00ce\31\3\2\2\2\u00cf\u00d0\7$\2\2\u00d0\u00d2\7\7\2")
        buf.write("\2\u00d1\u00d3\5\36\20\2\u00d2\u00d1\3\2\2\2\u00d2\u00d3")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\7\b\2\2\u00d5")
        buf.write("\u00d6\5\"\22\2\u00d6\33\3\2\2\2\u00d7\u00d8\7%\2\2\u00d8")
        buf.write("\u00d9\7\7\2\2\u00d9\u00da\7\b\2\2\u00da\u00db\5\"\22")
        buf.write("\2\u00db\35\3\2\2\2\u00dc\u00e1\5 \21\2\u00dd\u00de\7")
        buf.write("\r\2\2\u00de\u00e0\5 \21\2\u00df\u00dd\3\2\2\2\u00e0\u00e3")
        buf.write("\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("\37\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5\5\16\b\2\u00e5")
        buf.write("!\3\2\2\2\u00e6\u00ea\7\t\2\2\u00e7\u00e9\5$\23\2\u00e8")
        buf.write("\u00e7\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2")
        buf.write("\u00ea\u00eb\3\2\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00ea\3")
        buf.write("\2\2\2\u00ed\u00ee\7\n\2\2\u00ee#\3\2\2\2\u00ef\u00f9")
        buf.write("\5&\24\2\u00f0\u00f9\5\b\5\2\u00f1\u00f9\5\60\31\2\u00f2")
        buf.write("\u00f9\5\64\33\2\u00f3\u00f9\5\66\34\2\u00f4\u00f9\58")
        buf.write("\35\2\u00f5\u00f9\5:\36\2\u00f6\u00f9\5<\37\2\u00f7\u00f9")
        buf.write("\5\"\22\2\u00f8\u00ef\3\2\2\2\u00f8\u00f0\3\2\2\2\u00f8")
        buf.write("\u00f1\3\2\2\2\u00f8\u00f2\3\2\2\2\u00f8\u00f3\3\2\2\2")
        buf.write("\u00f8\u00f4\3\2\2\2\u00f8\u00f5\3\2\2\2\u00f8\u00f6\3")
        buf.write("\2\2\2\u00f8\u00f7\3\2\2\2\u00f9%\3\2\2\2\u00fa\u00fb")
        buf.write("\5(\25\2\u00fb\u00fc\7\r\2\2\u00fc\'\3\2\2\2\u00fd\u00fe")
        buf.write("\5*\26\2\u00fe\u00ff\7\65\2\2\u00ff\u0100\5@!\2\u0100")
        buf.write(")\3\2\2\2\u0101\u0105\7;\2\2\u0102\u0105\5,\27\2\u0103")
        buf.write("\u0105\5.\30\2\u0104\u0101\3\2\2\2\u0104\u0102\3\2\2\2")
        buf.write("\u0104\u0103\3\2\2\2\u0105+\3\2\2\2\u0106\u010b\5P)\2")
        buf.write("\u0107\u0108\7\13\2\2\u0108\u0109\5@!\2\u0109\u010a\7")
        buf.write("\f\2\2\u010a\u010c\3\2\2\2\u010b\u0107\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e")
        buf.write("-\3\2\2\2\u010f\u0110\5@!\2\u0110\u0111\7(\2\2\u0111\u0112")
        buf.write("\7;\2\2\u0112\u0118\3\2\2\2\u0113\u0114\5@!\2\u0114\u0115")
        buf.write("\7\17\2\2\u0115\u0116\7<\2\2\u0116\u0118\3\2\2\2\u0117")
        buf.write("\u010f\3\2\2\2\u0117\u0113\3\2\2\2\u0118/\3\2\2\2\u0119")
        buf.write("\u011a\7\35\2\2\u011a\u011b\7\7\2\2\u011b\u011c\5@!\2")
        buf.write("\u011c\u011d\7\b\2\2\u011d\u011f\5\"\22\2\u011e\u0120")
        buf.write("\5\62\32\2\u011f\u011e\3\2\2\2\u011f\u0120\3\2\2\2\u0120")
        buf.write("\61\3\2\2\2\u0121\u0122\7\36\2\2\u0122\u0123\7\7\2\2\u0123")
        buf.write("\u0124\5@!\2\u0124\u0125\7\b\2\2\u0125\u0127\5\"\22\2")
        buf.write("\u0126\u0128\5\62\32\2\u0127\u0126\3\2\2\2\u0127\u0128")
        buf.write("\3\2\2\2\u0128\u012c\3\2\2\2\u0129\u012a\7\37\2\2\u012a")
        buf.write("\u012c\5\"\22\2\u012b\u0121\3\2\2\2\u012b\u0129\3\2\2")
        buf.write("\2\u012c\63\3\2\2\2\u012d\u012e\7\33\2\2\u012e\u012f\7")
        buf.write("\r\2\2\u012f\65\3\2\2\2\u0130\u0131\7\34\2\2\u0131\u0132")
        buf.write("\7\r\2\2\u0132\67\3\2\2\2\u0133\u0134\7 \2\2\u0134\u0135")
        buf.write("\7\7\2\2\u0135\u0136\7;\2\2\u0136\u0137\7&\2\2\u0137\u0138")
        buf.write("\7\4\2\2\u0138\u0139\7)\2\2\u0139\u013c\7\4\2\2\u013a")
        buf.write("\u013b\7\'\2\2\u013b\u013d\7\4\2\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013d\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u013f\7")
        buf.write("\b\2\2\u013f\u0140\5\"\22\2\u01409\3\2\2\2\u0141\u0143")
        buf.write("\7!\2\2\u0142\u0144\5@!\2\u0143\u0142\3\2\2\2\u0143\u0144")
        buf.write("\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\7\r\2\2\u0146")
        buf.write(";\3\2\2\2\u0147\u0148\5> \2\u0148\u0149\7\r\2\2\u0149")
        buf.write("=\3\2\2\2\u014a\u014f\5@!\2\u014b\u014c\7(\2\2\u014c\u0150")
        buf.write("\7;\2\2\u014d\u014e\7\17\2\2\u014e\u0150\7<\2\2\u014f")
        buf.write("\u014b\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151\u0153\7\7\2\2\u0152\u0154\5\24\13\2\u0153\u0152")
        buf.write("\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155\3\2\2\2\u0155")
        buf.write("\u0156\7\b\2\2\u0156?\3\2\2\2\u0157\u0158\5B\"\2\u0158")
        buf.write("\u0159\t\3\2\2\u0159\u015a\5B\"\2\u015a\u015d\3\2\2\2")
        buf.write("\u015b\u015d\5B\"\2\u015c\u0157\3\2\2\2\u015c\u015b\3")
        buf.write("\2\2\2\u015dA\3\2\2\2\u015e\u015f\5D#\2\u015f\u0160\t")
        buf.write("\4\2\2\u0160\u0161\5D#\2\u0161\u0164\3\2\2\2\u0162\u0164")
        buf.write("\5D#\2\u0163\u015e\3\2\2\2\u0163\u0162\3\2\2\2\u0164C")
        buf.write("\3\2\2\2\u0165\u0166\b#\1\2\u0166\u0167\5F$\2\u0167\u016d")
        buf.write("\3\2\2\2\u0168\u0169\f\4\2\2\u0169\u016a\t\5\2\2\u016a")
        buf.write("\u016c\5F$\2\u016b\u0168\3\2\2\2\u016c\u016f\3\2\2\2\u016d")
        buf.write("\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016eE\3\2\2\2\u016f")
        buf.write("\u016d\3\2\2\2\u0170\u0171\b$\1\2\u0171\u0172\5H%\2\u0172")
        buf.write("\u0178\3\2\2\2\u0173\u0174\f\4\2\2\u0174\u0175\t\6\2\2")
        buf.write("\u0175\u0177\5H%\2\u0176\u0173\3\2\2\2\u0177\u017a\3\2")
        buf.write("\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179G\3")
        buf.write("\2\2\2\u017a\u0178\3\2\2\2\u017b\u017c\b%\1\2\u017c\u017d")
        buf.write("\5J&\2\u017d\u0183\3\2\2\2\u017e\u017f\f\4\2\2\u017f\u0180")
        buf.write("\t\7\2\2\u0180\u0182\5J&\2\u0181\u017e\3\2\2\2\u0182\u0185")
        buf.write("\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("I\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0187\7/\2\2\u0187")
        buf.write("\u018a\5J&\2\u0188\u018a\5L\'\2\u0189\u0186\3\2\2\2\u0189")
        buf.write("\u0188\3\2\2\2\u018aK\3\2\2\2\u018b\u018c\7+\2\2\u018c")
        buf.write("\u018f\5L\'\2\u018d\u018f\5N(\2\u018e\u018b\3\2\2\2\u018e")
        buf.write("\u018d\3\2\2\2\u018fM\3\2\2\2\u0190\u0195\5P)\2\u0191")
        buf.write("\u0192\7\13\2\2\u0192\u0193\5@!\2\u0193\u0194\7\f\2\2")
        buf.write("\u0194\u0196\3\2\2\2\u0195\u0191\3\2\2\2\u0196\u0197\3")
        buf.write("\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u019b")
        buf.write("\3\2\2\2\u0199\u019b\5P)\2\u019a\u0190\3\2\2\2\u019a\u0199")
        buf.write("\3\2\2\2\u019bO\3\2\2\2\u019c\u019d\b)\1\2\u019d\u019e")
        buf.write("\5R*\2\u019e\u01ab\3\2\2\2\u019f\u01a0\f\4\2\2\u01a0\u01a1")
        buf.write("\7(\2\2\u01a1\u01a7\7;\2\2\u01a2\u01a4\7\7\2\2\u01a3\u01a5")
        buf.write("\5\24\13\2\u01a4\u01a3\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\u01a8\7\b\2\2\u01a7\u01a2\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u019f\3")
        buf.write("\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac")
        buf.write("\3\2\2\2\u01acQ\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01af")
        buf.write("\b*\1\2\u01af\u01b0\5T+\2\u01b0\u01bd\3\2\2\2\u01b1\u01b2")
        buf.write("\f\4\2\2\u01b2\u01b3\7\17\2\2\u01b3\u01b9\7<\2\2\u01b4")
        buf.write("\u01b6\7\7\2\2\u01b5\u01b7\5\24\13\2\u01b6\u01b5\3\2\2")
        buf.write("\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01ba")
        buf.write("\7\b\2\2\u01b9\u01b4\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba")
        buf.write("\u01bc\3\2\2\2\u01bb\u01b1\3\2\2\2\u01bc\u01bf\3\2\2\2")
        buf.write("\u01bd\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01beS\3\2\2")
        buf.write("\2\u01bf\u01bd\3\2\2\2\u01c0\u01c1\7#\2\2\u01c1\u01c2")
        buf.write("\7;\2\2\u01c2\u01c4\7\7\2\2\u01c3\u01c5\5\24\13\2\u01c4")
        buf.write("\u01c3\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c9\7\b\2\2\u01c7\u01c9\5V,\2\u01c8\u01c0\3\2")
        buf.write("\2\2\u01c8\u01c7\3\2\2\2\u01c9U\3\2\2\2\u01ca\u01cb\7")
        buf.write("\7\2\2\u01cb\u01cc\5@!\2\u01cc\u01cd\7\b\2\2\u01cd\u01d0")
        buf.write("\3\2\2\2\u01ce\u01d0\5X-\2\u01cf\u01ca\3\2\2\2\u01cf\u01ce")
        buf.write("\3\2\2\2\u01d0W\3\2\2\2\u01d1\u01d6\7;\2\2\u01d2\u01d6")
        buf.write("\5\\/\2\u01d3\u01d6\7\"\2\2\u01d4\u01d6\7\32\2\2\u01d5")
        buf.write("\u01d1\3\2\2\2\u01d5\u01d2\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d5\u01d4\3\2\2\2\u01d6Y\3\2\2\2\u01d7\u01dc\5\\/\2")
        buf.write("\u01d8\u01d9\7\20\2\2\u01d9\u01db\5\\/\2\u01da\u01d8\3")
        buf.write("\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd")
        buf.write("\3\2\2\2\u01dd[\3\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e5")
        buf.write("\7\4\2\2\u01e0\u01e5\7\3\2\2\u01e1\u01e5\7\5\2\2\u01e2")
        buf.write("\u01e5\7\6\2\2\u01e3\u01e5\5^\60\2\u01e4\u01df\3\2\2\2")
        buf.write("\u01e4\u01e0\3\2\2\2\u01e4\u01e1\3\2\2\2\u01e4\u01e2\3")
        buf.write("\2\2\2\u01e4\u01e3\3\2\2\2\u01e5]\3\2\2\2\u01e6\u01e9")
        buf.write("\5`\61\2\u01e7\u01e9\5d\63\2\u01e8\u01e6\3\2\2\2\u01e8")
        buf.write("\u01e7\3\2\2\2\u01e9_\3\2\2\2\u01ea\u01eb\7\25\2\2\u01eb")
        buf.write("\u01ec\7\7\2\2\u01ec\u01ed\5b\62\2\u01ed\u01ee\7\b\2\2")
        buf.write("\u01eea\3\2\2\2\u01ef\u01f4\5d\63\2\u01f0\u01f1\7\20\2")
        buf.write("\2\u01f1\u01f3\5d\63\2\u01f2\u01f0\3\2\2\2\u01f3\u01f6")
        buf.write("\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5")
        buf.write("c\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f8\7\25\2\2\u01f8")
        buf.write("\u01f9\7\7\2\2\u01f9\u01fa\5\24\13\2\u01fa\u01fb\7\b\2")
        buf.write("\2\u01fbe\3\2\2\2\u01fc\u01fd\7\25\2\2\u01fd\u01fe\7\13")
        buf.write("\2\2\u01fe\u01ff\5\26\f\2\u01ff\u0200\7\20\2\2\u0200\u0201")
        buf.write("\7\4\2\2\u0201\u0202\7\f\2\2\u0202g\3\2\2\2\64ku\u0081")
        buf.write("\u0085\u0089\u0091\u009a\u00a3\u00ae\u00b8\u00c1\u00c8")
        buf.write("\u00cd\u00d2\u00e1\u00ea\u00f8\u0104\u010d\u0117\u011f")
        buf.write("\u0127\u012b\u013c\u0143\u014f\u0153\u015c\u0163\u016d")
        buf.write("\u0178\u0183\u0189\u018e\u0197\u019a\u01a4\u01a7\u01ab")
        buf.write("\u01b6\u01b9\u01bd\u01c4\u01c8\u01cf\u01d5\u01dc\u01e4")
        buf.write("\u01e8\u01f4")
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
                     "'Elseif'", "'Else'", "'Foreach'", "'Return'", "'Self'", 
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
    RULE_param_decl = 15
    RULE_block_stmt = 16
    RULE_block_item = 17
    RULE_assign_stmt = 18
    RULE_assign_lhs = 19
    RULE_lhs = 20
    RULE_array_operator = 21
    RULE_field_access = 22
    RULE_if_stmt = 23
    RULE_else_stmt = 24
    RULE_break_stmt = 25
    RULE_continue_stmt = 26
    RULE_forin_stmt = 27
    RULE_return_stmt = 28
    RULE_method_invocation_stmt = 29
    RULE_method_invocation = 30
    RULE_expr = 31
    RULE_expr1 = 32
    RULE_expr2 = 33
    RULE_expr3 = 34
    RULE_expr4 = 35
    RULE_expr5 = 36
    RULE_expr6 = 37
    RULE_expr7 = 38
    RULE_expr8 = 39
    RULE_expr9 = 40
    RULE_expr10 = 41
    RULE_expr11 = 42
    RULE_operands = 43
    RULE_list_literal = 44
    RULE_literal = 45
    RULE_array = 46
    RULE_muldi_arr = 47
    RULE_array_list = 48
    RULE_indx_arr = 49
    RULE_array_type = 50

    ruleNames =  [ "program", "class_decl", "mem_decl", "attr_decl", "immutable_attr", 
                   "mutable_attr", "id_list_type", "id_list", "iden_dol", 
                   "expr_list", "data_type", "method_decl", "constr_decl", 
                   "destr_decl", "params_list", "param_decl", "block_stmt", 
                   "block_item", "assign_stmt", "assign_lhs", "lhs", "array_operator", 
                   "field_access", "if_stmt", "else_stmt", "break_stmt", 
                   "continue_stmt", "forin_stmt", "return_stmt", "method_invocation_stmt", 
                   "method_invocation", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "expr8", "expr9", 
                   "expr10", "expr11", "operands", "list_literal", "literal", 
                   "array", "muldi_arr", "array_list", "indx_arr", "array_type" ]

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
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

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




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.class_decl()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 107
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Class_declContext(ParserRuleContext):

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




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(D96Parser.CLASS)
                self.state = 110
                self.match(D96Parser.IDEN)
                self.state = 111
                self.match(D96Parser.LP)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDEN) | (1 << D96Parser.DOL_IDEN))) != 0):
                    self.state = 112
                    self.mem_decl()
                    self.state = 117
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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
                self.match(D96Parser.COL)
                self.state = 122
                self.match(D96Parser.IDEN)
                self.state = 123
                self.match(D96Parser.LP)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDEN) | (1 << D96Parser.DOL_IDEN))) != 0):
                    self.state = 124
                    self.mem_decl()
                    self.state = 129
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 130
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_decl(self):
            return self.getTypedRuleContext(D96Parser.Attr_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(D96Parser.Method_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mem_decl




    def mem_decl(self):

        localctx = D96Parser.Mem_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mem_decl)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.attr_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.IDEN, D96Parser.DOL_IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
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




    def attr_decl(self):

        localctx = D96Parser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attr_decl)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.immutable_attr()
                self.state = 138
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.mutable_attr()
                self.state = 141
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




    def immutable_attr(self):

        localctx = D96Parser.Immutable_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_immutable_attr)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(D96Parser.VAL)
                self.state = 146
                self.id_list_type()
                self.state = 147
                self.match(D96Parser.OP_AS)
                self.state = 148
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(D96Parser.VAL)
                self.state = 151
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




    def mutable_attr(self):

        localctx = D96Parser.Mutable_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mutable_attr)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(D96Parser.VAR)
                self.state = 155
                self.id_list_type()
                self.state = 156
                self.match(D96Parser.OP_AS)
                self.state = 157
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(D96Parser.VAR)
                self.state = 160
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




    def id_list_type(self):

        localctx = D96Parser.Id_list_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_id_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.id_list()
            self.state = 164
            self.match(D96Parser.COL)
            self.state = 165
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Id_listContext(ParserRuleContext):

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




    def id_list(self):

        localctx = D96Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.iden_dol()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COM:
                self.state = 168
                self.match(D96Parser.COM)
                self.state = 169
                self.iden_dol()
                self.state = 174
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_iden_dol




    def iden_dol(self):

        localctx = D96Parser.Iden_dolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_iden_dol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
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




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.expr()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COM:
                self.state = 178
                self.match(D96Parser.COM)
                self.state = 179
                self.expr()
                self.state = 184
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


        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_data_type




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_data_type)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 189
                self.array_type()
                pass
            elif token in [D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 190
                self.match(D96Parser.IDEN)
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




    def method_decl(self):

        localctx = D96Parser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.constr_decl()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.destr_decl()
                pass
            elif token in [D96Parser.IDEN, D96Parser.DOL_IDEN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.iden_dol()
                self.state = 196
                self.match(D96Parser.LB)
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDEN or _la==D96Parser.DOL_IDEN:
                    self.state = 197
                    self.params_list()


                self.state = 200
                self.match(D96Parser.RB)
                self.state = 201
                self.block_stmt()
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

    class Constr_declContext(ParserRuleContext):

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




    def constr_decl(self):

        localctx = D96Parser.Constr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_constr_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 206
            self.match(D96Parser.LB)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.IDEN or _la==D96Parser.DOL_IDEN:
                self.state = 207
                self.params_list()


            self.state = 210
            self.match(D96Parser.RB)
            self.state = 211
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Destr_declContext(ParserRuleContext):

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




    def destr_decl(self):

        localctx = D96Parser.Destr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_destr_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(D96Parser.DESTRUCTOR)
            self.state = 214
            self.match(D96Parser.LB)
            self.state = 215
            self.match(D96Parser.RB)
            self.state = 216
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Params_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Param_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Param_declContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_params_list




    def params_list(self):

        localctx = D96Parser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.param_decl()
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 219
                self.match(D96Parser.SEMI)
                self.state = 220
                self.param_decl()
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Param_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list_type(self):
            return self.getTypedRuleContext(D96Parser.Id_list_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param_decl




    def param_decl(self):

        localctx = D96Parser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.id_list_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Block_stmtContext(ParserRuleContext):

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




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(D96Parser.LP)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 229
                self.block_item()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Block_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def attr_decl(self):
            return self.getTypedRuleContext(D96Parser.Attr_declContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


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




    def block_item(self):

        localctx = D96Parser.Block_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block_item)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.attr_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 240
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 241
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 242
                self.forin_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 243
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 244
                self.method_invocation_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 245
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhsContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.assign_lhs()
            self.state = 249
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_lhsContext(ParserRuleContext):

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




    def assign_lhs(self):

        localctx = D96Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assign_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.lhs()
            self.state = 252
            self.match(D96Parser.OP_AS)
            self.state = 253
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LhsContext(ParserRuleContext):

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




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lhs)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(D96Parser.IDEN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.array_operator()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LSB)
            else:
                return self.getToken(D96Parser.LSB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RSB)
            else:
                return self.getToken(D96Parser.RSB, i)

        def getRuleIndex(self):
            return D96Parser.RULE_array_operator




    def array_operator(self):

        localctx = D96Parser.Array_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.expr8(0)
            self.state = 265 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 261
                self.match(D96Parser.LSB)
                self.state = 262
                self.expr()
                self.state = 263
                self.match(D96Parser.RSB)
                self.state = 267 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.LSB):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_accessContext(ParserRuleContext):

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




    def field_access(self):

        localctx = D96Parser.Field_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_field_access)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.expr()
                self.state = 270
                self.match(D96Parser.DOT)
                self.state = 271
                self.match(D96Parser.IDEN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.expr()
                self.state = 274
                self.match(D96Parser.DCOL)
                self.state = 275
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


        def else_stmt(self):
            return self.getTypedRuleContext(D96Parser.Else_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(D96Parser.IF)
            self.state = 280
            self.match(D96Parser.LB)
            self.state = 281
            self.expr()
            self.state = 282
            self.match(D96Parser.RB)
            self.state = 283
            self.block_stmt()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSEIF or _la==D96Parser.ELSE:
                self.state = 284
                self.else_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_stmtContext(ParserRuleContext):

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


        def else_stmt(self):
            return self.getTypedRuleContext(D96Parser.Else_stmtContext,0)


        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_else_stmt




    def else_stmt(self):

        localctx = D96Parser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_else_stmt)
        self._la = 0 # Token type
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(D96Parser.ELSEIF)
                self.state = 288
                self.match(D96Parser.LB)
                self.state = 289
                self.expr()
                self.state = 290
                self.match(D96Parser.RB)
                self.state = 291
                self.block_stmt()
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.ELSEIF or _la==D96Parser.ELSE:
                    self.state = 292
                    self.else_stmt()


                pass
            elif token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(D96Parser.ELSE)
                self.state = 296
                self.block_stmt()
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

    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(D96Parser.BREAK)
            self.state = 300
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(D96Parser.CONTINUE)
            self.state = 303
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Forin_stmtContext(ParserRuleContext):

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




    def forin_stmt(self):

        localctx = D96Parser.Forin_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_forin_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(D96Parser.FOREACH)
            self.state = 306
            self.match(D96Parser.LB)
            self.state = 307
            self.match(D96Parser.IDEN)
            self.state = 308
            self.match(D96Parser.IN)
            self.state = 309
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 310
            self.match(D96Parser.DDOT)
            self.state = 311
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 312
                self.match(D96Parser.BY)
                self.state = 313
                self.match(D96Parser.INTEGER_LITERAL)


            self.state = 316
            self.match(D96Parser.RB)
            self.state = 317
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_stmtContext(ParserRuleContext):

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




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(D96Parser.RETURN)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 320
                self.expr()


            self.state = 323
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_invocation_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Method_invocationContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_stmt




    def method_invocation_stmt(self):

        localctx = D96Parser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.method_invocation()
            self.state = 326
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_invocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def DCOL(self):
            return self.getToken(D96Parser.DCOL, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation




    def method_invocation(self):

        localctx = D96Parser.Method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_method_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.expr()
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOT]:
                self.state = 329
                self.match(D96Parser.DOT)
                self.state = 330
                self.match(D96Parser.IDEN)
                pass
            elif token in [D96Parser.DCOL]:
                self.state = 331
                self.match(D96Parser.DCOL)
                self.state = 332
                self.match(D96Parser.DOL_IDEN)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 335
            self.match(D96Parser.LB)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 336
                self.expr_list()


            self.state = 339
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

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




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.expr1()
                self.state = 342
                _la = self._input.LA(1)
                if not(_la==D96Parser.OP_EQ_STR or _la==D96Parser.OP_ADD_STR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 343
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
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




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.expr2(0)
                self.state = 349
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_LTE) | (1 << D96Parser.OP_GTE) | (1 << D96Parser.OP_NEQ) | (1 << D96Parser.OP_EQ) | (1 << D96Parser.OP_LT) | (1 << D96Parser.OP_GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 350
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
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



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 358
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 359
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_AND or _la==D96Parser.OP_OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 360
                    self.expr3(0) 
                self.state = 365
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr3Context(ParserRuleContext):

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



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 369
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 370
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_ADD or _la==D96Parser.OP_SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 371
                    self.expr4(0) 
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr4Context(ParserRuleContext):

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



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 385
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 380
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 381
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_MUL) | (1 << D96Parser.OP_DIV) | (1 << D96Parser.OP_MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 382
                    self.expr5() 
                self.state = 387
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr5Context(ParserRuleContext):

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




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr5)
        try:
            self.state = 391
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.match(D96Parser.OP_NOT)
                self.state = 389
                self.expr5()
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.OP_SUB, D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
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




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr6)
        try:
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.match(D96Parser.OP_SUB)
                self.state = 394
                self.expr6()
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LSB)
            else:
                return self.getToken(D96Parser.LSB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RSB)
            else:
                return self.getToken(D96Parser.RSB, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expr7




    def expr7(self):

        localctx = D96Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr7)
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.expr8(0)
                self.state = 403 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 399
                        self.match(D96Parser.LSB)
                        self.state = 400
                        self.expr()
                        self.state = 401
                        self.match(D96Parser.RSB)

                    else:
                        raise NoViableAltException(self)
                    self.state = 405 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.expr8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr8Context(ParserRuleContext):

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



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.expr9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 413
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 414
                    self.match(D96Parser.DOT)
                    self.state = 415
                    self.match(D96Parser.IDEN)
                    self.state = 421
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 416
                        self.match(D96Parser.LB)
                        self.state = 418
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                            self.state = 417
                            self.expr_list()


                        self.state = 420
                        self.match(D96Parser.RB)

             
                self.state = 427
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


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



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr9, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.expr10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 443
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                    self.state = 431
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 432
                    self.match(D96Parser.DCOL)
                    self.state = 433
                    self.match(D96Parser.DOL_IDEN)
                    self.state = 439
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        self.state = 434
                        self.match(D96Parser.LB)
                        self.state = 436
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                            self.state = 435
                            self.expr_list()


                        self.state = 438
                        self.match(D96Parser.RB)

             
                self.state = 445
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr10Context(ParserRuleContext):

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




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.state = 454
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(D96Parser.NEW)
                self.state = 447
                self.match(D96Parser.IDEN)
                self.state = 448
                self.match(D96Parser.LB)
                self.state = 450
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                    self.state = 449
                    self.expr_list()


                self.state = 452
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.expr11()
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

    class Expr11Context(ParserRuleContext):

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




    def expr11(self):

        localctx = D96Parser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr11)
        try:
            self.state = 461
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.match(D96Parser.LB)
                self.state = 457
                self.expr()
                self.state = 458
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
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




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_operands)
        try:
            self.state = 467
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.match(D96Parser.IDEN)
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.literal()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 465
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 466
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




    def list_literal(self):

        localctx = D96Parser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.literal()
            self.state = 474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COM:
                self.state = 470
                self.match(D96Parser.COM)
                self.state = 471
                self.literal()
                self.state = 476
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_literal)
        try:
            self.state = 482
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.match(D96Parser.INTEGER_LITERAL)
                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.match(D96Parser.FLOAT_LITERAL)
                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 479
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 480
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 481
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def muldi_arr(self):
            return self.getTypedRuleContext(D96Parser.Muldi_arrContext,0)


        def indx_arr(self):
            return self.getTypedRuleContext(D96Parser.Indx_arrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array




    def array(self):

        localctx = D96Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_array)
        try:
            self.state = 486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.muldi_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
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




    def muldi_arr(self):

        localctx = D96Parser.Muldi_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_muldi_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(D96Parser.ARRAY)
            self.state = 489
            self.match(D96Parser.LB)
            self.state = 490
            self.array_list()
            self.state = 491
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indx_arr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Indx_arrContext)
            else:
                return self.getTypedRuleContext(D96Parser.Indx_arrContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COM)
            else:
                return self.getToken(D96Parser.COM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_array_list




    def array_list(self):

        localctx = D96Parser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.indx_arr()
            self.state = 498
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COM:
                self.state = 494
                self.match(D96Parser.COM)
                self.state = 495
                self.indx_arr()
                self.state = 500
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Indx_arrContext(ParserRuleContext):

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




    def indx_arr(self):

        localctx = D96Parser.Indx_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_indx_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(D96Parser.ARRAY)
            self.state = 502
            self.match(D96Parser.LB)
            self.state = 503
            self.expr_list()
            self.state = 504
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_typeContext(ParserRuleContext):

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




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(D96Parser.ARRAY)
            self.state = 507
            self.match(D96Parser.LSB)
            self.state = 508
            self.data_type()
            self.state = 509
            self.match(D96Parser.COM)
            self.state = 510
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 511
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
        self._predicates[33] = self.expr2_sempred
        self._predicates[34] = self.expr3_sempred
        self._predicates[35] = self.expr4_sempred
        self._predicates[39] = self.expr8_sempred
        self._predicates[40] = self.expr9_sempred
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
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




