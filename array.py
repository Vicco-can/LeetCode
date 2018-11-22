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
        对于相同元素时有误
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            half = target - nums[i]
            if half in nums and half != nums[i]:
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
                if nums[j] == target -nums[i]:
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

# if __name__ == "__main__":
#     # s = Solution1()
#     # print(s.twoSum2([2, 7, 11, 15], 9))

'''
26、删除数组中的重复项
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
示例 1:

给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。
'''


class Solution2:
    def removeDuplicates(self, nums):
        """
        思路，两个指针，一个用来从前往后遍历，一个快指针用于跳过重复的项，
        当等于最后一个元素时表明已经完成，基于有序数组
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        last = nums[length-1]
        i = 0
        j = 1
        if len(nums)==0:
            return 0
        while i < length-1:

            if nums[i] == last:
                return nums[:i+1]
            while j < length:

                if nums[i] != nums[j]:
                    nums[i+1] = nums[j]
                    break
                else:
                    j += 1
            i += 1

    '''
    官方题解思路：better
    双指针法
    算法
    
    数组完成排序后，我们可以放置两个指针 i 和 j，其中 i 是慢指针，而 j 是快指针。
    只要 nums[i] == nums[j]，我们就增加 j 以跳过重复项。
    
    当我们遇到 nums[j] != nums[i]时，跳过重复项的运行已经结束，
    因此我们必须把它（nums[j]）的值复制到 nums[i + 1]。
    然后递增 i，接着我们将再次重复相同的过程，直到 j 到达数组的末尾为止。
        
    '''
    def removeDuplicates1(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1


# if __name__ == "__main__":
#     s = Solution2()
#     print(s.removeDuplicates1([0,0,1,1,1,2,2,3,3,4]))


'''
27、移除元素
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
'''


class Solution3:
    def removeElement(self, nums, val):
        """
        该思路为从后往前遍历，若元素相同则删除，否则继续往前
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        j = i
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
                # return i+1
        # while i < len(nums):
        #
        #     if nums[i] == val:
        #
        #        while(j < len(nums)-1):
        #            j += 1
        #            if nums[j] != val:
        #                 nums[i], nums[j] = nums[j], nums[i]
        #                 break
        #     if j == len(nums):
        #         return i
        #     i += 1

        print(nums)
        return len(nums)

    def removeElement1(self, nums, val):
        '''官方题解思路一：双指针

        既然问题要求我们就地删除给定值的所有元素，我们就必须用 O(1) 的额外空间来处理它。
        如何解决？我们可以保留两个指针 i 和 j，其中 i 是慢指针，j 是快指针。

        算法

        当 nums[j] 与给定的值相等时，递增 j 以跳过该元素。只要 nums[j] != val，
        我们就复制 nums[j] 到 nums[i] 并同时递增两个索引。
        重复这一过程，直到 j 到达数组的末尾，该数组的新长度为 i。

        该解法与 删除排序数组中的重复项 的解法十分相似。

        '''
        i = 0  # 慢指针
        for j in range(i, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

    def removeElement2(self, nums, val):
        '''
        官方题解思路二：双指针 —— 当要删除的元素很少时
        现在考虑数组包含很少的要删除的元素的情况。
        例如，num=[1，2，3，5，4]，Val=4 num=[1，2，3，5，4]，Val=4。
        之前的算法会对前四个元素做不必要的复制操作。另一个例子是 num=[4，1，2，3，5]，Val=4
        num=[4，1，2，3，5]，Val=4。似乎没有必要将 [1，2，3，5]
        这几个元素左移一步，因为问题描述中提到元素的顺序可以更改。
        算法

        当我们遇到 nums[i] = val时，我们可以将当前元素与最后一个元素进行交换，并释放最后一个元素。
        这实际上使数组的大小减少了 1。

        请注意，被交换的最后一个元素可能是您想要移除的值。
        但是不要担心，在下一次迭代中，我们仍然会检查这个元素。
        :param nums:
        :param val:
        :return: 结果数组长度
        '''
        i = 0
        j = len(nums)
        while i < j:

            if nums[i] == val:
                nums[i] = nums[j-1]
                # nums.pop(j)
                j -= 1
            else:
                i += 1
        return j




# if __name__ == "__main__":
#     s = Solution3()
#     print(s.removeElement2([0,1,2,2,3,0,4,2], 2))

'''
35、搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
'''


class Solution4:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[0]:
                return 0
            elif target > nums[len(nums)-1]:
                return len(nums)
            else:
                for i in range(len(nums)-1):
                    if nums[i]<target and nums[i+1]>target:
                        return i+1
        '''速度更快一些
        if target <= nums[0]:
            return 0
        elif target > nums[len(nums)-1]:
            return len(nums)
        else:
            for i in range(len(nums)-1):
                if nums[i]<target and nums[i+1]>target:
                    return i+1
                elif nums[i]==target:
                    return i
                elif nums[i+1] == target:
                    return i+1
        '''

    def searchInsert1(self, nums, target):
        '''
        评论中看到的方法：二分查找
        :param self:
        :param nums:
        :param target:
        :return:
        '''
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j)//2
            if target < mid:
                j = mid - 1

            elif target > mid:
                i = mid + 1
            else:
                return mid


# if __name__ == "__main__":
#     s = Solution4()
#     print(s.searchInsert1([1,3,5,6], 2))
'''
53、最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

'''


class Solution5:
    def maxSubArray(self, nums):
        """
        从前往后遍历，当和为负数则停止，用一个变量记录之前最大的和记录，每次新的和与其比较，为其重新赋值
        :type nums: List[int]
        :rtype: int
        """
        premax = nums[0]
        sum = 0
        for item in nums:
            if sum >= 0:
                sum += item
            else:
                sum = item
            premax = max(sum, premax)
        return premax


# if __name__ == "__main__":
#     s = Solution5()
#     print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


'''
66、加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
'''


class Solution6:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """


'''88'''


'''118'''

'''119'''

'''121'''

'''122'''

'''167'''

'''169'''

'''189'''
#
# if __name__ == "__main__":
#     # s = Solution1()
#     # print(s.twoSum2([2, 7, 11, 15], 9))
#     # s = Solution2()
#     # print(s.removeDuplicates1([0,0,1,1,1,2,2,3,3,4]))
#     s = Solution3()
#     print(s.removeElement([0,1,2,2,3,0,4,2], 2))



