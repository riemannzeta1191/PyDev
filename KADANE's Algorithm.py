def maxsubArray(nums):
    max_curr = max_global =0
    for item in nums:
        max_curr = max(0, (max_curr + item))        #maximum sum of a subarray problem
        max_global = max(max_global, max_curr)
    return max_global



k  = maxsubArray([1,4,7,-3,-2,6,0,-9,8])
print k

