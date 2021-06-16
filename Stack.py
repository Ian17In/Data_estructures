class Stack:
    def __init__(self) -> list:
        self.elements = []
    
    def IsItEmpty(self):
        return self.elements == []

    def Push(self,item):
        self.elements.append(item)
    
    def Pop(self):
        return self.elements.pop()
    
    def LastElement(self):
        return self.elements[len(self.elements)-1]
    
    def Size(self):
        return len(self.elements)
    
    def See(self):
        for i in self.elements:
            print(i)
            print("^")

if __name__ == '__main__':
    
    n = Stack()

    n.Push(1)
    n.Push(21)
    n.Push(32)
    n.Push(10)
    n.Push(13)




    