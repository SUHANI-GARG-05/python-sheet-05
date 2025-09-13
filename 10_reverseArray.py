# 10. Reverse array
A = [3, 5, 1, 2, 1, 2]
rev = []
for i in range(len(A)-1, -1, -1):
    rev.append(A[i])
print("Reversed =", rev)



#OUTPUT
'''
Reversed = [2, 1, 2, 1, 5, 3]
'''