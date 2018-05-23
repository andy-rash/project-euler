
-- prime factors function from:
--   https://stackoverflow.com/questions/21276844/prime-factors-in-haskell
prime_factors n =
  case factors of
    [] -> [n]
    _  -> factors ++ prime_factors (n `div` (head factors))
  where factors = take 1 $ filter (\x -> (n `mod` x) == 0) [2..n-1]

r = maximum (prime_factors 600851475143)

main = print r
