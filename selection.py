def selection(A):
    for i in range(len(A)-1):
        min = i
        for j in range(i+1,len(A)):
            if A[j] < A[min] :
                min = j
            j = j + 1
        temp = A[i]
        A[i] = A[min]
        A[min] = temp
        i = i+1

# A = [32,12,23,8,0,2,43,55]
# print(A)
# selection(A)
# print(A)