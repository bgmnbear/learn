import Data.List

numUniques :: (Eq a) => [a] -> Int
numUniques = length . nub

let stock = [(994.4,2008,9,1),(995.2,2008,9,2),(999.2,2008,9,3),(1001.4,2008,9,4),(998.3,2008,9,5)]   
head (dropWhile (\(val,y,m,d) -> val 1000) stock)

let (fw，rest) = span (/=' ') "This is a sentence" in "First word:" ++ fw ++ "，the rest:" ++ rest