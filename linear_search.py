def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
arr=[1,3,8,5,2]
x=6
print("element found at index " + str(linear_search(arr, x)))







