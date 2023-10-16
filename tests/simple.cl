class Main inherits IO {
  a: Int <- 1 + 5;
  b: Int <- 2 - 1;
  c: Int <- 3 / 1;
  d: Int <- 4 * 1;

  main(): Object {
    {
      a <- a + 5;
      b <- 6 - 2;
      c <- 9 / 3;
      d <- 2 * 4;
    }
  };
};