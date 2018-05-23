
isPalindrome :: Int -> Bool
isPalindrome a = show a == reverse (show a)

r = maximum (filter isPalindrome [ x*y | x <- [100..999], y <- [100..999]])

main = print r
