module DayFourB where

import Data.List
import Data.Char

-----------------------------------------------------------------------------

run file = do
    f <- readFile file
    let input = map words $ lines f
    print (validPassphrases input)


validPassphrases :: Ord a => [[[a]]] -> Int
validPassphrases is = length [i | i <- is, not (anagram i)]


anagram :: Ord a => [[a]] -> Bool
anagram ss = duplicates $ map sort ss


duplicates :: Eq a => [a] -> Bool
duplicates [] = False
duplicates (x:xs) 
    | x `elem` xs = True
    | otherwise   = duplicates xs
