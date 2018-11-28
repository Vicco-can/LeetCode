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
        length = len(digits)
        i = 1
        while i <= length:
            print(length, i)
            digits[length-i] += 1
            if digits[length-i] < 10:
                return digits
            else:
                digits[length - i] = 0
                if length-i == 0:
                    digits.insert(0, 1)
                    return digits
                else:
                    i += 1

        return digits


# if __name__ == "__main__":
#     s = Solution6()
#     print(s.plusOne([9,9,9]))


'''88、合并两个有序数组
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
'''


class Solution7:
    def merge(self, nums1, m, nums2, n):
        """归并排序中的思路
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        res = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while i < m:
            res.append(nums1[i])
            i += 1
        while j < n:
            res.append(nums2[j])
            j += 1
        nums1 = res
        return nums1


    def merge1(self, nums1, m, nums2, n):
        """归并排序中的思路, 合并到一个数组中，
        因为数组是有序的，假设升序，从后往前遍历比较，将最大的数组放置到nums1的最后
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index = n + m

        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[index-1] = nums2[n-1]
                n = n - 1
            else:
                nums1[index-1] = nums1[m-1]
                m = m - 1
            index -= 1
        while m > 0:
            nums1[index-1] = nums1[m-1]
            m -= 1
            index -= 1
        while n > 0:
            nums1[index-1] = nums2[n-1]
            n -= 1
            index -= 1
        return nums1

#
# if __name__ == "__main__":
#     s = Solution7()
#     print(s.merge1([1,2,3,0,0,0],3,[2,5,6],3))


'''118、杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution8:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []

        for i in range(numRows):
            line = []
            if i == 0:
                line.append(1)
            else:
                line.append(1)

                for j in range(1, i):
                    line.append(res[i-1][j-1]+res[i-1][j])
                line.append(1)
            res.append(line)
        return res


# if __name__ == "__main__":
#     s = Solution8()
#     print(s.generate(5))

'''119、杨辉三角 II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]

进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？
'''


class Solution9:
    def getRow(self, rowIndex):
        """思路：1、用生成杨辉三角的方法直接返回某一行，但是空间复杂度高，2、递归方法，用时间复杂度换空间复杂度
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            pre_Line = self.getRow(rowIndex-1)
            i = 0
            res = []
            res.append(1)
            for i in range(1, rowIndex):
                res.append(pre_Line[i-1]+pre_Line[i])
            res.append(1)

            return res


# if __name__ == "__main__":
#     s = Solution9()
#     print(s.getRow(2))


'''121、买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

'''


class Solution10:
    def maxProfit(self, prices):
        """思路：从前往后遍历，寻找两元素间最大差值，且有方向之分,该方法可求出解，但是时间复杂度较高
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        max_diff = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i]
                max_diff = max(max_diff, diff)

        return max_diff

    def maxProfit2(self, prices):
        """思路：从前往后遍历，或者从后往前遍历，两个值分别用于记录差值最大值和当前最小元素值
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        max_diff = 0
        min_item = prices[0]
        for i in range(len(prices)):
            min_item = min(min_item, prices[i])
            max_diff = max(max_diff, prices[i] - min_item)

        return max_diff


# if __name__ == "__main__":
#     s = Solution10()
#     print(s.maxProfit2([7,1,5,3,6,4]))
'''122、买卖股票的最佳时机 II
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
'''


class Solution11:
    def maxProfit(self, prices):
        """思路，动态规划，递归，最大的收益等于最后一段的大的收益加上之前最大的收益？？
        :type prices: List[int]
        :rtype: int
        """
        max_p = 0
        for i in range(len(prices)-1):
            for j in range(1, len(prices)):
                max_p = max(prices[j] - prices[i]+Solution10.maxProfit2(self, prices[(j+1):]), max_p)
        return max_p

if __name__ == "__main__":
    s = Solution11()
    print(s.maxProfit([1,2,3,4,5]))

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



