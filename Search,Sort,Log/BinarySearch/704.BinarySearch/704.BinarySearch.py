finding_target = 2
finding_nums = [0, 2, 4]

def binary_search(nums, target: int) -> int:
    min, max = 0, len(nums) - 1
    while min < max: 
        mid = min + (max - min) // 2
        if nums[mid] < target: min = mid + 1
        else: max = mid
    return min if nums[min] == target else -1


res = binary_search(finding_nums, finding_target)
print(res)
