def insertionsort(arr):
    for i in range(1,len(arr)):
        value = arr[i]

        j = i-1
        while j>=0 and value < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
            arr[j+1] = value
    print('sorted array: ',arr)
arr = []
a = int(input("enter number of values for array: "))
for i in range(a):
    s = int(input("enter values for array: "))
    arr.append(s)
print('given array: ',arr)
insertionsort(arr) 
