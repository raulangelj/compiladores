class A {
  a: Int <- 0;
  b: Int <- 0;
  c: Bool;

  sum(d: Int): Int {
    {
      if  c then {
        a <- a + d;
        b <- b + 1;
      } else {
        a <- a + d;
        b <- b + 2;
      }
      fi;
      while (c) loop {
        a <- a + 1;
        b <- b + 1;
        d <- d - 1;
      } pool;
      a;
    }
  };
};

class B { 
  a: B;
  aa: A;
};

class Main inherits IO {
  a: Int <- 0;
  b: A;

  main(): Object {
    a <- 1
    --let h: A in {
    --  h <- new A;
    --}
  };
};