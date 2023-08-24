class A {
  a : Int <- 1;

  sum(b : Int) : Int {
    a + b;
  };
};

class B inherits A {
  b : Int <- 2;

  sum(b : String, a: Int) : String {
    a + b;
  };
};

class Main inherits IO {
  a : A;
  main(): Object {
    a <- new A;
  }
};