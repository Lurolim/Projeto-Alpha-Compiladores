from ProjetoAlphaVisitor import ProjetoAlphaVisitor

class SemanticChecker(ProjetoAlphaVisitor):
    def __init__(self):
        self.simbolos = {}
        self.erros = []

    def erro(self, msg):
        self.erros.append(f"Erro semântico: {msg}")

    # -----------------------------
    # DECLARAÇÃO DE VARIÁVEIS
    # -----------------------------
    def visitVarDecl(self, ctx):
        nome = ctx.ID().getText()
        tipo = ctx.tipo().getText()
        if nome in self.simbolos:
            self.erro(f"Variável '{nome}' já declarada.")
        else:
            self.simbolos[nome] = tipo
        return None

    # -----------------------------
    # ATRIBUIÇÕES
    # -----------------------------
    def visitAtribuicao(self, ctx):
        nome = ctx.ID().getText()
        if nome not in self.simbolos:
            self.erro(f"Variável '{nome}' não declarada.")

        tipo_expr = self.visit(ctx.expr())
        tipo_var = self.simbolos.get(nome)
        if tipo_var and tipo_expr and tipo_var != tipo_expr:
            self.erro(f"Tipo incompatível: variável '{nome}' é '{tipo_var}' mas recebeu '{tipo_expr}'.")
        return None

    # -----------------------------
    # SE / SENÃO
    # -----------------------------
    def visitSeStmt(self, ctx):
        tipo_cond = self.visit(ctx.expr())
        if tipo_cond != "booleano":
            self.erro("Condição do SE deve ser booleana.")
        self.visit(ctx.bloco(0))
        # Verifica se existe bloco 'senao'
        if len(ctx.bloco()) > 1:
            self.visit(ctx.bloco(1))
        return None

    # -----------------------------
    # WHILE
    # -----------------------------
    def visitWhileStmt(self, ctx):
        tipo_cond = self.visit(ctx.expr())
        if tipo_cond != "booleano":
            self.erro("Condição do WHILE deve ser booleana.")
        self.visit(ctx.bloco())
        return None

    # -----------------------------
    # ENTRADA / SAÍDA
    # -----------------------------
    def visitIoStmt(self, ctx):
        # Leitura
        if ctx.ID():
            var = ctx.ID().getText()
            if var not in self.simbolos:
                self.erro(f"Variável '{var}' não declarada para leitura.")
        # Escrita
        for e in ctx.expr():
            self.visit(e)
        return None

    # -----------------------------
    # EXPRESSÕES
    # -----------------------------
    def visitExpr(self, ctx):
        tipo = self.visit(ctx.exprAnd(0))
        for e in ctx.exprAnd()[1:]:
            right = self.visit(e)
            if tipo != "booleano" or right != "booleano":
                self.erro("Operador '||' só aceita booleanos.")
            tipo = "booleano"
        return tipo

    def visitExprAnd(self, ctx):
        tipo = self.visit(ctx.exprRel(0))
        for e in ctx.exprRel()[1:]:
            right = self.visit(e)
            if tipo != "booleano" or right != "booleano":
                self.erro("Operador '&&' só aceita booleanos.")
            tipo = "booleano"
        return tipo

    def visitExprRel(self, ctx):
        tipo = self.visit(ctx.exprAdd(0))
        filhos = list(ctx.getChildren())
        idx = 1
        for f in filhos:
            op = f.getText()
            if op in ["<", ">", "<=", ">=", "==", "!="]:
                right = self.visit(ctx.exprAdd(idx))
                if op in ["<", ">", "<=", ">="]:
                    if tipo not in ("inteiro", "real") or right not in ("inteiro", "real"):
                        self.erro(f"Operador '{op}' só funciona com números.")
                if op in ["==", "!="] and tipo != right:
                    self.erro(f"Comparação entre tipos incompatíveis: {tipo} e {right}.")
                tipo = "booleano"
                idx += 1
        return tipo

    def visitExprAdd(self, ctx):
        tipo = self.visit(ctx.exprMul(0))
        filhos = list(ctx.getChildren())
        idx = 1
        for f in filhos:
            if f.getText() in ["+", "-"]:
                right = self.visit(ctx.exprMul(idx))
                if tipo not in ("inteiro", "real") or right not in ("inteiro", "real"):
                    self.erro("Operadores '+' e '-' só aceitam números.")
                tipo = "real" if "real" in (tipo, right) else "inteiro"
                idx += 1
        return tipo

    def visitExprMul(self, ctx):
        tipo = self.visit(ctx.exprPrimaria(0))
        filhos = list(ctx.getChildren())
        idx = 1
        for f in filhos:
            if f.getText() in ["*", "/"]:
                right = self.visit(ctx.exprPrimaria(idx))
                if tipo not in ("inteiro", "real") or right not in ("inteiro", "real"):
                    self.erro("Operadores '*' e '/' só aceitam números.")
                tipo = "real" if "real" in (tipo, right) else "inteiro"
                idx += 1
        return tipo

    def visitExprPrimaria(self, ctx):
        token = ctx.getChild(0).getText()
        if token.isdigit():
            return "inteiro"
        if "." in token and token.replace(".", "", 1).isdigit():
            return "real"
        if token in ("verdadeiro", "falso"):
            return "booleano"
        if token in self.simbolos:
            return self.simbolos[token]
        if token.isidentifier():
            self.erro(f"Variável '{token}' não declarada.")
            return None
        if token == "(":
            return self.visit(ctx.expr())
        return None

    # -----------------------------
    # RELATÓRIO FINAL
    # -----------------------------
    def report(self):
        if self.erros:
            return False, self.erros
        return True, ["Nenhum erro semântico"]
