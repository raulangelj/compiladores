class Main inherits IO {
  a: Bool <- false;
  b: Int <- 1;

  main() : SELF_TYPE {
    {
        b <- a + true;
        b <- a - true;
        b <- a * true;
        b <- a / true;
    }
  };
};
