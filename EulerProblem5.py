# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder. What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?


def is_divide_number(number):
    for x in range(1, 20):
        if number % x != 0:
            return False
    return True


tested = 1
while not is_divide_number(tested):
    tested += 1

print(str(tested))
