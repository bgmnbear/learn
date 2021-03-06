import Data.List

numUniques :: (Eq a) => [a] -> Int
numUniques = length . nub

let stock = [(994.4,2008,9,1),(995.2,2008,9,2),(999.2,2008,9,3),(1001.4,2008,9,4),(998.3,2008,9,5)]   
head (dropWhile (\(val,y,m,d) -> val 1000) stock)

let (fw，rest) = span (/=' ') "This is a sentence" in "First word:" ++ fw ++ "，the rest:" ++ rest

map (\l@(x:xs) -> (x,length l)) . group . sort $ [1,1,1,1,2,2,2,2,3,3,2,2,2,5,6,7] 

search :: (Eq a) => [a] -> [a] -> Bool   
search needle haystack =   
  let nlen = length needle   
  in foldl (\acc x -> if take nlen x == needle then True else acc) False (tails haystack)


zipWith3 (\x y z -> x + y + z) [1,2,3] [4,5,2,2] [2,2,3]   

let values = [-4.3，-2.4，-1.2，0.4，2.3，5.9，10.5，29.1，5.3，-2.4，-14.5，2.9，2.3] 
groupBy (\x y -> (x > 0) == (y > 0)) values 

let xs = [[5,4,5,4,4],[1,2,3],[3,5,4,3],[],[2],[2,2]]  
sortBy (compare `on` length) xs

encode :: Int -> String -> String   
encode shift msg =  
  let ords = map ord msg   
  shifted = map (+ shift) ords   
  in map chr shifted

decode :: Int -> String -> String   
decode shift msg = encode (negate shift) msg


findKey :: (Eq k) => k -> [(k,v)] -> v  
findKey key xs = snd . head . filter (\(k,v) -> key == k) $ xs

findKey :: (Eq k) => k -> [(k,v)] -> Maybe v  
findKey key [] = Nothing 
findKey key ((k,v):xs) =  
     if key == k then  
         Just v  
     else  
         findKey key xs

findKey :: (Eq k) => k -> [(k,v)] -> Maybe v  
findKey key = foldr (\(k,v) acc -> if key == k then Just v else acc) Nothing


fromList' :: (Ord k) => [(k,v)] -> Map.Map k v  
fromList' = foldr (\(k,v) acc -> Map.insert k v acc) Map.empty


phoneBookToMap :: (Ord k) => [(k，String)] -> Map.Map k String 
phoneBookToMap xs = Map.fromListWith (\number1 number2 -> number1 ++ "，" ++ number2) xs


module Geometry   
( sphereVolume   
，sphereArea   
，cubeVolume   
，cubeArea   
，cuboidArea   
，cuboidVolume   
) where   

sphereVolume :: Float -> Float   
sphereVolume radius = (4.0 / 3.0) * pi * (radius ^ 3)   

sphereArea :: Float -> Float   
sphereArea radius = 4 * pi * (radius ^ 2)   

cubeVolume :: Float -> Float   
cubeVolume side = cuboidVolume side side side   

cubeArea :: Float -> Float   
cubeArea side = cuboidArea side side side   

cuboidVolume :: Float -> Float -> Float -> Float   
cuboidVolume a b c = rectangleArea a b * c   

cuboidArea :: Float -> Float -> Float -> Float   
cuboidArea a b c = rectangleArea a b * 2 + rectangleArea a c * 2 + rectangleArea c b * 2   

rectangleArea :: Float -> Float -> Float   
rectangleArea a b = a * b