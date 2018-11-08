'''array中前200题，easy-medium-hard'''
'''
1、给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

class Solution1:

    def twoSum(self, nums, target):
        """
        自己写的方法采用了python自带的list.index()方法
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            half = target - nums[i]
            if half in nums and half != i:
                a, b = i, nums.index(half)
                return [a, b]
        return None


    def twoSum1(self, nums, target):
        '''
        官方题解1暴力法
        :param nums:
        :param target:
        :return:
        '''
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if target -nums[i] == nums[j]:
                    return [i, j]
        return None


    def twoSum2(self, nums, target):
        '''
        官方题解2hashmap,以空间换时间
        :param nums:
        :param target:
        :return:
        '''
        dic = {}
        for i in range(len(nums)):
            if target-nums[i] in dic.keys():
                return [dic.get(target-nums[i]), i]

            dic[nums[i]] = i
        return None

'''
26
'''

'''
27
'''

'''
35
'''

'''
53
'''

'''
66
'''

'''88'''


'''118'''

'''119'''

'''121'''

'''122'''

'''167'''

'''169'''

'''189'''

if __name__ == "__main__":
    s = Solution1()
    print(s.twoSum2([2, 7, 11, 15], 9))


