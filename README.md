# Projeto Alpha — Compilador

## Sobre o Projeto
O Projeto Alpha é uma linguagem simples desenvolvida para a disciplina de Compiladores.  
Ela inclui: declaração de variáveis, operações aritméticas, condicionais, laços de repetição, entrada/saída e verificação semântica.  
O analisador léxico e sintático foi gerado com **ANTLR 4** e toda a etapa semântica foi implementada em **Python** através de um visitor personalizado.

## Estrutura do Repositório
- `antlr/` — ANTLR 4.13.2 (jar para gerar o parser)
- `ProjetoAlpha.g4` — Gramática da linguagem
- `ProjetoAlphaLexer.py` — Lexer gerado pelo ANTLR
- `ProjetoAlphaParser.py` — Parser gerado pelo ANTLR
- `ProjetoAlphaVisitor.py` — Visitor base gerado pelo ANTLR
- `ProjetoAlphaListener.py` — Listener base gerado pelo ANTLR
- `semantic_checker.py` — Checagem semântica
- `main.py` — Script principal
- `Test_alpha/` — Programas de teste

## Requisitos Atendidos (Resumo)

✔ Tipos de variáveis: inteiro, real e booleano  
✔ Condicional: se ... senao  
✔ Laço: while  
✔ Expressões aritméticas com precedência  
✔ Atribuições com checagem de tipos  
✔ leia() e escreva()  
✔ Tokens ignorados (espaços e quebras)

## Como Executar o Projeto
Instale dependências:
pip install antlr4-python3-runtime anytree

Execute:
python main.py Test_alpha/teste1.alpha

## Como Regenerar o Parser
java -jar antlr/antlr-4.13.2-complete.jar -Dlanguage=Python3 ProjetoAlpha.g4 -visitor

## Testes
python main.py Test_alpha/<arquivo>

## Conclusão
O Projeto Alpha inclui:

✔léxico,
✔sintaxe,
✔análise semântica,
✔testes executáveis,

cumprindo todos os requisitos solicitados para um Compilador.
