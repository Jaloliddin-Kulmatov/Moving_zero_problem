
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


triangle = []
time = 3
for i in range(time):
    row = [1]
    if triangle:
        last_row = triangle[-1]
        for j in range(1, len(last_row)):
            row.append(last_row[j-1] + last_row[j])

        row.append(1)
    triangle.append(row)
print(triangle)


nums = [-4,-1,0,3,10]
positive_nums = []
for i in nums:
    if i < 0:
        i*=-1
        positive_nums.append(i)
    else:
        positive_nums.append(i)
print(positive_nums)

sorted_nums = sorted(positive_nums)
print(sorted_nums)
squared_nums = []
for i in sorted_nums:
    squared_nums.append(i*i)
print(squared_nums)
