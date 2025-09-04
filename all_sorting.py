#bubble sorting
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr       


#selection sort
def selection_sort(arr):
    for i in range(len(arr)-1):
        minn=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minn]:
                minn=j
        arr[i],arr[minn]=arr[minn],arr[i]
    
    return arr


#insertion sorting
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr


#merge sorting
def merge_sort(arr):
    if len(arr) > 1:  
        mid = len(arr) // 2   
        left = arr[:mid]     
        right = arr[mid:]    
        merge_sort(left)
        merge_sort(right)   
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

