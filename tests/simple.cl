class A {
  a: Bool <- false;
  b: Int <- 1;
};

class B inherits A {
  a: Bool <- true;
  c: Int <- 2;
};

class C inherits A {
  a: Bool <- false;
  d: Int <- 3;
};

class D {
  a: Bool <- true;
  e: Int <- 4;
};

class Main inherits IO {
  bClass: B <- new B;
  b2 : D <- new D;
  a : Int <- 1;

  main() : SELF_TYPE {
    {
      bClass < b2;
      2 < a;
    }
  };
};
