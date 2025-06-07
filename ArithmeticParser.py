# Generated from Arithmetic.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,87,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,1,1,
        1,1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,41,
        8,2,1,3,1,3,1,3,1,3,1,4,4,4,48,8,4,11,4,12,4,49,1,5,1,5,1,5,3,5,
        55,8,5,1,6,1,6,1,6,1,6,3,6,61,8,6,1,7,1,7,5,7,65,8,7,10,7,12,7,68,
        9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,78,8,8,1,8,1,8,1,8,3,8,83,
        8,8,3,8,85,8,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,0,3,4,1,0,5,
        6,1,0,7,12,89,0,18,1,0,0,0,2,26,1,0,0,0,4,40,1,0,0,0,6,42,1,0,0,
        0,8,47,1,0,0,0,10,54,1,0,0,0,12,56,1,0,0,0,14,62,1,0,0,0,16,71,1,
        0,0,0,18,23,3,2,1,0,19,20,7,0,0,0,20,22,3,2,1,0,21,19,1,0,0,0,22,
        25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,1,1,0,0,0,25,23,1,0,0,
        0,26,31,3,4,2,0,27,28,7,1,0,0,28,30,3,4,2,0,29,27,1,0,0,0,30,33,
        1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,3,1,0,0,0,33,31,1,0,0,0,34,
        41,5,13,0,0,35,41,5,20,0,0,36,37,5,16,0,0,37,38,3,0,0,0,38,39,5,
        17,0,0,39,41,1,0,0,0,40,34,1,0,0,0,40,35,1,0,0,0,40,36,1,0,0,0,41,
        5,1,0,0,0,42,43,3,0,0,0,43,44,7,2,0,0,44,45,3,0,0,0,45,7,1,0,0,0,
        46,48,3,10,5,0,47,46,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,
        0,0,0,50,9,1,0,0,0,51,55,3,12,6,0,52,55,3,0,0,0,53,55,3,16,8,0,54,
        51,1,0,0,0,54,52,1,0,0,0,54,53,1,0,0,0,55,11,1,0,0,0,56,57,5,20,
        0,0,57,58,5,19,0,0,58,60,3,0,0,0,59,61,5,18,0,0,60,59,1,0,0,0,60,
        61,1,0,0,0,61,13,1,0,0,0,62,66,5,14,0,0,63,65,3,10,5,0,64,63,1,0,
        0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,66,
        1,0,0,0,69,70,5,15,0,0,70,15,1,0,0,0,71,72,5,1,0,0,72,73,5,16,0,
        0,73,74,3,6,3,0,74,77,5,17,0,0,75,78,3,10,5,0,76,78,3,14,7,0,77,
        75,1,0,0,0,77,76,1,0,0,0,78,84,1,0,0,0,79,82,5,2,0,0,80,83,3,10,
        5,0,81,83,3,14,7,0,82,80,1,0,0,0,82,81,1,0,0,0,83,85,1,0,0,0,84,
        79,1,0,0,0,84,85,1,0,0,0,85,17,1,0,0,0,10,23,31,40,49,54,60,66,77,
        82,84
    ]

class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'+'", "'-'", "'*'", 
                     "'/'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "<INVALID>", "'{'", "'}'", "'('", "')'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "PLUS", "MINUS", "MUL", 
                      "DIV", "EQUALS", "NOT_EQUALS", "LT", "GT", "LTE", 
                      "GTE", "INT", "LCURLY", "RCURLY", "LPAREN", "RPAREN", 
                      "SEMICOLON", "ASSIGN", "VAR", "WS" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2
    RULE_comparison = 3
    RULE_program = 4
    RULE_statement = 5
    RULE_assignment = 6
    RULE_block = 7
    RULE_ifStatement = 8

    ruleNames =  [ "expr", "term", "factor", "comparison", "program", "statement", 
                   "assignment", "block", "ifStatement" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    PLUS=3
    MINUS=4
    MUL=5
    DIV=6
    EQUALS=7
    NOT_EQUALS=8
    LT=9
    GT=10
    LTE=11
    GTE=12
    INT=13
    LCURLY=14
    RCURLY=15
    LPAREN=16
    RPAREN=17
    SEMICOLON=18
    ASSIGN=19
    VAR=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.TermContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.PLUS)
            else:
                return self.getToken(ArithmeticParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.MINUS)
            else:
                return self.getToken(ArithmeticParser.MINUS, i)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ArithmeticParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.term()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 19
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 20
                self.term()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.FactorContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.MUL)
            else:
                return self.getToken(ArithmeticParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.DIV)
            else:
                return self.getToken(ArithmeticParser.DIV, i)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ArithmeticParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.factor()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 27
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 28
                self.factor()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ArithmeticParser.INT, 0)

        def VAR(self):
            return self.getToken(ArithmeticParser.VAR, 0)

        def LPAREN(self):
            return self.getToken(ArithmeticParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ArithmeticParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ArithmeticParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(ArithmeticParser.INT)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(ArithmeticParser.VAR)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.match(ArithmeticParser.LPAREN)
                self.state = 37
                self.expr()
                self.state = 38
                self.match(ArithmeticParser.RPAREN)
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


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.ExprContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.ExprContext,i)


        def EQUALS(self):
            return self.getToken(ArithmeticParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(ArithmeticParser.NOT_EQUALS, 0)

        def LT(self):
            return self.getToken(ArithmeticParser.LT, 0)

        def GT(self):
            return self.getToken(ArithmeticParser.GT, 0)

        def LTE(self):
            return self.getToken(ArithmeticParser.LTE, 0)

        def GTE(self):
            return self.getToken(ArithmeticParser.GTE, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = ArithmeticParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.expr()
            self.state = 43
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8064) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 44
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.StatementContext,i)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ArithmeticParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.statement()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1122306) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ArithmeticParser.AssignmentContext,0)


        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ArithmeticParser.IfStatementContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ArithmeticParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.ifStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ArithmeticParser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(ArithmeticParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(ArithmeticParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ArithmeticParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(ArithmeticParser.VAR)
            self.state = 57
            self.match(ArithmeticParser.ASSIGN)
            self.state = 58
            self.expr()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 59
                self.match(ArithmeticParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURLY(self):
            return self.getToken(ArithmeticParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(ArithmeticParser.RCURLY, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.StatementContext,i)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ArithmeticParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(ArithmeticParser.LCURLY)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1122306) != 0):
                self.state = 63
                self.statement()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.match(ArithmeticParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ArithmeticParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ArithmeticParser.LPAREN, 0)

        def comparison(self):
            return self.getTypedRuleContext(ArithmeticParser.ComparisonContext,0)


        def RPAREN(self):
            return self.getToken(ArithmeticParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.StatementContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.BlockContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(ArithmeticParser.ELSE, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = ArithmeticParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(ArithmeticParser.IF)
            self.state = 72
            self.match(ArithmeticParser.LPAREN)
            self.state = 73
            self.comparison()
            self.state = 74
            self.match(ArithmeticParser.RPAREN)
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 13, 16, 20]:
                self.state = 75
                self.statement()
                pass
            elif token in [14]:
                self.state = 76
                self.block()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 79
                self.match(ArithmeticParser.ELSE)
                self.state = 82
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 13, 16, 20]:
                    self.state = 80
                    self.statement()
                    pass
                elif token in [14]:
                    self.state = 81
                    self.block()
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





