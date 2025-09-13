# 7. Separate Odd and Even
A = [1, 2, 3, 4, 5]
print("Odd numbers:")
for num in A:
    if (num % 2 != 0):
        print(num, end=" ")
print("\nEven numbers:")
for num in A:
    if (num % 2 == 0):
        print(num, end=" ")
print()



#OUTPUT
'''
Odd numbers:
1 3 5
Even numbers:
2 4
'''