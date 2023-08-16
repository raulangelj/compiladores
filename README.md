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

## :red_circle: Reglas semanticas

- [ ]  Main
  - [x] Debe tener una clase Main
  - [x] La clase main solo puede heredar de IO
  - [x] La clase Main debe de tener un metodo main sin parametros
  - [ ] La ejecucion inicia evaluando (new Main).main()

- [x] BASICS Types
  - [x] Int, String, Bool
  - [x] Se puede crear tipos de datos apartir de clases
  - [x] Las clases de tipos basicos no pueden ser padres de otras clases

- [ ] Scope
  - [x] Los atributos deben de ser definidos antes de su uso
  - [ ] Un metodo puede ser llamado de forma recursiva - ! COMO VALIDARLO
  - [ ] Ambito global y local, las variables let son locales
  - [ ] Todos los atributos y metodos de las clases son publicos
  - [ ] Scope local tiene prioridad sobre global
  - [x] Ningun identificador puede ser definido mas de una vez
  - [ ] Si B hereda de A y B sobreescribe un método de A, este método debe de poseer la misma firma con la que fue declarado en A. - ! NO ENTIENDO
  - [ ] No se puede herencia multiple y herencia recursiva - ! NO ENTIENDO LA RECURSIVA

- [x] Default
  - [x] Int -> 0
  - [x] String -> "" (cadena vacia)
  - [x] Bool -> false

- [x] Casteo
  - [x] Casteo implicito de Bool a Int (False es 0 y True es 1)
  - [x] Casteo implicito de Int a Bool (0 es False y 1 es True)
  - [x] NO se puede casteo explicito

- [ ]  Asignacion
  - [x] `<id>` <- `<expr>`
  - [x] El tipo de expr debe ser del mismo tipo de id o puede ser heredado
  - [x] El valor de `<expr>` se convierte a `<id>`
  - [x] El tipo de dato de la asignacion es el tipo de `<exp>`
  - [x] Si `<id>` es un atributo de alguna clase este debe de haberse definido antes
  - [ ] Se pueden tener identificadores recurisivos [class1].[class2].[class3]...

- [ ] Metodos y returns
  - [ ] Los argumentos que son de tipo basicio se pasan por valor - int, string, bool?
  - [ ] Los argumetnos que son de tipos derivados se pasan po referencia - objetos?
  - [x] Los argumentos del metodo son variables locales
  - [x] Los argumentos se evaluan de izquierda a derecha
  - [x] El tipo de retorno del metodo debe concidir con tipo de retorno
  - [x] Si se llama a un metodo en `<id>` <- `<exp>` el return se asiganra al `<id>`

- [x] Estructuras de control
  - [x] El tipo estatico de un if o while debe de ser bool
  - [x] El tipo de dato del condicional if es el tipo de dato del bloque que sea un supertipo de ambas ramas del condicional
  - [x] El tipo de dato de while es un Objeto

- [x] Expresiones
  - [x] Los aritmeticos se aplican a variables tipo int y el resultado es int
  - [x] Los comparativos se aplica a datos que sean de la misma clase o que sean objetos que hereden de la misma clase. El resultado es bool
  - [x] La operacion ~ aplicado a tipo int devuelve un tipo int
  - [x] La operacion not en un dato bool devuelve un tipo bool

- [x] Clases especiales
  - [x] Clase IO que define funciones de entrada y salida de int y string
  - [x] La tabla de simbolos debe de tener definidas las clases IO, Int, String y Bool con sus metodos por defecto.

## :bookmark: Tests

TO DO

## :star2: Authors

| Raul Angel J. | Donaldo Garcia |
| :---: |:---:|
| [![Raul Angel](https://avatars0.githubusercontent.com/u/46568595?s=200&u=c1481289dc10f8babb1bdd0853e0bcf82a213d26&v=4)](https://github.com/raulangelj)    | [![Donaldo Garcia](https://avatars1.githubusercontent.com/u/54748964?s=200&u=5e617360d13f87fa6d62022e81bab94ebf50c4e3&v=4)](https://github.com/donaldosebas) |
| <a href="https://github.com/raulangelj" target="_blank">`@raulangelj`</a> | <a href="https://github.com/donaldosebas" target="_blank">`@donaldosebas`</a> |

## :lock: License

MIT
