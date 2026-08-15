class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort
        res, left, right = 0, 0, len(people) - 1

        while left <= right:
            remain = limit - people[right]
            right -= 1
            res += 1

            if left <= right and people[left] <= remain:
                left += 1
        return res

if __name__ == "__main__":
    obj = Solution()
    people = [3, 2, 2, 1]
    limit = 3
    print(obj.numRescueBoats(people, limit))