#find the first duplicate element
def find_first_duplicate(nums):#we can use only underscore(_) in any function name not minus(-)
    num_set = set()
    no_duplicate = -1
    for i in range(len(nums)):
        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])
    return no_duplicate
print(find_first_duplicate([1,2,3,2,4,5,4,6]))           