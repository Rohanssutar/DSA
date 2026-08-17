class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        rich = 0

        for customer in accounts:
            rich = max(rich, sum(customer))
        return rich

if __name__ == "__main__":
    obj = Solution()
    accounts = [
        [1,2,3],
        [2,3,4]
    ]
    print(obj.maximumWealth(accounts)) 

