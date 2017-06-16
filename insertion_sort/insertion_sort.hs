isort :: Ord a => [a] -> [a]
isort [] = []
isort (x:l) = insert(x, isort l)
    where
        insert :: Ord a => (a, [a]) -> [a]
        insert (y, []) = [y]
        insert (y, z:zs) =
            if y <= z then y:(z:zs)
            else z:(insert(y, zs))
