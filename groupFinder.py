class GroupFinder(object):
    def __init__(self,rows,cols):
        self.rows=rows
        self.columns=cols
    def getIndex(self,i,j):
        index= i* (self.columns+1) +  (j+1)
        if(self.checkIndex(index)):
            return index
    def checkIndex(self,index):
        if(index > (self.rows+1)*(self.columns+1)):
           raise Exception("Wrong index Found %d : Required <= %d "
                           %(index , (self.rows+1)*(self.columns+1)))
        return True
    def getCoordinates(self,index):
        if(self.checkIndex(index)):
            row=(index)/(self.columns+1)
            if(row>=self.rows+1):
               raise Exception("Wrong index")
            return (row,(index)%(self.columns+1))
    def check (self,row,col):
        if(row<0 or  row > self.rows):
            return False
        if(col<0 or col > self.columns):
            return False
        return True
    def getAllSides(self,row,col):
        if(self.check(row , col+1) == True):
            yield (row , col+1)
        if(self.check(row+1 , col+1)  == True):
            yield (row+1 , col+1)
        if(self.check(row+1 , col)  == True):
            yield (row+1 , col)
        if(self.check(row+1 , col-1)  == True):
            yield (row+1 , col-1)
        if(self.check(row , col-1)  == True):
            yield (row , col-1)
        if(self.check(row-1 , col-1)  == True):
            yield (row-1 , col-1)
        if(self.check(row-1 , col)  == True):
            yield (row-1 , col)
        if(self.check(row-1 , col+1)  == True):
            yield (row-1 , col+1)

if __name__=='__main__':
    rows=4
    cols=6
    ind=8
    gf=GroupFinder(rows,cols)
    #a=gf.getCoordinates(ind)
    #print(gf.getIndex(*a))
    #print(gf.getIndex(rows,cols))
    a=gf.getCoordinates(ind)
    #print(gf.getCoordinates(ind))
    #print(gf.getIndex(4,6))
    #print a
    for x in gf.getAllSides(*a):
        print (x);
    
        
