module DayFour where

import Data.List
import Data.Char

-----------------------------------------------------------------------------

duplicates :: Eq a => [a] -> Bool
duplicates [] = False
duplicates (x:xs) 
    | x `elem` xs = True
    | otherwise   = duplicates xs


validPassphrases is = length [i | i <- is, not (duplicates i)]


run file = do
    f <- readFile file
    let input = map words $ lines f
    print (validPassphrases input)
