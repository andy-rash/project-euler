
-- fib :: Int -> Int
-- fib x
--   | x < 2 = 1
--   | otherwise = fib (x - 1) + fib (x - 2)

-- Fancy Binet's formula for constant-time evaluation of Fibonacci numbers
fib :: Int -> Int
fib n = round $ phi ** fromIntegral n / sq5
  where
    sq5 = sqrt 5 :: Double
    phi = (1 + sq5) / 2

fibs :: [Int]
fibs = map fib [1..]

-- Paul's fancy shit
-- fibs = 1 : 2 : zipWith (+) fibs (tail fibs)

r = sum (filter even (takeWhile (<4000000) fibs))

main = print r
