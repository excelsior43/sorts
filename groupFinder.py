__author__ = 'MonuNisa'

from itertools import combinations
from copy import deepcopy
from sys import maxsize as MAX_INT
import timeit


class GroupFinder(object):
    def __init__(self,rows,cols,theList):
        self.rows=rows
        self.columns=cols
        self.theList=theList
    def getIndex(self,i,j):
        index= i* (self.columns+1) +  (j)
        if(self.checkIndex(index)):
            return index
    def checkIndex(self,index):
        if(index >= (self.rows+1)*(self.columns+1)):
           raise Exception("Wrong index Found %d : Required <= %d  "
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
        if(self.check(row , col+1)):
            yield (row , col+1)
        if(self.check(row+1 , col+1)):
            yield (row+1 , col+1)
        if(self.check(row+1 , col)):
            yield (row+1 , col)
        if(self.check(row+1 , col-1)):
            yield (row+1 , col-1)
        if(self.check(row , col-1)):
            yield (row , col-1)
        if(self.check(row-1 , col-1)):
            yield (row-1 , col-1)
        if(self.check(row-1 , col)):
            yield (row-1 , col)
        if(self.check(row-1 , col+1)):
            yield (row-1 , col+1)

    def plotSingleGroup(self, r, c, idOfTheGroup):
        self.cloneList[self.getIndex(r,c)][1]=True
        for (ro, co) in self.getAllSides(r,c):
            if(self.cloneList[self.getIndex(ro,co)][1]==False and self.cloneList[self.getIndex(ro,co)][0]== idOfTheGroup):
                self.plotSingleGroup(ro, co, idOfTheGroup)

    def groupCounter(self, idOfGroup,lis):
        count=0;
        self.cloneList=[[ele,False] for ele in lis]
        for r in range(self.rows+1):
            for c in range(self.columns+1):
                if( self.cloneList[self.getIndex(r,c)][1]==False and
                            self.cloneList[self.getIndex(r,c)][0] == idOfGroup):
                    self.plotSingleGroup(r, c, idOfGroup)
                    count=count+1
        self.noCommunicationList=  [ind for ind in enumerate(self.cloneList) if ind[1][1]==False]
        return count

    def getAllCombinations(self,lis):
        for L in range(1, len(lis)+1):
            for subset in combinations(lis, L):
                #print subset
                if(self.theCost >= sum( theElement[1][0] for theElement in subset) ):
                    yield (subset)
                #yield (subset)

    def getCost(self,combination):
        tempList=deepcopy(self.theList)
        for e in combination:
            tempList[e[0]]=-1
        if self.groupCounter(-1,tempList)==1:
            return sum(int(i[0]) for i in combination)

    def calculateLeastCost(self):
        if(self.theList.count(-1) == (self.rows+1)*(self.columns+1)):
            return 0  # fully connected
        elif (self.theList.count(-1)==0):
            return 0  # No Communication Zone exist
        elif(self.theList.index(-1) >=0):
            numberOfCommunicationChannels=self.groupCounter(-1,self.theList)
            if( numberOfCommunicationChannels==1):
                return 0  # All Communication channels are fully connected
            else:
                self.theCost=MAX_INT
                for combination in self.getAllCombinations(self.noCommunicationList):
                    tempList=deepcopy(self.theList)
                    for e in combination:
                        tempList[e[0]]=-1
                    if self.groupCounter(-1,tempList)==1:
                        localCost=sum(int(i[1][0]) for i in combination)
                        if(self.theCost > localCost):
                            self.theCost =localCost
                return self.theCost

def minimum_possible_cost(input1):
    theList=[]
    rows=-1
    cols=0
    for rowList in input1.split("#"):
        theColList=rowList.split("@")
        rows=rows+1
        if cols==0:
            cols=len(theColList)-1
        for colList in theColList:
            theList.append(int(colList))
    if((rows+1)*(cols+1) != len(theList)):
        raise ValueError("Please enter proper values")
    gf=GroupFinder(rows,cols,theList)
    return gf.calculateLeastCost()



if __name__=='__main__':
    #theRst=minimum_possible_cost("-1@10@-1#10@-1@10#-1@10@-1")
    #theRst=minimum_possible_cost("-1@10@-1#10@-1@10#-1@10@-1")
    #theRst=minimum_possible_cost("1@10@1#10@2@10#1@10@1")
    #theRst=minimum_possible_cost("1")
    #theRst=minimum_possible_cost("-1@-1@10@-1#1@10@20@10#-1@2@10@10")
    #theRst=minimum_possible_cost("-1@1@9@10#11@10@-1@2#6@4@3@2#-1@1@1@0#1@1@1@-1")

    theRst=minimum_possible_cost('-1@10@9@12@1#15@12@-1@2@1#6@4@3@2@-1#-1@1@50@30@100#1@1@100@-1@1#-1@3@60@100@90')

    #print(timeit.timeit("minimum_possible_cost('-1@10@9@12@1#15@12@-1@2@1#6@4@3@2@-1#-1@1@50@30@100#1@1@100@-1@1#-1@3@60@100@90')", setup="from __main__ import minimum_possible_cost"))

    print(theRst);
    rows=3
    cols=3
    ind=8
    index=-1

    #theMatrix=[-1,-1,10,-1,-1,10,2,10,10,2,10,-1]
    #theMatrix=[-1,-1,10,-1,10,10,2,10,-1,2,10,10]  # 4
    #theMatrix=[-1,-1,10,-1,1,10,20,10,-1,2,10,10]  # 11
    #theMatrix=[1,2,3,-1,-1,1,2,10,10,3,1,-1,-1,5,-1,-1]  # 11
    #gf=GroupFinder(rows,cols,theMatrix)
    #a=gf.getCoordinates(ind)
    #print(gf.getIndex(*a))
    #print(gf.getIndex(rows,cols))
    #a=gf.getCoordinates(ind)
    #print(gf.getCoordinates(ind))
    #print(gf.getIndex(4,6))
    #print a
    #for x in gf.getAllSides(*a):
    #    print (x);

    #print ("Index :: %d "% (gf.getIndex(0,0)))
    #print ("Count of %d  is %d "% (index,gf.groupCounter(-1)))
    
    #theList=[[-1, True], [-1, True], [10, False], [-1, True], [10, False], [10, False], [2, False], [10, False], [-1, True], [2, False], [10, False], [10, False]]
    #print("The Least Cost :: %d"%(gf.calculateLeastCost()))
