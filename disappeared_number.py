def missing_number(nums):
    print(list((set(range(1, len(nums) + 1)) - set(nums))))


nums = [1, 4, 6, 9, 4, 8, 3, 9]
missing_number(nums)
