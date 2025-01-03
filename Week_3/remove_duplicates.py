# def removeDuplicates(self, nums):
#         if not nums:
#             return 0
        
#         unique_index = 0
#         for i in range(1, len(nums)):
#             if nums[i] != nums[unique_index]:
#                 unique_index += 1
#                 nums[unique_index] = nums[i]
        
#         return unique_index + 1

def removeDuplicates(nums):
    unique_index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]
    return unique_index + 1

nums = [int(x) for x in input("Enter a sorted list of integers (space-separated): ").split()]

k = removeDuplicates(nums)

print(f"The number of unique elements is: {k}")
print(f"The modified array is: {nums[:k]}")
