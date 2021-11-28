# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13. What is the 10 001st prime number?

def find_prim(number, plist):
    if number == 0 or number == 1:
        return False
    elif number == 2:
        return True
    else:
        for x in range(len(plist)):
            if number % prim_list[x] == 0:
                return False
        return True


prim_list = []
test_prim = 1
while len(prim_list) < 10001:
    if find_prim(test_prim, prim_list):
        prim_list.append(test_prim)
    test_prim += 1

print(prim_list[10000])
