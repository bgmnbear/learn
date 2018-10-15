doubleMe x = x + x
doubleUs x y = doubleMe x + doubleMe y
doubleSmallNumber x = if x > 100 then x else  x*2

let lostNumbers = [4,8,15,16,23,48]
lostNumbers !! 2

[3,2,1] > [2,1,0]

['a'..'z']
[2,4..20]

take 10 (cycle [1,2,3])  

[x*2 | x  [1..10]]
[x*2 | x  [1..10], x*2 >= 12]

boomBangs xs = [ if x 10 then "BOOM!" else "BANG!" | x  xs, odd x]  
[ x*y | x  [2,5,10], y  [8,10,11]]  

length' xs = sum [1 | _  xs]  
removeNonUppercase st = [ c | c  st, c `elem` ['A'..'Z']]  
[ [ x | x  xs, even x ] | xs  xxs

fst (8, 11)
snd (8, 11)

zip [1,2,3,4,5] [5,5,5,5,5]

let rightTriangles' = [ (a,b,c) | c  [1..10], b  [1..c], a  [1..b], a^2 + b^2 == c^2, a+b+c == 24] 


addThree :: Int -> Int -> Int -> Int   
addThree x y z = x + y + z