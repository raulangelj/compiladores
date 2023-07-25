# Compilers Lab 1

ANTLR -> Parser/Lexer -> Tree gui

INDICE

## :cyclone: About

This is a python implementation of ANTLR to read a *.cl file parser and lexer it with ANTLR and then show in screen a tree of the file wiht a specific grammar.

**The document for the semantic types can be found in**[THIS LINK](https://docs.google.com/document/d/1rENcILO97wyMBg6W2bGD8t54zeyllCEIRl2E6ZQi8Rs/edit?usp=sharing)

## :zap: Instalation

You have to follow the official documentation for [ANTLR](https://github.com/antlr/antlr4/blob/master/doc/index.md)

## :electric_plug: Compile

1. Generate the grammar (This will generate the files in dist/grammar) (This is necessary if it is the first time running or if there was a change in the g4)

```python
  antlr4 -Dlanguage=Python3 ./grammar/<FILE_NAME>.g4 -visitor -o yapl/grammar
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

The test for this is "semantic_errors.cl"

SEMANTIC_ERRORS **semantic_errors.cl**

<img src="assets/LAB1/semantic_errors.png" alt="semantic_errors">

## :star2: Authors

| Raul Angel J. | Donaldo Garcia |
| :---: |:---:|
| [![Raul Angel](https://avatars0.githubusercontent.com/u/46568595?s=200&u=c1481289dc10f8babb1bdd0853e0bcf82a213d26&v=4)](https://github.com/raulangelj)    | [![Donaldo Garcia](https://avatars1.githubusercontent.com/u/54748964?s=200&u=5e617360d13f87fa6d62022e81bab94ebf50c4e3&v=4)](https://github.com/donaldosebas) |
| <a href="https://github.com/raulangelj" target="_blank">`@raulangelj`</a> | <a href="https://github.com/donaldosebas" target="_blank">`@donaldosebas`</a> |

## :lock: License

MIT
