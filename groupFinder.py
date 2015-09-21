class GroupFinder(object):
    def __init__(self,rows,cols):
        self.rows=rows
        self.columns=cols
        
    def getIndex(self,i,j):
        index= (i*self.columns) +  j
        if(not(index < (self.rows*self.columns))):
           raise Exception("Wrong index")
        return index
    def getCoordinates(self,index):
        row=index/self.columns
        if(not(row<self.rows)):
           raise Exception("Wrong index")
        return (row,index%self.columns)



if __name__=='__main__':
    rows=3
    cols=4
    ind=11
    gf=GroupFinder(rows,cols)
    print(gf.getCoordinates(ind))
    a=gf.getCoordinates(ind)
    print(gf.getIndex(*a))
    print(gf.getIndex(1,1))
