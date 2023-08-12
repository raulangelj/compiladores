class Main inherits IO {
  a : Int <- 2;
  b : Int <- 5;
  c : String <- "holaaaaa";
  main() : SELF_TYPE {
    {
        a <- 1;
        c <- "ho";
    }
  };
};

class A {
  a : Int <- 2;
  b : Int;
  d : Bool;
  e : String;
  c : String <- "holaaaaa";
  main() : SELF_TYPE {
    {
        a <- 1;
    }
  };
};