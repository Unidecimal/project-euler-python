# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


# Test if a number is a prim number returns bool.
def find_prim(number, plist):
    # Check for known not prim numbers
    if number == 0 or number == 1:
        return False
    # check for first known prim number
    elif number == 2:
        return True
    else:
        # test the number against earlier found prims in list.
        for x in range(len(plist)):
            # Check so that you not test to many old prims against the new, to cut time.
            if prim_list[x] * prim_list[x] > number:
                return True
            elif number % prim_list[x] == 0:
                return False
        return True


# Returns the sum of all prims
def sum_list(plist):
    total = 0
    for x in range(len(plist)):
        total += plist[x]
    return total


prim_list = []
test_prim = 2
while test_prim < 2000000:
    # Sends the list of found prims and the new number to test
    if find_prim(test_prim, prim_list):
        prim_list.append(test_prim)
    # Ensure only uneven numbers ar tested
    if test_prim < 3:
        test_prim += 1
    else:
        test_prim += 2


length = len(prim_list)
print(prim_list[length - 1])
print(sum_list(prim_list))



