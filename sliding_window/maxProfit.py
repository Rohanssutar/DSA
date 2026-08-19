class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        left = 0
        max_profit = 0

        for right in range(1, n):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
        return max_profit

if __name__ == "__main__":
    obj = Solution()
    prices = [10,1,5,6,7,1]
    print(obj.maxProfit(prices))