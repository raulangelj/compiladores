class Main inherits IO {
  a : Int <- 2;
  main() : SELF_TYPE {
    {
      (*HAY 53 errores en total*)
      -- 32 arithmetic erros
      -- Errors on the plus
      a <- 1 + 2;
      a <- 1 + "aa";
      a <- "ff" + 2;
      a <- "ff" + "aa";
      a <- 1 + true;
      a <- true + 2;
      a <- true + true;
      a <- "aa" + true;
      a <- true + "aa";
      -- Errors on the minus
      a <- 1 - 2;
      a <- 1 - "aa";
      a <- "ff" - 2;
      a <- "ff" - "aa";
      a <- 1 - true;
      a <- true - 2;
      a <- true - true;
      a <- "aa" - true;
      a <- true - "aa";
      -- Errors on the times
      a <- 1 * 2;
      a <- 1 * "aa";
      a <- "ff" * 2;
      a <- "ff" * "aa";
      a <- 1 * true;
      a <- true * 2;
      a <- true * true;
      a <- "aa" * true;
      a <- true * "aa";
      -- Errors on the divide
      a <- 1 / 2;
      a <- 1 / "aa";
      a <- "ff" / 2;
      a <- "ff" / "aa";
      a <- 1 / true;
      a <- true / 2;
      a <- true / true;
      a <- "aa" / true;
      a <- true / "aa";
      -- 18 comparison errors
      -- Errors on the less
      a <- 1 < 2;
      a <- 1 < "aa";
      a <- "ff" < 2;
      a <- "ff" < "aa";
      a <- 1 < true;
      a <- true < 2;
      a <- true < true;
      a <- "aa" < true;
      a <- true < "aa";
      -- Errors on the less equal
      a <- 1 <= 2;
      a <- 1 <= "aa";
      a <- "ff" <= 2;
      a <- "ff" <= "aa";
      a <- 1 <= true;
      a <- true <= 2;
      a <- true <= true;
      a <- "aa" <= true;
      a <- true <= "aa";
      -- Errors on the equal
      a <- 1 = 2;
      a <- 1 = "aa";
      a <- "ff" = 2;
      a <- "ff" = "aa";
      a <- 1 = true;
      a <- true = 2;
      a <- true = true;
      a <- "aa" = true;
      a <- true = "aa";
      -- Error on Not - 2
      a <- not 1;
      a <- not "aa";
      a <- not true;
      -- Error on Negate - 1
      a <- ~"aa";
      a <- ~true;
      a <- ~1;
    }
  };
};