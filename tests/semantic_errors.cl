class Main inherits IO {
  a : Int <- 2;
  main() : SELF_TYPE {
    {
      -- Errors on the plus 32 errors
      a <- 1 + 2;
      a <- 1 + "aa";
      a <- "ff" + 2;
      a <- "ff" + "aa";
      a <- 1 + true;
      a <- true + 2;
      a <- true + true;
      a <- "aa" + true;
      a <- true + "aa";
      -- Errors on the minus 32 errors
      a <- 1 - 2;
      a <- 1 - "aa";
      a <- "ff" - 2;
      a <- "ff" - "aa";
      a <- 1 - true;
      a <- true - 2;
      a <- true - true;
      a <- "aa" - true;
      a <- true - "aa";
      -- Errors on the times 32 errors
      a <- 1 * 2;
      a <- 1 * "aa";
      a <- "ff" * 2;
      a <- "ff" * "aa";
      a <- 1 * true;
      a <- true * 2;
      a <- true * true;
      a <- "aa" * true;
      a <- true * "aa";
      -- Errors on the divide 32 errors
      a <- 1 / 2;
      a <- 1 / "aa";
      a <- "ff" / 2;
      a <- "ff" / "aa";
      a <- 1 / true;
      a <- true / 2;
      a <- true / true;
      a <- "aa" / true;
      a <- true / "aa";
      -- Errors on the less than
    }
  };
};