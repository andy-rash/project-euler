
r = sum [x | x <- [1..999], x `rem` 3 == 0 || x `rem` 5 == 0]

main = print r
