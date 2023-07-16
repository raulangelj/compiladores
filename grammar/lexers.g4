lexer grammar lexers;

// PALABRAS RESERVADAS son case insenstive, es valido 'class' o 'CLASS'
CLASS: [cC][lL][aA][sS][sS];
ELSE: [eE][lL][sS][eE];
FI: [fF][iI];
IF: [iI][fF];
IN: [iI][nN];
INHERITS: [iI][nN][hH][eE][rR][iI][tT][sS];
ISVOID: [iI][sS][vV][oO][iI][dD];
LOOP: [lL][oO][oO][pP];
POOL: [pP][oO][oO][lL];
THEN: [tT][hH][eE][nN];
WHILE: [wW][hH][iI][lL][eE];
NEW: [nN][eE][wW];
NOT: [nN][oO][tT];
LET: [lL][eE][tT];

// BOOLS
TRUE: 'true';
FALSE: 'false';

// WHITESPACE
WS: [ \n\f\r\t]+ -> skip;

NEWLINE: '\r'? '\n' -> skip;

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
COLON: ':';
SEMICOLON: ';';
COMMA: ',';
PERIOD: '.';
NEGATIVE: '~';
AT: '@';
// OPERADORES
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
// COMPARADORES
LESS_THAN: '<';
LESS_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_EQUAL: '>=';
EQUAL: '=';
FAT_ARROW: '=>';
ASSIGN: '<-';

// CADENAS
STR_VAR : '"' (ESC_SEQ | ~['"])* '"'; // ? como agrego la validacion? dentro de brackets deberia de ser python?
fragment ESC_SEQ : '\\' ('b' | 't' | 'n' | 'f');

// COMENTARIOS
COMMENT_LINE: '--' ~[\r\n]* -> skip;
COMMENT_BLOCK: '(*' .*? '*)' -> skip;

// ENTEROS
INT_VAR: [0-9]+;
// IDENTIFICADORES
ID_VAR: [a-z]([a-zA-Z0-9]|'_')*;
TYPE_IDENTIFIER: [A-Z]([a-zA-Z0-9]|'_')*;
// ? Existen dos identificadores especiales, self y SELF_TYPE, que no son tratados como palabras reservadas. ¿Como agrego estos identificadores?