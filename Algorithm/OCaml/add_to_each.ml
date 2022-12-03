(*目的：受け取ったlstの要素をそれぞれの頭にくっつける *)
(*add_to_each : int -> int list list -> int list list *)
let rec add_to_each n lst = match lst with
    [] -> []
  | first :: rest -> (n :: first) :: add_to_each n rest (*add_to_each n rest *)

let test4  = add_to_each 1 [[2]; [2; 3]; [2; 3; 4]]
           = [[1; 2]; [1; 2; 3]; [1; 2; 3; 4]]