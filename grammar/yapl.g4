grammar yapl;
import lexers;

// Productions
program: (classs SEMICOLON)+;

classs:
	CLASS TYPE_IDENTIFIER (INHERITS TYPE_IDENTIFIER)? LBRACE (
		feature SEMICOLON
	)* RBRACE;

var_typescript:
	<assoc = right> ID_VAR COLON TYPE_IDENTIFIER (ASSIGN expr)? # attributesDeclaration;

feature:
	ID_VAR LPAREN (formal (COMMA formal)*)* RPAREN COLON TYPE_IDENTIFIER LBRACE expr RBRACE #
		methodDef
	| <assoc = right> ID_VAR COLON TYPE_IDENTIFIER (ASSIGN expr)? # attr;

formal: ID_VAR COLON TYPE_IDENTIFIER;

expr:
	ID_VAR LPAREN (expr (COMMA expr)*)* RPAREN			# FunctionCall
	| expr (AT TYPE_IDENTIFIER)? PERIOD ID_VAR LPAREN (
		expr (COMMA expr)*
	)* RPAREN												# methodCall
	| IF expr THEN expr ELSE expr FI						# if
	| WHILE expr LOOP expr POOL								# while
	| LBRACE (expr SEMICOLON)+ RBRACE						# block // ? Precedencia correcta?
	| LET var_typescript (COMMA var_typescript)* IN expr	# let
	| NEW TYPE_IDENTIFIER									# new
	| NEGATIVE expr											# negative
	| ISVOID expr											# isvoid
	| expr MULT expr										# mult
	| expr DIV expr											# div
	| expr PLUS expr										# plus
	| expr MINUS expr										# minus
	| expr LESS_EQUAL expr									# less_equal
	| expr LESS_THAN expr									# less
	| expr EQUAL expr										# equal
	| NOT expr												# not
	| LPAREN expr RPAREN									# paren
	| ID_VAR												# id
	| INT_VAR												# integer
	| STR_VAR												# string
	| TRUE													# true
	| FALSE													# false
	| <assoc = right> ID_VAR ASSIGN expr					# assign;