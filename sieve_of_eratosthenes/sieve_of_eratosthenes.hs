-- How to use
-- either inifite list using sieve:
-- sieve [2..]
--
-- Or using sieve_of_eratosthenes:
-- sieve_of_eratosthenes 29

-- returns list of prime numbers from list of integers
sieve :: [Int] -> [Int]
sieve [] = []
sieve (n:l) = n:(sieve [ m | m <- l, m `mod` n > 0 ])

-- returns list of prime number up until n
sieve_of_eratosthenes n = sieve [2..n]
