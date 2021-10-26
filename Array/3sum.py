class Solution:
    
    @staticmethod
    def threeSum(nums):
        results = []
        
        if len(nums) < 3:
            return results

        nums.sort()

        lo = 0
        hi = len(nums) - 1
        aux = 1

        while lo < hi - 1:
            while aux < hi:
                s = nums[lo] + nums[aux] + nums[hi]
                if (s) < 0: 
                    aux += 1
                    while aux > 0 and aux < hi and nums[aux] == nums[aux-1]:
                        aux += 1
                elif (s) > 0:
                    hi -= 1
                    while hi > 2 and hi > 0 and nums[hi] == nums[hi+1]:
                        hi -= 1
                else:
                    results.append([nums[lo], nums[aux], nums[hi]])
                    aux += 1
                    while aux > 0 and aux < hi and nums[aux] == nums[aux-1]:
                        aux += 1
            lo += 1
            while lo > 0 and lo < len(nums) - 1 and nums[lo] == nums[lo-1]:
                lo += 1
            aux = lo + 1
            hi = len(nums) - 1
        
        return results

sol = Solution()

test = [-1,-2,-3,4,1,3,0,3,-2,1,-2,2,-1,1,-5,4,-3]
test2 = [-25, -10, -7, -3, 2, 4, 8, 10]
"[-25, -10, -7, -3, 2, 4, 8, 10]"
print(sol.threeSum(test))