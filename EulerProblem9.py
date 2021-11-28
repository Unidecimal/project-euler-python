# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def find_triplet_sum(known_sum):
    for a in range(1, known_sum + 1):
        for b in range(a + 1, known_sum + 1):
            if a + b + (known_sum - a - b) == known_sum and a < b < (known_sum - a - b) and a * a + b * b == (
                        known_sum - a - b) * (known_sum - a - b):
                triplet_sum = a * b * (known_sum - a - b)
                return a, b, known_sum - a - b, triplet_sum


print(str(find_triplet_sum(1000)))
