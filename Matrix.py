class Matrix():
    def __init__(self):
        self.elements = []
    
    def InsertRow(self,index=0,row=[]):
        self.elements.insert(index,row)
    
    def InsertColumn(self,column=[]):
        if len(self.elements) != 0:

            for j in range(len(self.elements)):

                for i in range(len(self.elements[j])):

                    if self.elements[j][i]  == self.elements[j][-1]:

                        for e in range(len(column)):
                            self.elements[j].insert(len(self.elements[j]),column[e])
        else:
            return 'The matrix is empty'
    
    def __str__(self):
        return f'This is your matrix {self.elements}' 

if __name__ == '__main__':
    matrix1 = Matrix()
    matrix1.InsertRow(0,row=[1,2,3,4])
    matrix1.InsertRow(1,row=[5,6,7,8])
    
    print(matrix1)
    
    matrix1.InsertColumn([2,3,4,5])
    print(matrix1)
    
