class Main inherits IO {
  a: Int <- 0;
  --a: Bool <- true;
  --a: String <- "0";

  main() : SELF_TYPE {
    {
        if a then {
          a <- 1;
        } else {
          a <- 2;
          d <- "hola";
        }
        fi;
        while "1" loop {
          a <- a + 1;
        } pool;
    }
  };
};
