factorial :: (Integral a) => a -> a   
factorial 0 = 1   
factorial n = n * factorial (n - 1) 

addVectors :: (Num a) => (a, a) -> (a, a) -> (a, a)   
addVectors (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)  

first :: (a, b, c) -> a   
first (x, _, _) = x   

second :: (a, b, c) -> b   
second (_, y, _) = y   

third :: (a, b, c) -> c   
third (_, _, z) = z  

head' :: [a] -> a
head' (x:_) = x

tell :: (Show a) => [a] -> String   
tell [] = "The list is empty"   
tell (x:[]) = "The list has one element: " ++ show x   
tell (x:y:[]) = "The list has two elements: " ++ show x ++ " and " ++ show y   
tell (x:y:_) = "This list is long. The first two elements are: " ++ show x ++ " and " ++ show y  

length' :: (Num b) => [a] -> b
length' [] = 0
length' (_:xs) = 1 + length' xs

sum' :: (Num b) => [a] -> b
sum' [] = 0
sum' (x:xs) = x + sum' xs

capital :: String -> String   
capital "" = "Empty string, whoops!"   
capital all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]  

bmiTell :: (RealFloat a) => a -> String   
bmiTell bmi   
    | bmi  18.5 = "You're underweight, you emo, you!"   
    | bmi  25.0 = "You're supposedly normal. Pffft, I bet you're ugly!"   
    | bmi  30.0 = "You're fat! Lose some weight, fatty!"   
    | otherwise   = "You're a whale, congratulations!"
    
max' :: (Ord a) => a -> a -> a   
max' a b    
    | a > b     = a   
    | otherwise = b  

myCompare :: (Ord a) => a -> a -> Ordering   
a `myCompare` b   
    | a > b     = GT   
    | a == b    = EQ   
    | otherwise = LT  

initials :: String -> String -> String   
initials firstname lastname = [f] ++ ". " ++ [l] ++ "."   
    where (f:_) = firstname   
          (l:_) = lastname  

calcBmis :: (RealFloat a) => [(a, a)] -> [a]   
calcBmis xs = [bmi w h | (w, h)]
    where bmi weight height = weight / height ^ 2  

cylinder :: (RealFloat a) => a -> a -> a   
cylinder r h =  
    let sideArea = 2 * pi * r * h   
        topArea = pi * r ^2   
    in  sideArea + 2 * topArea 

head' :: [a] -> a   
head' xs = case xs of [] -> error "No head for empty lists!"   
                      (x:_) -> x  


maximum' :: (Ord a) => [a] -> a   
maximum' [] = error "maximum of empty list"   
maximum' [x] = x   
maximum' (x:xs)    
    | x > maxTail = x   
    | otherwise = maxTail   
    where maxTail = maximum' xs

maximum' :: (Ord a) => [a] -> a
maximum' [] = error "maximum of empty list"
maximum' [x] = x
maximum' (x:xs) = max x (maximum' xs)

replicate' :: (Num i, Ord i) => i -> a -> [a]   
replicate' n x   
    | n  0    = []   
    | otherwise = x:replicate' (n-1) x

take' :: (Num i, Ord i) => i -> [a] -> [a]   
take' n _   
    | n  0   = []   
take' _ []     = []   
take' n (x:xs) = x : take' (n-1) xs

reverse :: [a] -> [a]
reverse [] = []
reverse (x:xs) = reverse xs ++ [x]

repeat :: a -> [a]
repeat x = x:repeat x

zip :: [a] -> [b] -> [(a,b)]
zip [],_ = []
zip _,[] = []
zip (x:xs) (y:ys) = (x,y):zip xs ys

elem' :: (Eq a) => a -> [a] -> Bool   
elem' a [] = False   
elem' a (x:xs)   
    | a == x    = True   
    | otherwise = a `elem'` xs