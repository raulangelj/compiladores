(* this is a comment *)
class B {
  s : String <- "Hello";
  g(y:String) : Int {
    y.concat(s)
  };
  f(x:Int) : Int {
    x+1
  };
};

class DB {
  -- this is another comment
  s : B <- "Hello";
  g(y:String) : Int {
    y.concat(s)
    self.y.concat(s)
  };
};

class Pa {
  -- this is another comment
  fa(y:String, point: Dot): Int { 1 + point.x };
  fa2(y:String, point: Dot): Int { 1 + point.x(1, 3) };
};
