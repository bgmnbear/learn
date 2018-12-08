data Bool = False | True
data Shape = Circle Float Float Float | Rectangle Float Float Float Float

surface :: Shape -> Float   
surface (Circle _ _ r) = pi * r ^ 2   
surface (Rectangle x1 y1 x2 y2) = (abs $ x2 - x1) * (abs $ y2 - y1)

data Shape = Circle Float Float Float | Rectangle Float Float Float Float deriving (Show)

data Point = Point Float Float deriving (Show)   
data Shape = Circle Point Float | Rectangle Point Point deriving (Show)

surface :: Shape -> Float
surface (Circle _ r) = pi * r ^ 2
surface (Rectangle (Point x1 y1) (Point x2 y2)) = (abs $ x2 - x1) * (abs $ y2 - y1)

nudge :: Shape -> Float -> Float -> Shape   
nudge (Circle (Point x y) r) a b = Circle (Point (x+a) (y+b)) r   
nudge (Rectangle (Point x1 y1) (Point x2 y2)) a b = Rectangle (Point (x1+a) (y1+b)) (Point (x2+a) (y2+b))

baseCircle :: Float -> Shape
baseCircle r = Circle (Point 0 0) r

baseRec :: Float -> Float -> Shape
baseRec width height = Rectangle (Point 0 0) (Point width height)


data Person = Person { firstName :: String   
                     , lastName :: String   
                     , age :: Int   
                     , height :: Float   
                     , phoneNumber :: String   
                     , flavor :: String   
                     } deriving (Show)


data Maybe a = Nothing | Just a

tellCar :: Car -> String 
tellCar (Car {company = c, model = m, year = y}) = "This " ++ c ++ " " ++ m ++ " was made in " ++ show y

tellCar :: (Show a) => Car String String a -> String   
tellCar (Car {company = c, model = m, year = y}) = "This " ++ c ++ " " ++ m ++ " was made in " ++ show y

data Vector a = Vector a a a deriving (Show)     
vplus :: (Num t) => Vector t -> Vector t -> Vector t   
(Vector i j k) `vplus` (Vector l m n) = Vector (i+l) (j+m) (k+n)     
vectMult :: (Num t) => Vector t -> t -> Vector t   
(Vector i j k) `vectMult` m = Vector (i*m) (j*m) (k*m)     
scalarMult :: (Num t) => Vector t -> Vector t -> t   
(Vector i j k) `scalarMult` (Vector l m n) = i*l + j*m + k*n


data Person = Person { firstName :: String   
                     , lastName :: String   
                     , age :: Int   
                     }

data Person = Person { firstName :: String   
                     , lastName :: String   
                     , age :: Int   
                     } deriving (Eq)   
                     
data Person = Person { firstName :: String   
                     , lastName :: String   
                     , age :: Int   
                     } deriving (Eq, Show, Read)                     


data Day = Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday    
           deriving (Eq, Ord, Show, Read, Bounded, Enum)                     


           
import qualified Data.Map as Map   

data LockerState = Taken | Free deriving (Show, Eq)   

type Code = String   

type LockerMap = Map.Map Int (LockerState, Code)  

lockerLookUp :: Int -> LockerMap -> Either String Code
lockerLookUp num map = 
    case Map.lookup num map of 
        Nothing -> Left "Nothing"
        Just (state, code) -> if state /= Taken
                              then Right code
                              else Left "Taken"