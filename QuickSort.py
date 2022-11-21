import random 

def QuickSort(arr,start,stop):
    if(start<stop):
        pivot=partition_r(arr,start,stop)
        #print(pivot)
        QuickSort(arr,start,pivot-1)
        QuickSort(arr,pivot+1,stop)

def partition_r(arr,start,stop):
    pivot=random.randrange(start,stop)
    arr[start],arr[pivot]=arr[pivot],arr[start]
    return partition(arr,start,stop)

def partition(arr,start,stop):
    pivot=start 
    i=start+1 
    for j in range(start+1,stop+1):
        if(arr[j]<=arr[pivot]):
            arr[j],arr[i]=arr[i],arr[j]
            i=i+1 
    arr[pivot],arr[i-1]=arr[i-1],arr[pivot]
    pivot=i-1 
    return pivot 

arr=[10,1,5,7,9,8]
QuickSort(arr,0,5)
print(arr)