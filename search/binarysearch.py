def binarysearch(arr,key):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if key > arr[mid]:
            low = mid+1
        elif key < arr[mid]:
            high = mid -1
        else:
            return mid
    return -1

arr = [1,2,3,4,5,6,7]
location = binarysearch(arr,1)

if location <= 0:
    print('the element is present in index ',location)
else:
    print('the element is not found')