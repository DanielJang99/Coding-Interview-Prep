from typing import List

def peakIndexInMountainArray(arr: List[int]) -> int:
    min, max = 1, len(arr) -1 
    while(min <= max):
        cur_index = (min + max) // 2
        if arr[cur_index] > arr[cur_index-1] and arr[cur_index] > arr[cur_index+1]:
            return cur_index
        if arr[cur_index] > arr[cur_index-1]:
            min = cur_index +1 
        else:
            max = cur_index -1 
