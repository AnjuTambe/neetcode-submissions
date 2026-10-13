class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        n = len(nums)

        ans = []

        for i in range(n) : 
            if nums[i] > 0 : 
                break

            elif i > 0 and nums[i] == nums[i-1] : 
                continue

            lo , high = i+1 , n-1

            while lo < high : 

                sum = nums[i] + nums[lo] + nums[high] 

                if sum == 0 : 
                    ans.append([nums[i], nums[lo], nums[high]])
                    lo = lo + 1
                    high = high - 1
                    while lo < high and nums[lo] == nums[lo-1] : 
                        lo += 1
                    while lo < high and nums[high] == nums[high+1] : 
                        high -= 1
                elif sum < 0 :
                    lo += 1
                else:
                    high -= 1            
        return ans




 

        # result = []
        # for i in range(len(nums)) : 

        #     for j in range(i+1, len(nums)) : 

        #         for k in range(j+1, len(nums)) : 

        #             if nums[i] + nums[j] + nums[k] == 0 : 
                        
        #                 triplet = sorted([nums[i] , nums[j] , nums[k]])

        #                 if triplet not in result : 
                            
        #                     result.append(triplet)


        
        # return result


# optimized approach : 
               


        










