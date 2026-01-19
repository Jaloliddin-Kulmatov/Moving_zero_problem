#
# def moveZeroes(nums: list) -> list:
#     count = 0
#
#     for i, num in enumerate(nums):
#
#         if num == 0:
#             count += 1
#             continue
#         nums[i], nums[i-count] = nums[i-count], nums[i]
#
#     return nums
#
# nums = [1,2,3,4,5,6,7]
# k = 3
# first_part = len(nums) - k
# new_list = nums[first_part:] + nums[:first_part]
# print(new_list)
#
#
# triangle = []
# time = 3
# for i in range(time):
#     row = [1]
#     if triangle:
#         last_row = triangle[-1]
#         for j in range(1, len(last_row)):
#             row.append(last_row[j-1] + last_row[j])
#
#         row.append(1)
#     triangle.append(row)
# print(triangle)
#
#
# nums = [-4,-1,0,3,10]
# positive_nums = []
# for i in nums:
#     if i < 0:
#         i*=-1
#         positive_nums.append(i)
#     else:
#         positive_nums.append(i)
# print(positive_nums)
#
# sorted_nums = sorted(positive_nums)
# print(sorted_nums)
# squared_nums = []
# for i in sorted_nums:
#     squared_nums.append(i*i)
# print(squared_nums)
#
# height = [1,8,6,2,5,4,8,3,7]
# answer = 0

#water storage
#1
# for i in range(len(height)):
#     for j in range(i + 1, len(height)):
#         width = j-i
#         area = min(height[i], height[j]) * width
#
#         if area > answer:
#             answer = area
# print(answer)

#2

# max_area = 0
#
# while j > i:
#     area = (j-i) * min(height[j], height[i])
#     if area > max_area:
#         max_area = area
#     if height[i] < height[j]:
#         i +=1
#     else:
#         j-=1
# print(max_area)


#arqon tortish
#1
# nums = [1, 2, 3, 4]
# result = []
#
# for i in range(len(nums)):
#     if sum(nums[:i]) > sum(nums[i+1:]):
#         result.append(-1)
#     elif sum(nums[:i]) < sum(nums[i+1:]):
#         result.append(1)
#     else:
#         result.append(0)
#
# print(result)

#2
# nums = [1, 2, 3, 4]
# left, right = 0, sum(nums)
# result = []
#
# for num in nums:
#     right -= num
#
#     if right - left > 0:
#         result.append(1)
#     elif right - left < 0:
#         result.append(-1)
#     else:
#         result.append(0)
#
#     left += num
# print(result)

#multiplier

# nums = [1,2,3,4]
# result = []
#
# for i in range(0, len(nums)):
#     new_list = nums[:i] + nums[i+1:]
#     answer = 1
#     for j in new_list:
#         answer = answer * j
#     result.append(answer)
# print(result)

# nums = [1,2,3,4]
# prefix = []
# suffix = []
#
# product = 1
#
# for num in nums:
#     product*=num
#     prefix.append(product)
# product = 1
# for num in reversed(nums):
#     product *= num
#     suffix.append(product)
# suffix.reverse()
#
# result = []
# for i in range(len(nums)):
#     left, right = 1,1
#     if i >0:
#         left = prefix[i-1]
#     if i < len(nums) -1:
#         right = suffix[i+1]
#     product = left * right
#     result.append(product)
# print(result)