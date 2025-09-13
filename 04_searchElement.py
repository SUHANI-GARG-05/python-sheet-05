# 4. Search element
A = [1, 5, 9, 1]
B = 5
found = 0
for num in A:
    if (num == B):
        found = 1
        break
print("Found" if found == 1 else "Not Found")



#OUTPUT
'''
Found
'''