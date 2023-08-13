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

class Main inherits IO {
  a : Int <- 2;
  -- FALTA VALIDAR ESTO: b : A;
  c : String <- 3;
  main() : SELF_TYPE {
    {
        a <- "d";
        c <- "ho";
        z <- 1;
    }
  };
};
