def selectionsort(arr):
    n = len(arr)

    for i in range(n):
        Min = i
        for j in range(i+1,n):
            if arr[j] < arr[Min]:
                temp = arr[j]
                arr[j] = arr[Min]
                arr[Min] = temp
    
    print(arr)

arr = [9,3,4,0,12,173,739,7288,7830]
selectionsort(arr)