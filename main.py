# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def recursiveSearch(start, last, nums, target) -> int:
    median = start + int((last - start)/2)
    # print(median)
    if nums[median] == target:
        return median
    if start == median:
        if nums[last] == target:
            return last
        else:
            return -1
    if nums[median] > nums[last]:
        if target < nums[median]:
            if target == nums[last]:
                return last
            else:
                if target < nums[last]:
                    return recursiveSearch(median + 1, last, nums, target)
                else:
                    return recursiveSearch(start, median - 1, nums, target)
        else:
            return recursiveSearch(median + 1, last, nums, target)
    else:
        if target < nums[median]:
            return recursiveSearch(start, median - 1, nums, target)
        else:
            if target == nums[last]:
                return last
            else:
                if target < nums[last]:
                    return recursiveSearch(median + 1, last, nums, target)
                else:
                    return recursiveSearch(start, median - 1, nums, target)


class Solution:
    def search(self, nums, target) -> int:
        if len(nums) < 4:
            for i in range(0, len(nums)):
                if nums[i] == target:
                    return i
            return -1
        result = recursiveSearch(0, len(nums) - 1, nums, target)
        return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.search([5, 1, 2, 3, 4], 1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
