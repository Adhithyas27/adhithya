class Solution:
    def permuteUnique(self, nums):
        if len(nums)==0:
            return []
        result = []
        nums.sort()
        return self.recursive(nums,0,result)
    
        
    def recursive(self, nums, start, result):
        myset = set()
        if start>=len(nums)-1:
            result.append(nums[:])
            return result
        
        for i in range(start,len(nums)):
            
            if nums[i] not in myset:
                myset.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                self.recursive(nums,start+1,result)
                nums[start], nums[i] = nums[i], nums[start]
            
        return result
print(result)
