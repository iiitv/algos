euclid :: (Int, Int) -> Int
euclid (n,m)
    | n == m = n
    | n < m = euclid(n, m-n)
    | otherwise = euclid(n-m, m)
