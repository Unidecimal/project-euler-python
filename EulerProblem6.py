# The sum of the squares of the first ten natural numbers is,
#  1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#  ( 1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# 3025 - 385 = 2640
# and the square of the sum is. Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

squares_sum = 0
x_sum = 0
for x in range(1, 101):
    squares_sum += (x * x)
    x_sum += x

print(str((x_sum * x_sum) - squares_sum))

