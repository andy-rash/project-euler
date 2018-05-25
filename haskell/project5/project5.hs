import Data.List (find)

-- What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

-- by only considering multiples of 20 and then only checking those multiples
-- only against the numbers in [1..20] that do not evenly divide 20, we can
-- shave off a significant amount of overhead in attempting to find the
-- correct answer

f :: Int -> Bool
f a = all (\x -> a `rem` x == 0) [3,6,7,8,9,11,12,13,14,15,16,17,18,19]

r = find f [20,40..]

main = print r
