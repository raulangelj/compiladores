(* This program should print
"Hello" to the screen. *)
-- this is a comment
(* this is a bad comment)
class Main inherits IO {
    main(): SELF_TYPE {
	  out_string("Hello")
   };
};