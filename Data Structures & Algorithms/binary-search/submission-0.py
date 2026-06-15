class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums) -1

        while lp <= rp:
            mid = lp + ((rp - lp) // 2)
        
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lp = mid + 1
            elif nums[mid] > target:
                rp = mid - 1   
        
        return -1