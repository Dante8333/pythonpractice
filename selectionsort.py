def selectionsort(arr):
    n=len(arr)
    for i in range(0,n):
        minindex = i
        for j in range(i+1,n):
            if arr[minindex]>arr[j]:
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
    print("The sorted array: ",arr)
arr = []
a = int(input("enter number of values in the array: "))
for i in range(0,a):
    s = int(input("enter values into the array: "))
    arr.append(s)
print("The given array is: ",arr)
selectionsort(arr)
