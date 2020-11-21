def bubbleSort(arr):
    temp = 0
    for i in range(1,arr.length):
        for j in range(0, arr.length-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

arr = [4, 2, 6, 3, 8, 9, 0, 7, 1, 5]

bubbleSort(arr)
for i in arr:
    print(i)

