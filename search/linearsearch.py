def linearsearch(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    else:
        return False


arr = [1,2,3,45,6,7,8,9]

if linearsearch(arr,9):
    print(linearsearch(arr,9))
else:
    print('element not found')