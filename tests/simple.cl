class Main inherits IO {
  a : Int <- 1;
  b : Int <- 2;
  c : String <- "Helld";

  sum(a : Int, b : Int) : Int {
    {
      a + b;
    }
  };

  main() : SELF_TYPE {
    {
      a <- sum(a, b);
    }
  };
};
