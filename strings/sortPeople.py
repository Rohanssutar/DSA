class solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        map_height_to_names = {}
        sorted_names = []

        for h1, n1 in zip(heights, names):
            map_height_to_names[h1] = n1

        res = sorted(map_height_to_names.items(), reverse=True)
        for n in range(len(res)):
            sorted_names.append(res[n][1])

        return sorted_names

if __name__ == "__main__":
    obj = solution()
    names = ["Mary", "Emma", "John"]
    heights = [180, 165, 170]
    print(obj.sortPeople(names, heights))