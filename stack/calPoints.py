class solution:
    def calPoints(self, ops: list[str]) -> int:
        records = []

        for i in ops:
            if i == "+":
                records.append(records[-1] + records[-2])
            elif i == "D":
                records.append(2 * records[-1])
            elif i == "C":
                records.pop()
            else:
                records.append(int(i))

        return sum(records)

if __name__ == "__main__":
    obj = solution()
    ops = ["1","2","+","C","5","D"] 
    print(obj.calPoints(ops))