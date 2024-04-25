def insertion(A):
    for i in range(2,len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key

# A = [32,12,23,8,0,2,43,55]
# print(A)
# insertion(A)
# print(A)