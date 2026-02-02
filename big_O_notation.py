# num = [1, 2, 3]
# for i in range(len(num)):
#     print("three iteration")



# for i in range(3):
#     print("three iteration")num = [1, 2, 3]
# for i in range(len(num)):
#     print("three iteration")



# for i in range(3):
#     print("three iteration")

# numbers = [1, 2, 1, 3, 4]

# for i in range(len(numbers) - 2):
#     a = numbers[i]
#     b = numbers[i + 1]
#     c = numbers[i + 2]
#     print(a, b, c)

# def solution(numbers):
#     result = []

#     for i in range(len(numbers)-2):
#         a = numbers[i]
#         b = numbers[i+1]
#         c = numbers[i+2]

#         if a > b < c:
#             result.append(1)
#         else:
#             result.append(0)
#     return result
# print(solution([2, 1, 4, 2, 6]))



def retate(nums, k):
    for i in range(k):
        nums[:] = nums[-1:] + nums[:-1]

nums = [1, 2, 3, 4, 5, 6]
k = 3

retate(nums, k)

























