doubleMe x = x + x
doubleUs x y = doubleMe x + doubleMe y
doubleSmallNumber x = if x > 100 then x else  x*2

let lostNumbers = [4,8,15,16,23,48]
lostNumbers !! 2

[3,2,1] > [2,1,0]