from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser

class ArithmeticVisitor:
    def __init__(self):
        self.variables = {}

    def visit(self, ctx):
        if isinstance(ctx, ArithmeticParser.ExprContext):
            return self.visitExpr(ctx)
        elif isinstance(ctx, ArithmeticParser.TermContext):
            return self.visitTerm(ctx)
        elif isinstance(ctx, ArithmeticParser.FactorContext):
            return self.visitFactor(ctx)
        elif isinstance(ctx, ArithmeticParser.AssignmentContext):
            return self.visitAssignment(ctx)
        elif isinstance(ctx, ArithmeticParser.StatementContext):
            return self.visitStatement(ctx)
        elif isinstance(ctx, ArithmeticParser.ProgramContext):
            return self.visitProgram(ctx)
        elif isinstance(ctx, ArithmeticParser.IfStatementContext):
            return self.visitIfStatement(ctx)
        elif isinstance(ctx, ArithmeticParser.ComparisonContext):
            return self.visitComparison(ctx)
        elif isinstance(ctx, ArithmeticParser.BlockContext):
            return self.visitBlock(ctx)
        else:
            raise Exception(f"Tipo de contexto desconhecido: {type(ctx)}")

    def visitExpr(self, ctx):
        result = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            if ctx.getChild(i * 2 - 1).getText() == '+':
                result += self.visit(ctx.term(i))
            else:
                result -= self.visit(ctx.term(i))
        return result

    def visitTerm(self, ctx):
        result = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            if ctx.getChild(i * 2 - 1).getText() == '*':
                result *= self.visit(ctx.factor(i))
            else:
                result /= self.visit(ctx.factor(i))
        return result

    def visitFactor(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.VAR():
            var_name = ctx.VAR().getText()
            if var_name not in self.variables:
                raise Exception(f"Variável '{var_name}' não definida.")
            return self.variables.get(var_name, 0)
        else:
            return self.visit(ctx.expr())

    def visitAssignment(self, ctx):
        var_name = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        self.variables[var_name] = value
        return value        
    
    def visitStatement(self, ctx):
        if ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.expr():
            return self.visit(ctx.expr())
        else:
            raise Exception("Unknown statement type")
    
    def visitBlock(self, ctx):
        results = []
        for statement in ctx.statement():
            results.append(self.visit(statement))
        return results[-1] if results else None

    def visitProgram(self, ctx):
        results = []
        for statement in ctx.statement():
            results.append(self.visit(statement))
        return results[-1] if results else None

    def visitComparison(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        op = ctx.getChild(1).getText()
        if op == '==':
            return left == right
        elif op == '!=':
            return left != right
        elif op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right

    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.comparison())
        if condition:
            if ctx.block(0):
                return self.visit(ctx.block(0))
            return self.visit(ctx.statement(0))
        elif ctx.ELSE():
            if ctx.block(1):
                return self.visit(ctx.block(1))
            return self.visit(ctx.statement(1))
        return None
    
    

def main():
    visitor = ArithmeticVisitor()
    print("Calculadora aritmética. Digite '$' para sair.")
    while True:
        try:
            expression = input(">")
            if expression == "$":
                break
            lexer = ArithmeticLexer(InputStream(expression))
            stream = CommonTokenStream(lexer)
            parser = ArithmeticParser(stream)
            tree = parser.program()
            result = visitor.visit(tree)
            if result is not None:
                print("Resultado:", result)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()