class A {
  a: Int <- 0;
  b: Int <- 0;
  c: Bool <- true;

  sum(m: Int): Int {
    {
      if (c) then {
        a + b;
      } else {
        a - b;
      }
      while (a < b) {
        a <- a + 1;
      }
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
  b: new A;

  main(): Object {
    a <- 1
    --let h: A in {
    --  h <- new A;
    --}
  };
};