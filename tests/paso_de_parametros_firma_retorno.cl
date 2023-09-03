class Main inherits IO {
  a : Int <- 0;

  sum(a: Int, b: Int) : Int {
    a + b
  };

  main() :Object {
    a <- sum("hola")
  }
}