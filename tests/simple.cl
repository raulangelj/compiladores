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
  --c : String <- 3;
  d : String;
  n: Bool <- true;
  pruebavar : Int;
  main() : SELF_TYPE {
    {
        a <- 1 + a;
        --a <- "d";
        d <- "ho";
        --z <- 1;
        n <- 1 < 2;
    }
  };

  prueba(n: Int) : Int {
    {
      pruebavar <- 1;
    }
  };
};
