class Main inherits IO {
  a: Int <- 0;
  b: Int <- 2 + a * 3;
  c: Bool <- true;

  aa(c : Int, d : Int): Bool {
    {
      while (a <= 0) loop {
        a <- a - 1;
      } pool;
    }
  };

  main(): Object {
    {
      a <- 1 * 3 + a;
      if ( 2 < 3) then {
        b <- 2;
      } else {
        b <- 3;
        c <- aa(1, 1);
      } fi;
    }
  };
};