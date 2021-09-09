# Method definition
def intersect_array(arr1, arr2):
    set_arr1 = set(arr1)
    set_arr2 = set(arr2)

    if set_arr1 < set_arr2:
        return [x for x in set_arr1 if x in set_arr2]
    else:
        return [x for x in set_arr2 if x in set_arr1]

# Driver code
arr1 = [1, 3, 5, 7, 9, 10, 12]
arr2 = [2, 5, 6, 8, 12]

result = []
result = intersect_array(arr1, arr2)
print("Intersected values between arr1 and arr2:")

for i in range(len(result)):
    print(result[i], end=' ')