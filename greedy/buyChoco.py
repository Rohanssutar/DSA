class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        min1, min2 = float('inf'), float('inf')

        for price in prices:
            if price < min1:
                min1, min2 = price, min1
            elif price < min2:
                min2 = price

        leftover = money - min1 - min2
        if leftover >= 0:
            return leftover
        else:
            return money

if  __name__ == "__main__":
    obj = Solution()
    prices = [1, 3, 2]
    money = 5
    print(obj.buyChoco(prices, money))