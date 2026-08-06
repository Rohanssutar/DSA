class myHashMap:
    def __init__(self):
        self.data = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = -1

if __name__ == "__main__":
    obj = myHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))  
    print(obj.get(3))  
    obj.put(2, 1)      
    print(obj.get(2))  
    obj.remove(2)      
    print(obj.get(2))