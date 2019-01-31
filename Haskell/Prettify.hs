module Prettify where
import Prelude hiding ((<>)) 
import Data.Bits (shiftR, (.&.))
import Data.Char (ord)
import Numeric (showHex)

data Doc = Empty
        | Char Char
        | Text String
        | Line
        | Concat Doc Doc
        | Union Doc Doc
        deriving (Show, Eq)

empty :: Doc
empty = Empty

char :: Char -> Doc
char c = Char c

text :: String -> Doc
text "" = Empty
text s  = Text s

double :: Double -> Doc
double d = text (show d)

line :: Doc
line = Line

string :: String -> Doc
string = enclose '"' '"' . hcat . map oneChar

(<>) :: Doc -> Doc -> Doc
a <> Empty = a
Empty <> a = a
a <> b = a `Concat` b

enclose :: Char -> Char -> Doc -> Doc
enclose left right x = char left <> x <> char right


hcat :: [Doc] -> Doc
hcat = fold (<>)

fold :: (Doc -> Doc -> Doc) -> [Doc] -> Doc
fold f = foldr f empty

oneChar :: Char -> Doc
oneChar c = case lookup c simpleEscapes of
              Just r -> text r
              Nothing | mustEscape c -> hexEscape c
                      | otherwise    -> char c
    where mustEscape c = c < ' ' || c == '\x7f' || c > '\xff'

simpleEscapes :: [(Char, String)]
simpleEscapes = zipWith ch "\b\n\f\r\t\\\"/" "bnfrt\\\"/"
    where ch a b = (a, ['\\',b])

hexEscape :: Char -> Doc
hexEscape c | d < 0x10000 = smallHex d
            | otherwise = astral (d - 0x10000)
        where d = ord c

smallHex :: Int -> Doc
smallHex x = text "\\u" 
            <> text (replicate (4 - (length hex)) '0') 
            <> text hex
    where hex = showHex x ""

astral :: Int -> Doc
astral x = smallHex (a + 0xd800) <> smallHex (b + 0xdc00)
    where a = (x `shiftR` 10) .&. 0x3ff
          b = x .&. 0x3ff

series :: Char -> Char -> (a -> Doc) -> [a] -> Doc
series open close f = enclose open close 
                    . fsep . punctuate (Char ',') . map f

punctuate :: Doc -> [Doc] -> [Doc]
punctuate p []     = []
punctuate p [d]    = [d]
punctuate p (d:ds) = (d <> p) : punctuate p ds

fsep :: [Doc] -> Doc
fsep = fold (</>)

(</>) :: Doc -> Doc -> Doc
a </> b = a <> softline <> b

softline :: Doc
softline = group line

group :: Doc -> Doc
group x = flatten x `Union` x

flatten :: Doc -> Doc
flatten (x `Concat` y) = flatten x `Concat` flatten y
flatten Line           = Char ' '
flatten (x `Union` _)  = flatten x
flatten other          = other

compact :: Doc -> String
compact x = transform [x]
    where transform [] = ""
          transform (d:ds) = 
            case d of 
                Empty -> transform ds
                Char c -> c : transform ds
                Text s -> s ++ transform ds
                Line -> '\n' : transform ds
                a `Concat` b -> transform (a:b:ds)
                _ `Union` b -> transform (b:ds)

nicest col a b width
    | (width - least) `fits` a = a
    | otherwise                = b
    where least = min width col                                    

pretty :: Int -> Doc -> String
pretty width x = best 0 [x]
    where best _ _ = ""
          best col (d:ds) = 
            case d of
            Empty        -> best col ds
            Char c       -> c :  best (col + 1) ds
            Text s       -> s ++ best (col + length s) ds
            Line         -> '\n' : best 0 ds
            a `Concat` b -> best col (a:b:ds)
            a `Union` b  -> nicest col (best col (a:ds))
                                       (best col (b:ds))
                                       width
  
fits :: Int -> String -> Bool
w `fits` _ | w < 0 = False
w `fits` ""        = True
w `fits` ('\n':_)  = True
w `fits` (c:cs)    = (w - 1) `fits` cs
