def solution2(arr, value):
    i = 0
    multiplier = 1
    left_bound = 0
    right_bound = 0
    len_arr = len(arr)
    # no need to check lenght but still putting it for testing since i can only enter finite array
    while(True and right_bound<len_arr):
#         print("left_bound,right_bound,i",left_bound,right_bound,i)
        
        if i==0 and arr[i] > value:
            return 'no such element'
        elif arr[i] > value:
            response = binarySearch(arr,left_bound,right_bound,value)
            if response != -1:
                return response
            else:
                return "no such element"
        elif arr[i] == value:
            return 'position ' + str(i+1)
        else:
            if arr[i] < value:
                left_bound = i
                right_bound = left_bound+ 10 * multiplier
                i = right_bound
                multiplier = multiplier*2

def binarySearch (arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1