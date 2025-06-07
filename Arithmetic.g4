grammar Arithmetic;

// Regras do Parser
expr: term ( (PLUS | MINUS) term )* ;
term: factor ( (MUL | DIV) factor )* ;
factor: INT | VAR | LPAREN expr RPAREN ;
comparison: expr (EQUALS | NOT_EQUALS | LT | GT | LTE | GTE) expr ;

program: statement+ ;

statement: assignment | expr | ifStatement ;
assignment: VAR ASSIGN expr SEMICOLON?;

block: LCURLY statement* RCURLY ;
ifStatement: IF LPAREN comparison RPAREN (statement | block) (ELSE (statement | block))? ;


// Regras do Lexer
IF: 'if' ;
ELSE: 'else' ;

PLUS: '+' ;
MINUS: '-' ;
MUL: '*' ;
DIV: '/' ;

EQUALS: '==' ;
NOT_EQUALS: '!=' ;
LT: '<' ;
GT: '>' ;
LTE: '<=' ;
GTE: '>=' ;

INT: [0-9]+ ;
LCURLY: '{' ;
RCURLY: '}' ;
LPAREN: '(' ;
RPAREN: ')' ;
SEMICOLON: ';' ;
ASSIGN: '=' ;
VAR: [a-zA-Z_][a-zA-Z0-9_]* ;

WS: [ \t\r\n]+ -> skip ;

