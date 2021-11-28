#  Each new term in the Fibonacci sequence is generated by 
#  adding the previous two terms. 
#  By starting with 1 and 2, the first 10 terms will be:
#   1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#  By considering the terms in the Fibonacci sequence whose
#  values do not exceed four million, find the sum of the even-valued terms.

x = 2
first = 2
second = 8 
sum = 10
while x < 4000:
    print(x) 
    x = (second * 4) + first
    print("New-x:" + x)
    sum = sum + x
    print("Summan:" + str(sum))
    first = second
    second = x
print("Sum of even-valued Fibonacci numbers is:" + str(sum)) 

