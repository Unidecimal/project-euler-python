# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

x = 1
hPrim = 0
target = 600851475143
while x <= target:
    if target % x == 0:
        target = target / x
        hPrim = x
    x += 2
print("hPrim: " + str(hPrim))
