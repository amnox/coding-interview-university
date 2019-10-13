arr = [64, 34, 25, 12, 22, 11, 90] 

def bubble(arr,swaps):
    i=0
    lee = len(arr)
    cnt = 0
    tmp = 0
    while (swaps):
        print (i, lee, cnt, tmp, arr, swaps)
        if i+1 == lee-1:
            if cnt ==0:
                swaps=False
                
            i = 0
            cnt = 0
            continue
        if arr[i]<arr[i+1]:
            i+=1
            continue
        if arr[i]>arr[i+1]:
            
            tmp = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = tmp
            cnt+=1
            i+=1
        
    return 0

swaps = True

#bubble(arr,swaps)
