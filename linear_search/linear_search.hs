lsearch :: (Eq a) => (a, [a]) -> Bool
lsearch (_, []) = False
lsearch (z, x:xs) =
    if z == x then True
    else lsearch (z, xs)
