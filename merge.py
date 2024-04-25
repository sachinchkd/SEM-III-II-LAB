
def mergeSort(A):

    if len(A) <= 1:
        return A
    
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i = i + 1
        else:
            merged.append(right[j])
            j = j + 1

    while i < len(left):
        merged.append(left[i])
        i = i + 1
    
    while j < len(right):
        merged.append(right[j])
        j = j + 1
    
    return merged