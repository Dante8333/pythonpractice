def bubblesort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print("sorted array = ",arr)
arr = []
num =int(input("enter number of values for array: "))
for i in range(0,num):
    s=int(input("enter values in the array: "))
    arr.append(s)
print('given array = ',arr)
bubblesort(arr)

