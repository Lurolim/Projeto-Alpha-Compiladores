grammar ProjetoAlpha;

program : decls? bloco EOF ;


// DECLARAÇÕES DE VARIÁVEIS

decls : varDecl+;

varDecl : 'var' ID ':' tipo ';' ;

tipo 
    : 'inteiro'
    | 'real'
    | 'booleano'
    ;


// BLOCO DE COMANDOS

bloco : '{' stmt* '}';


// COMANDOS

stmt
    : atribuicao
    | seStmt
    | whileStmt
    | ioStmt
    ;


// ATRIBUIÇÃO

atribuicao : ID '=' expr ';';


// SE / SENAO(IF/ ELSE )

seStmt : 'se' '(' expr ')' bloco ('senao' bloco)?;


// WHILE

whileStmt : 'while' '(' expr ')' bloco;


// ENTRADA / SAÍDA

ioStmt 
    : 'leia' '(' ID ')' ';'
    | 'escreva' '(' expr (',' expr)* ')' ';'
    ;


// EXPRESSÕES (PRECEDÊNCIA)


// OR (mais fraca)
expr : exprAnd ( '||' exprAnd )*;

// AND
exprAnd : exprRel ( '&&' exprRel )*;

// COMPARAÇÕES
exprRel 
    : exprAdd ( ('<' | '>' | '<=' | '>=' | '==' | '!=') exprAdd )*
    ;

// SOMA / SUBTRAÇÃO
exprAdd : exprMul ( ('+' | '-') exprMul )*;

// MULTIPLICAÇÃO / DIVISÃO
exprMul 
    : exprPrimaria ( ('*' | '/') exprPrimaria )*
    ;

// PRIMÁRIOS
exprPrimaria
    : INT
    | REAL
    | TRUE
    | FALSE
    | ID
    | '(' expr ')'
    ;


// TOKENS

TRUE  : 'verdadeiro' ;
FALSE : 'falso' ;

INT   : [0-9]+ ;
REAL  : [0-9]+ '.' [0-9]+ ;

ID    : [a-zA-Z_][a-zA-Z_0-9]* ;

WS    : [ \t\r\n]+ -> skip ;