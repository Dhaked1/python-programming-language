# find in array is there any duplicate element is present or not
def test_duplicate(array_nums):
    nums_set = set(array_nums)
    l = len(array_nums)-len(nums_set)
    print("how many duplicate element are presnt = ",l)
    return len(array_nums) != len(nums_set)
print(test_duplicate([1,2,3,4,5,6]))
print(test_duplicate([1,2,3,2,4,2,5,6,4]))
print(test_duplicate([3,2,3,1,4,5,2]))