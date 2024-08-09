def bubble(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    print(arr)

arr = [100,999,1,10,0,6,2,1,1,2]

bubble(arr)