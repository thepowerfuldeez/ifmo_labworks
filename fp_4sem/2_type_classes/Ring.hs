-- (1 балл) Определите класс типов Группа, 
-- https://ru.wikipedia.org/wiki/Группа_(математика).
class Monoid g => Group g where
  inv  :: g -> g 

-- (2 балла) Определите класс типов Кольцо (с единицей), 
-- https://ru.wikipedia.org/wiki/Кольцо_(математика).
class Group a => Ring a where
  mul :: a -> a -> a
  unit :: a
  -- a * (b * c) === (a * b) * c
  --     one * a === a
  --     a * one === a
  -- a * (b + c) === a * b + a * c

-- (3 балла) Определите тип данных Кольцо вычетов по модулю n 
-- представителем класса типов Кольцо (с единицей), 
-- https://ru.wikipedia.org/wiki/Сравнение_по_модулю#Классы_вычетов.
data RingMod = RingMod { rmRem :: Int, rmMod :: Int } deriving (Show, Eq)

ringMod :: Int -> Int -> RingMod
ringMod a m = RingMod (a `mod` m)  m

instance Monoid RingMod where
  mempty = ringMod 0 1
  mappend (RingMod a m) (RingMod b n) | m == n = ringMod (a + b) m
                                      | otherwise = undefined

instance Group RingMod where
  inv (RingMod a m) = ringMod (a - m) m

instance Ring RingMod where
  mul (RingMod a m) (RingMod b n) | m == n = ringMod (a * b) m
                                  | otherwise = undefined
  unit = ringMod 1 1

