class Queue:
    def __init__(self):
        self.elements = []
    
    def IsItEmpty(self):
        return self.elements == []
    
    def enqueue(self,item):
        self.elements.insert(0,item)
    
    def dequeue(self):
        self.elements.pop()
    
    def seeFront(self):
        return self.elements[len(self.elements)-1]
    
    def seeBack(self):
        return self.elements[0]
    
    def LenQueue(self):
        return len(self.elements)

if __name__ == '__main__':
    cola = Queue()
        
        
    