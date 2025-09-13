# 3. Max and Min
A = [1, 2, 3, 4, 5]
max = A[0]
min = A[0]
for num in A:
    if (num > max):
        max = num
    if (num < min):
        min = num
print("Max =", max, "Min =", min)



#OUTPUT
'''
Max = 5 Min = 1
'''