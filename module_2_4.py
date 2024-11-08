numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [2,3,5,7,11,13]
not_primes = [4,6,8,9,10,12,14,15]
for i in numbers :
    print (i)
def is_prime (n):
    f = 2
    while n % f != 0 :
        f += 1
    return f == n
print (is_prime(15))
print (primes)
print (not_primes)





