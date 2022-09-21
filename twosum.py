def twosum(arr,target):
    for i in range(0,len(arr)):
        for j in range(1,len(arr)):
           if arr[j] == target - arr[i]:
            print(arr[i],arr[j])
arr = [2,7,11,15]
twosum(arr,9)
            
    

        

