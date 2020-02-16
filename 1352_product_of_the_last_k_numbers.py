from functools import reduce
from typing import List


class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.length = 0
        self.lastProduct = 0
        self.lastProductIndexes = []
        self.lastBeginIndex = 0
        self.lastEndIndex = 0

    def getNumsProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        elif len(nums) == 1:
            return nums[0]
        else:
            return reduce(lambda x, y: x * y, nums)

    def calculate(self, currentBeginIndex: int, currentEndIndex: int) -> int:
        lastLength = self.lastEndIndex - self.lastBeginIndex + 1
        currentLength = currentEndIndex - currentBeginIndex + 1
        if self.lastProduct == 0:
            value = self.getNumsProduct(self.nums[currentBeginIndex:currentEndIndex + 1])
        else:
            if currentBeginIndex > self.lastEndIndex:
                # 无公共部分
                commonPartLength = 0
                extraStep = currentLength
                mode = 0
            elif self.lastBeginIndex < currentBeginIndex <= self.lastEndIndex:
                # 部分去除、部分添加
                commonPartBeginIndex = currentBeginIndex
                commonPartEndIndex = self.lastEndIndex
                commonPartLength = commonPartEndIndex - commonPartBeginIndex + 1
                extraStep = currentLength + lastLength - 2 * commonPartLength
                mode = 1
            else:
                # 全部添加
                commonPartBeginIndex = self.lastBeginIndex
                commonPartEndIndex = self.lastEndIndex
                commonPartLength = lastLength
                extraStep = currentLength - commonPartLength
                mode = 2
            if extraStep >= currentLength:
                value = self.getNumsProduct(self.nums[currentBeginIndex:currentEndIndex + 1])
            else:
                if mode == 1:
                    value = self.lastProduct * self.getNumsProduct(
                        self.nums[commonPartEndIndex + 1:currentEndIndex + 1]) / self.getNumsProduct(
                        self.nums[self.lastBeginIndex:commonPartBeginIndex])
                elif mode == 2:
                    value = self.lastProduct * self.getNumsProduct(
                        self.nums[commonPartEndIndex + 1:currentEndIndex + 1]
                    )
                    if currentBeginIndex < commonPartBeginIndex:
                        value *= self.getNumsProduct(self.nums[currentBeginIndex:commonPartBeginIndex])

        return int(value)

    def add(self, num: int) -> None:
        self.nums.append(num)
        self.length += 1

    def getProduct(self, k: int) -> int:
        currentBeginIndex = self.length - k
        currentEndIndex = self.length - 1
        product = self.calculate(currentBeginIndex, currentEndIndex)
        self.lastBeginIndex = currentBeginIndex
        self.lastEndIndex = currentEndIndex
        self.lastProduct = product
        return product


def test(lista, listb):
    obj = ProductOfNumbers()
    results = []
    for index, item in enumerate(lista):
        value = None
        if item == 'add':
            obj.add(listb[index][0])
        elif item == 'getProduct':
            value = obj.getProduct(listb[index][0])
        results.append(value)

    return results


if __name__ == '__main__':
    assert test(
        ["ProductOfNumbers", "add", "getProduct", "getProduct", "add", "add", "getProduct", "add", "getProduct", "add",
         "getProduct", "add", "getProduct", "getProduct", "add", "getProduct"],
        [[], [7], [1], [1], [4], [5], [3], [4], [4], [3], [4], [8], [1], [6], [2], [3]]
    ) == [None, None, 7, 7, None, None, 140, None, 560, None, 240, None, 8, 13440, None, 48]
    assert test(
        ["ProductOfNumbers", "add", "getProduct", "getProduct", "add", "add", "getProduct", "add", "getProduct", "add",
         "getProduct", "add", "getProduct", "getProduct", "add", "getProduct"]
        , [[], [7], [1], [1], [4], [5], [3], [4], [4], [3], [4], [8], [1], [6], [2], [3]]
    ) == [None, None, 7, 7, None, None, 140, None, 560, None, 240, None, 8, 13440, None, 48]
    assert test(
        ["ProductOfNumbers", "add", "add", "add", "getProduct", "add", "add", "add", "getProduct", "getProduct",
         "getProduct", "add", "add"]
        , [[], [0], [0], [9], [3], [8], [3], [8], [5], [4], [6], [8], [8]]
    ) == [None, None, None, None, 0, None, None, None, 0, 1728, 0, None, None]
