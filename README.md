# compiladores
Labs and projects compis

antlr -Dlanguage=Python3 <FILE_NAME>.g4 -visitor -o dist 

antlr4-parse <FILE_NAME>.g4 <TOP_RULE> -tree

antlr4-parse <FILE_NAME>.g4 <TOP_RULE> -gui

# Compilers Lab 0

ANTLR -> Parser/Lexer -> Tree gui

INDICE

## :cyclone: About

This is a python implementation of ANTLR to read a *.cl file parser and lexer it with ANTLR and then show in screen a tree of the file wiht a specific grammar.

## :zap: Instalation

You have to follow the official documentation for [ANTLR](https://github.com/antlr/antlr4/blob/master/doc/index.md)

## :electric_plug: Compile

1. Generate the grammar (This will generate the files in dist/grammar)

```python
  antlr -Dlanguage=Python3 ./grammar/<FILE_NAME>.g4 -visitor -o dist
```

2. Show the tree in the terminal, TOP_RULE in this case will be `program`

``` python
python
  antlr4-parse ./grammar/<FILE_NAME>.g4 <TOP_RULE> -tree
```

## :rocket: Run

``` python
python main.py ./tests/<file_to_test>.cl
```

## :bookmark: Tests

If all the .cl file is good then it will render the tree otherwise it will show the error in terminal.

TREE **simple.cl**
<img title='simple.cl' alt='simple.cl' src='https://raw.githubusercontent.com/raulangelj/compiladores/feat/lab0/assets/simple.png?token=GHSAT0AAAAAACFG5E55ITQMTVFJWJ2J4KWCZFWEY4Q'>
[SIMPLE.CL](https://raw.githubusercontent.com/raulangelj/compiladores/feat/lab0/assets/simple.png?token=GHSAT0AAAAAACFG5E55ITQMTVFJWJ2J4KWCZFWEY4Q)

TREE **complex1.cl**
<img title='comple1.cl' alt='complex1.cl' src='https://raw.githubusercontent.com/raulangelj/compiladores/feat/lab0/assets/complex1.png?token=GHSAT0AAAAAACFG5E54IQVWIQBYICW22CNIZFWEZTQ'>
[COMPLEX.CL](https://raw.githubusercontent.com/raulangelj/compiladores/feat/lab0/assets/complex1.png?token=GHSAT0AAAAAACFG5E54IQVWIQBYICW22CNIZFWEZTQ)

TERMINAL **string_too_long.cl**
<img title='string_to_long.cl' alt='string_to_long.cl' src='https://raw.githubusercontent.com/raulangelj/compiladores/feat/lab0/assets/string_too_long.png?token=GHSAT0AAAAAACFG5E546OWQPDGWWAYQILKYZFWE2YQ'>
[STRING_TOO_LONG.CL](https://raw.githubusercontent.com/raulangelj/compiladores/feat/lab0/assets/string_too_long.png?token=GHSAT0AAAAAACFG5E546OWQPDGWWAYQILKYZFWE2YQ)

TERMINAL **bad_comment.cl**
<img title='bad_comment.cl' alt='bad_comment.cl' src='https://raw.githubusercontent.com/raulangelj/compiladores/feat/lab0/assets/bad_comment.png?token=GHSAT0AAAAAACFG5E54TK42WLEIPECHTTH4ZFWE2BQ'>
[BAD_COMMENT.cl](https://raw.githubusercontent.com/raulangelj/compiladores/feat/lab0/assets/bad_comment.png?token=GHSAT0AAAAAACFG5E54TK42WLEIPECHTTH4ZFWE2BQ)

## :star2: Authors

| Raul Angel J. | Donaldo Garcia |
| :---: |:---:|
| [![Raul Angel](https://avatars0.githubusercontent.com/u/46568595?s=200&u=c1481289dc10f8babb1bdd0853e0bcf82a213d26&v=4)](https://github.com/raulangelj)    | [![Donaldo Garcia](https://avatars1.githubusercontent.com/u/54748964?s=200&u=5e617360d13f87fa6d62022e81bab94ebf50c4e3&v=4)](https://github.com/donaldosebas) |
| <a href="https://github.com/raulangelj" target="_blank">`@raulangelj`</a> | <a href="https://github.com/donaldosebas" target="_blank">`@donaldosebas`</a> |

## :lock: License

MIT
