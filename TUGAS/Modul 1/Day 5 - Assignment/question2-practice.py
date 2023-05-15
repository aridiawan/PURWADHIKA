'''
## Question-2

You are given a list `nums`, write a `find()` function to return the index of two items whose sum equals the `target`. 
Each input has one solution, and you cannot use the same item twice.

nums = [2, 7, 11, 15] 
target = 9
find(nums, target)

output:
[0, 1]
'''
# function to return index
def find(nums,target):
    '''ini adalah fungsi find

    Args:
        nums (list) : list nnumber to calculate
        target (int) : calculated result from members of nums list

    Return:
        index (list) : index of two items whose equals the 'target'
    '''
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            val = nums[i] + nums[j]
            if target == val:
                index = [i,j]
    return index

if __name__ == "__main__":
    nums = [2, 7, 11, 15] 
    target = 9

    output = find(nums,target)
    print(output)