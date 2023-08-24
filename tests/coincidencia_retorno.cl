class Main inherits IO {
  a : String <- "ff";

  sum(a : Int, b : Int) : Int {
    a + b
  };

  main(): Object {
    a <- sum(1, 2)
  };
};