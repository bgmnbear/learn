applyTwice (a -> a) -> a -> a 
applyTwice f x = f (f x)

zipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith _ [] _ = []
zipWith _ _ [] = []
zipWith f (x:xs) (y:ys) = (f x y) : zipWith f xs ys

flip' :: (a -> b -> c) -> b -> a -> c   
flip' f y x = f x y

map :: (a -> b) -> [a] -> [b]
map _ [] = []
map f (x:xs) =  (f x):map f xs

filter :: (a -> Bool) -> [a] -> [a]   
filter _ [] = []   
filter p (x:xs)    
    | p x       = x : filter p xs   
    | otherwise = filter p xs