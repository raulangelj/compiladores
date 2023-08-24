class Main inherits IO {
  a : String <- "Hello World";
  b : String <- "Bye World";

  sum(a : Int, b : Int) : Int {
    {
      a <- "World";
      a + b;
    }
  };

  main() : Object {
    sum(5, 5);
  };
};