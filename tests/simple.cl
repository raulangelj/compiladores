class Animal {
  a : Int <- 1;
  say_hello() : SELF_TYPE {
    {
      a <- 2;
      self;
    }
  };
};

class Dog inherits Animal {
  a : Int <- 3;
  say_hello() : SELF_TYPE {
    {
      a <- 4;
      self;
    }
  };
};

class Cat inherits Animal {
  a : Int <- 5;
  say_hello() : SELF_TYPE {
    {
      a <- 5;
      self;
    }
  };
};

class Main inherits IO {
  a : Animal <- new Animal;
  b : Dog <- new Dog;
  main() : SELF_TYPE {
    {
      a.say_hello();
      b@Animal.say_hello();
    }
  };
};
