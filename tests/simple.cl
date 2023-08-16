class A {
  a : Int <- 1;

  sum(b: Int, d: Int) : Int {
    {
      b + d; 
    }
  };
};

class B inherits A {

  sum(a: Int, u: String) : String {
    {
      a + u; 
    }
  };
};

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
