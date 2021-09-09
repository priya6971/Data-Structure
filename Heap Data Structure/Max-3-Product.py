import heapq

# Method Definitions --------------------------------
def max_product(arr):
    '''
    heap = []
    for i in range(len(arr)):
        heapq.heappush(heap, arr[i])
    '''
    a = heapq.nlargest(3, arr)
    b = heapq.nsmallest(2, arr)

    return max((a[0]*a[1]*a[2]),(b[0]*b[1]*a[0]))

# Driver code
arr = [-5, -4, 3, 1]
result = max_product(arr)
print("Maximum Product of three numbers is:", result)