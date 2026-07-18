# find index on n by using binary search

arr = [1, 2, 3, 4, 5, 6]   
target = 100
def find(arr:list, target:int):
    left = 0
    right = len(arr)-1
    
    while left <= right:
        mid = (left + right)//2
        if result == arr[mid]:
            return mid

        elif result >  arr[mid]:
            left = mid+1
        else:
            right = mid -1
            
    return -1 
print(find(arr, target))

# best case = O(1) -> when target is in middle -  (left + right)//2
