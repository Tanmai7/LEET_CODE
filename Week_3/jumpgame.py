def Jump(num):
    maxEnd = 0
    for i in range(len(num)):
        if i > maxEnd:
            return False
        maxEnd = max(maxEnd, i + num[i])
        if maxEnd >= len(num) - 1:
            return True
    return False

num = list(map(int, input("Enter the numbers separated by space: ").split()))
result = Jump(num)
print(result)


#=================================================================
#logic


# def canJump(nums):
#     maxReach = 0
#     for i in range(len(nums)):
#         if i > maxReach:
#             return False
#         maxReach = max(maxReach, i + nums[i])
#         if maxReach >= len(nums) - 1:
#             return True
#     return False