# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
from typing import Any, Union


def check_palindrome(number):
    string = str(number)
    rev_string = str(number)[::-1]
    if string == rev_string:
        return True
    else:
        return False


def check_if_not_pal_list(number, pal_list):
    if number in pal_list:
        return False
    else:
        return True


factor_A = 999
factor_B = 999
findingP = 0
list_pal = []
while factor_B != 100:
    if factor_A != 100:
        findingP = factor_A * factor_B
        if check_palindrome(findingP) and check_if_not_pal_list(findingP, list_pal):
            list_pal.append(findingP)
        factor_A -= 1
    else:
        factor_B -= 1
        factor_A = 999
print(list_pal)

highest = 0
for x in range(len(list_pal)):
    if list_pal[x] > highest:
        highest = list_pal[x]
print(highest)

