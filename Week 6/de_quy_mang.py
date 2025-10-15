def print_array(arr, i=0):
    if i == len(arr):    
        return
    print(arr[i], end=" ")
    print_array(arr, i + 1)  

arr = [1, 2, 3, 4]
print_array(arr)   
