class Main inherits IO {
  a : Int <- 4;

  sum(a : Int, b : Int) : Int {
    a + b
  };

  main(): Object {
    a <- sum(1, 2)
  };
};