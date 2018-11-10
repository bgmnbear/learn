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