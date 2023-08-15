class A {
  a: Bool <- false;
  b: Int <- 1;
};

class Main inherits IO {
  aClass: A <- new A;
  a : Int <- 1;

  main() : SELF_TYPE {
    {
      aClass <- new A;
    }
  };
};
