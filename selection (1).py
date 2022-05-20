def selectionSort(array,size):
    for step in range(size):
        mid_idx=step
        
        for i in range(step+1,size):
            
            if array[i]<array[mid_idx]:
                mid_idx=i
                
        (array[step],array[mid_idx])=(array[mid_idx],array[step])
            
data=[11,0,8,6]
size=len(data)
selectionSort(data,size)
print(data)
