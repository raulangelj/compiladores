class Main inherits IO {
  a : Int <- 2;
  b : Int <- 5;
  c : String <- "holaaaaa";
  main() : SELF_TYPE {
    {
        a <- a + b * c;
          self;
    }
  };
};