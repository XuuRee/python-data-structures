def sort(arr):
    count = []
    s = [0] * len(arr)
    for i in range(len(arr)):
        count.append(0)
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                count[j] +=1
            else:
                count[i] +=1
    i = 0
    for i in range(len(arr)):
        s[count[i]] =  arr[i]



def sort2(arr,k):
    c =[]
    s = [-1] * len(arr)
    for i in range(k):
        c.append(0)
    for i in range(len(arr)):
        c[arr[i]] +=1
    for i in range(1,k):
        c[i] = c[i] + c[i-1]
    for i in range(len(arr)-1,-1,-1):
        c[arr[i]] -=1
        s[c[arr[i]]] = arr[i]
    o = 9



sort([1,5,2,7,4,6,0,9])
sort2([5,4,2,1,3],6)
