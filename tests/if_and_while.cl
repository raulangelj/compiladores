class Main inherits IO {
  a : Bool <- true;
  b : String <- "Hello World";

  main() : Object {
    if b then {
      out_string(b);
    } else {
      out_string("Hello World");
    }
  };
};