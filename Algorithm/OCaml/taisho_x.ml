(* 座標をx軸で対象にする *)
(* int * int -> int * int *)
let taisho_x pair = match pair with
   (a, b) -> (a, (-b))

let test1 = taisho_x (2, 3) = (2, -3)