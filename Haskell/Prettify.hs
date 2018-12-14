string :: String -> Doc
string = enclose '"' '"' . hcat . map oneChar

enclose :: Char -> Char -> Doc -> Doc
enclose left right x = char left <> x <> char right

(<>) :: Doc -> Doc -> Doc
a <> b = undefined

char :: Char -> Doc
char c = undefined

hcat :: [Doc] -> Doc
hcat [] = JNull
hcat [x:xs] = x <> hcat xs

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

