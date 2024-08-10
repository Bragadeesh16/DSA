def inserionsort(arr):
    n = len(arr)
    i =1

    for i in range(n):
        temp = arr[i]
        j = i-1
        while ((j >= 0) and (arr[j] > temp)):
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = temp

    print(arr)
    

arr = [2,5,1,3,2,7,5]
inserionsort(arr)