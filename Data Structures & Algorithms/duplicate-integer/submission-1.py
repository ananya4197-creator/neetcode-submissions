class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums)
        a = len(my_set)
        b = len(nums)

        if a != b:
            return True
        
        else:
            return False
