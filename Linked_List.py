class Node():
    def __init__(self,element,next=None):
        self.element = element
        self.next = next
    
    def __str__(self):
        return self.element
    
    def DefNext(self,NewNext):
        self.next = NewNext

    def ChangeElement(self,NewElement):
        self.element = NewElement

class Linked_list():
    def __init__(self,head=None):
        self.Nodes = []
        self.MapEstate = False

        self.head = head
    
    def MapList(self):
        while self.head != None:
            self.Nodes.append(self.head.element)
            self.head = self.head.next
        self.Nodes.append(None)
        self.MapEstate = True
    
    def __str__(self):
        self.ReturnString = ""
        for i in self.Nodes:
            if len(self.ReturnString) == 0:
                self.ReturnString = f'{str(i)}'
            else:
                self.ReturnString = self.ReturnString+ f' -> {str(i)}'
        
        return f'[{self.ReturnString}]'
    
    def ChangeHead(self,NewHead):
        NewHead.next = self.head
        self.head = NewHead
    
    def addELement(self,Node,index=0):

        if self.MapEstate == True:

            if index == 0 or index == None:
                self.Nodes.insert(0,Node.element)
                Node.next = self.Nodes[index+1]
            else:
                self.Nodes.insert(index,Node.element)
                Node.next = self.Nodes[index+1]
        else:
            return 'Map the list before, please'




        

        

        
if __name__ == '__main__':

    variable1 = 'John'
    Node1 = Node(variable1)
    Node2 = Node('2')
    Node1.DefNext(Node2)
    Node3 = Node(2)

    l=Linked_list(Node1)
    l.MapList()
    l.addELement(Node3,index=1)
    print(l)

    NewNode1 = None
    