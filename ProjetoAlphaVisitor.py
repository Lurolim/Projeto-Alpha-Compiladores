# Generated from ProjetoAlpha.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ProjetoAlphaParser import ProjetoAlphaParser
else:
    from ProjetoAlphaParser import ProjetoAlphaParser

# This class defines a complete generic visitor for a parse tree produced by ProjetoAlphaParser.

class ProjetoAlphaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ProjetoAlphaParser#program.
    def visitProgram(self, ctx:ProjetoAlphaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#decls.
    def visitDecls(self, ctx:ProjetoAlphaParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#varDecl.
    def visitVarDecl(self, ctx:ProjetoAlphaParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#tipo.
    def visitTipo(self, ctx:ProjetoAlphaParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#bloco.
    def visitBloco(self, ctx:ProjetoAlphaParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#stmt.
    def visitStmt(self, ctx:ProjetoAlphaParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#atribuicao.
    def visitAtribuicao(self, ctx:ProjetoAlphaParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#seStmt.
    def visitSeStmt(self, ctx:ProjetoAlphaParser.SeStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#whileStmt.
    def visitWhileStmt(self, ctx:ProjetoAlphaParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#ioStmt.
    def visitIoStmt(self, ctx:ProjetoAlphaParser.IoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#expr.
    def visitExpr(self, ctx:ProjetoAlphaParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#exprAnd.
    def visitExprAnd(self, ctx:ProjetoAlphaParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#exprRel.
    def visitExprRel(self, ctx:ProjetoAlphaParser.ExprRelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#exprAdd.
    def visitExprAdd(self, ctx:ProjetoAlphaParser.ExprAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#exprMul.
    def visitExprMul(self, ctx:ProjetoAlphaParser.ExprMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ProjetoAlphaParser#exprPrimaria.
    def visitExprPrimaria(self, ctx:ProjetoAlphaParser.ExprPrimariaContext):
        return self.visitChildren(ctx)



del ProjetoAlphaParser