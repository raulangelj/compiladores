class Main inherits IO {
  a: Int <- 0;
  b: Int <- 2 + a * 3;
  c: Bool <- true;

  main(): Object {
    {
      a <- 1 * 3 + a;
      if ( 2 < 3) then {
        b <- 2;
      } else {
        b <- 3;
      } fi;
    }
  };
};