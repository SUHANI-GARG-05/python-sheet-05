# 6. Even - Odd difference
A = [1, 2, 3, 4]
even = 0
odd = 0
for num in A:
    if (num % 2 == 0):
        even = even + 1
    else:
        odd = odd + 1
print("Difference =", abs(even - odd))



#OUTPUT
'''
Difference = 0
'''