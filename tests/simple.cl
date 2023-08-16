class Main inherits IO {
  a : Int <- 1;
  b : String <- "hello";
  f : String <- "jj";
  
  sum(b: Int, d: Int) : Int {
    {
      (
        let f: Int in 
        {
          b <- 7;
          f <- 1;
        }
      );
    }
  };

  main() : SELF_TYPE {
    {
      a <- sum(1, 2);
    }
  };
};
