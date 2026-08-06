class myHashSet:
    def __init__(self):
        self.value= []

    def add(self, key: int) -> None:
        if key not in self.value:
            self.value.append(key)

    def remove(self, key: int) -> None:
        if key in self.value:
            self.value.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.value

if __name__ == "__main__":
    obj = myHashSet()
    obj.add(1)
    obj.add(2)
    obj.add(3)
    obj.remove(2)
    