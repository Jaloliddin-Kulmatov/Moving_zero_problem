
def moveZeroes(nums: list) -> list:
    count = 0

    for i, num in enumerate(nums):

        if num == 0:
            count += 1
            continue
        nums[i], nums[i-count] = nums[i-count], nums[i]

    return nums

nums = [1,2,3,4,5,6,7]
k = 3
first_part = len(nums) - k
new_list = nums[first_part:] + nums[:first_part]
print(new_list)