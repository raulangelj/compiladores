lexer grammar lexers;

// ENTEROS
INT_VAR: [0-9]+;
// IDENTIFICADORES
ID_VAR: [a-z][_a-z0-9A-Z]*;
TYPE_IDENTIFIER: [A-Z][_a-z0-9A-Z]*;
// ? Existen dos identificadores especiales, self y SELF_TYPE, que no son tratados como palabras reservadas. ¿Como agrego estos identificadores?
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

// ! FALTA AGREGAR LAS REGLAS DE STRINS VER DOC

// COMENTARIOS
COMMENT_LINE: '--' ~[\r\n]* -> skip;
COMMENT_BLOCK: '(*' .*? '*)' -> skip;

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

// BOOLS
TRUE: 'true';
FALSE: 'false';

// WHITESPACE
WS: [ \n\f\r\t\v]+ -> skip;
