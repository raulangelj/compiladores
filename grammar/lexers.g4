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
ERROR: 'ERROR';

// COMENTARIOS
COMMENT_BLOCK: '(*' .*? '*)' -> skip;
COMMENT_LINE: '--' ~[\r\n]* -> skip;

// ENTEROS
INT_VAR: [0-9]+;
// IDENTIFICADORES
ID_VAR: [a-z]([a-zA-Z0-9]|'_')*;
TYPE_IDENTIFIER: [A-Z]([a-zA-Z0-9]|'_')*;
// ? Existen dos identificadores especiales, self y SELF_TYPE, que no son tratados como palabras reservadas. ¿Como agrego estos identificadores?

// CADENAS
fragment ESC_SEQ : '\\' ('b' | 't' | 'n' | 'f');
// STR_VAR : '"' (ESC_SEQ | ~['"])* '"';
STR_VAR : '"' (ESC_SEQ | ~['"])* '"' {
  text = self.text

  char_count = 0
  char_limit = 1024

  eof = False
  toolong = False
  backslash = False
  nullflag = False
  esc_nullflag = False
  unescaped = False

  special_chars = {
      '\\n': '\n',
      '\\t': '\t',
      '\\f': '\f',
      '\\b': '\b',
      '\\"': '\"',
      '\\\\': '\\'
  }

  str_list = []
  length = len(text)
  if (text[length - 1] != '"' and text[length - 1] != '\n' and text[length - 1] != '\\') or length == 1:
      eof = True
  elif text[length - 1] == '\n':
      unescaped = True
  elif text[length - 1] == '\\':
      backslash = True

  i = 1
  while i < length - 1:
      if text[i] == '\\':
          if text[i:i + 2] in special_chars:
              str_list.append(special_chars[text[i:i + 2]])
              i += 2
          elif text[i + 1] == '\n':
              str_list.append('\n')
              i += 2
              if i == length - 1:
                  eof = True
                  unescaped = False
          elif text[i + 1] == '\u0000' and not nullflag:
              esc_nullflag = True
              break
          else:
              str_list.append(text[i + 1])
              i += 2
      elif text[i] == '\u0000' and not esc_nullflag:
          nullflag = True
          break
      else:
          str_list.append(text[i])
          i += 1

      char_count += 1
      if char_count > char_limit:
          toolong = True
          break

  if esc_nullflag:
      self.type = self.ERROR
      self.text = "String contains escaped null character."
      return
  if backslash and char_count < char_limit + 2:
      self.type = self.ERROR
      self.text = "Backslash at end of file"
      return
  if toolong:
      self.type = self.ERROR
      self.text = "String constant too long"
      return
  if unescaped and char_count < char_limit + 2:
      self.type = self.ERROR
      self.text = "Unterminated string constant"
      return
  if eof:
      self.type = self.ERROR
      self.text = "EOF in string constant"
      return
  if nullflag:
      self.type = self.ERROR
      self.text = "String contains null character."
      return

  formatted_str = ''.join(str_list)
  self.text = formatted_str
}; // SI ES PYTHON
