import sys
from antlr4 import *
from ProjetoAlphaLexer import ProjetoAlphaLexer
from ProjetoAlphaParser import ProjetoAlphaParser
from ProjetoAlphaVisitor import ProjetoAlphaVisitor
from semantic_checker import SemanticChecker
from anytree import Node, RenderTree

# ÁRVORE HIERÁRQUICA

def build_tree(ctx, parent=None):
    name = type(ctx).__name__.replace("Context", "")
    node = Node(name, parent=parent)
    for child in ctx.getChildren():
        if hasattr(child, "getChildren"):
            build_tree(child, node)
        else:
            Node(str(child), parent=node)
    return node


# EXECUTOR COMPATÍVEL COM SEU G4

class Executor(ProjetoAlphaVisitor):
    def __init__(self):
        self.memory = {}

    # Programa
    def visitProgram(self, ctx):
        if ctx.decls():
            self.visit(ctx.decls())
        return self.visit(ctx.bloco())

    # Declaração de variáveis
    def visitVarDecl(self, ctx):
        tipo = ctx.tipo().getText()
        name = ctx.ID().getText()
        if tipo == "inteiro":
            self.memory[name] = 0
        elif tipo == "real":
            self.memory[name] = 0.0
        elif tipo == "booleano":
            self.memory[name] = False

    # Atribuição
    def visitAtribuicao(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value

    # SE / SENÃO
    def visitSeStmt(self, ctx):
        cond = self.visit(ctx.expr())
        if cond:
            self.visit(ctx.bloco(0))
        elif len(ctx.bloco()) > 1:
            self.visit(ctx.bloco(1))

    # WHILE
    def visitWhileStmt(self, ctx):
        while self.visit(ctx.expr()):
            self.visit(ctx.bloco())

    # LEIA / ESCREVA
    def visitIoStmt(self, ctx):
        cmd = ctx.getChild(0).getText()
        if cmd == "leia":
            var = ctx.ID().getText()
            value = input(f"{var} = ")
            if value.isdigit():
                value = int(value)
            elif value.replace(".", "", 1).isdigit():
                value = float(value)
            elif value.lower() in ["verdadeiro", "falso"]:
                value = (value.lower() == "verdadeiro")
            self.memory[var] = value
        else:
            vals = [str(self.visit(e)) for e in ctx.expr()]
            print(" ".join(vals))

    # EXPRESSÕES
    def visitExpr(self, ctx):
        result = self.visit(ctx.exprAnd(0))
        for e in ctx.exprAnd()[1:]:
            result = result or self.visit(e)
        return result

    def visitExprAnd(self, ctx):
        result = self.visit(ctx.exprRel(0))
        for e in ctx.exprRel()[1:]:
            result = result and self.visit(e)
        return result

    def visitExprRel(self, ctx):
        result = self.visit(ctx.exprAdd(0))
        filhos = list(ctx.getChildren())
        idx = 1
        for f in filhos:
            op = f.getText()
            if op in ["<", ">", "<=", ">=", "==", "!="]:
                right = self.visit(ctx.exprAdd(idx))
                match op:
                    case "<":  result = result < right
                    case ">":  result = result > right
                    case "<=": result = result <= right
                    case ">=": result = result >= right
                    case "==": result = result == right
                    case "!=": result = result != right
                idx += 1
        return result

    def visitExprAdd(self, ctx):
        result = self.visit(ctx.exprMul(0))
        filhos = list(ctx.getChildren())
        idx = 1
        for f in filhos:
            op = f.getText()
            if op in ["+", "-"]:
                right = self.visit(ctx.exprMul(idx))
                result = result + right if op == "+" else result - right
                idx += 1
        return result

    def visitExprMul(self, ctx):
        result = self.visit(ctx.exprPrimaria(0))
        filhos = list(ctx.getChildren())
        idx = 1
        for f in filhos:
            op = f.getText()
            if op in ["*", "/"]:
                right = self.visit(ctx.exprPrimaria(idx))
                result = result * right if op == "*" else result / right
                idx += 1
        return result

    def visitExprPrimaria(self, ctx):
        token = ctx.getChild(0).getText()
        if token.isdigit():
            return int(token)
        if "." in token and token.replace(".", "", 1).isdigit():
            return float(token)
        if token == "verdadeiro":
            return True
        if token == "falso":
            return False
        if token in self.memory:
            return self.memory[token]
        if token == "(":
            return self.visit(ctx.expr())
        return token

# MAIN

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.alpha>")
        return

    arquivo = sys.argv[1]
    input_stream = FileStream(arquivo, encoding="utf-8")
    lexer = ProjetoAlphaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ProjetoAlphaParser(stream)
    tree = parser.program()

    # ÁRVORE HIERÁRQUICA

    print("=== Árvore Sintática (Hierarquia) ===")
    root = build_tree(tree)
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")

    # ÁRVORE LINEAR

    print("\n=== Árvore Sintática (Linear) ===")
    print(tree.toStringTree(recog=parser))

    # Verificação semântica
    print("=== Verificação Semântica ===")
    checker = SemanticChecker()
    checker.visit(tree)
    valid, msgs = checker.report()
    for m in msgs:
        print(m)

    # Execução
    if valid:
        print("\n=== Execução ===")
        executor = Executor()
        executor.visit(tree)

if __name__ == "__main__":
    main()