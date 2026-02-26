"""
Q1. Set Mismatch
Easy
Topics
premium lock icon
Companies
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
"""

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        u = []
        d = []
        for item in nums:
            if item not in u:
                u.append(item)
            else:
                if item not in d:
                    d.append(item)
        for i in range(1, len(nums) + 1):
            if i not in u:
                return [d[0], i]
            

    def findErrorNums1(self, nums: List[int]) -> List[int]:
            n = len(nums)
            # print(n)
            sum_n = n * (n + 1) // 2
            # print(sum_n)
            auctal_sum = sum(nums)
            # print(auctal_sum)
            unique_sum = sum(set(nums))
            # print(unique_sum)
            return [auctal_sum - unique_sum, sum_n - unique_sum]


# print(Solution().findErrorNums([1,2,2,4]))
# print(Solution().findErrorNums([1,1]))
# print(Solution().findErrorNums([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,17,19,20,21,22,23,24,25,26,27,28,29,30,]))


print(Solution().findErrorNums1([1,2,2,4]))
print(Solution().findErrorNums1([1,1]))
print(Solution().findErrorNums1([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,17,19,20,21,22,23,24,25,26,27,28,29,30,]))

