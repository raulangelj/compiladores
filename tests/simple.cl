class Main inherits IO {
  a : Int <- 1;
  b : String <- "hello";
  
  sum(b: Int, d: Int) : Int {
    {
      b + d; 
    }
  };

  main() : SELF_TYPE {
    {
      a <- sum(1, 2);
    }
  };
};
