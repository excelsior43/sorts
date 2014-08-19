class quickSort(object):
       def printThis(self,a,left,right):
              print("%r     (%d,%d) Count : %d"%(a,left,right,self.count));
       def swap(self,a,i,j):
              a[i],a[j]=a[j],a[i]
              self.count=self.count+1
       def getPivote(self,a,left,right):
              pivote=a[left]
              i=left+1
              j=right
              while(i<=j):
                     while a[j]>pivote:
                            j=j-1
                     while a[i]<pivote and i<=j:
                            i=i+1
                     if i<j :
                           self.swap(a,i,j)
                           i=i+1
                           j=j-1
              self.swap(a,left,j)
              return j
       def getPivote2(self,a,left,right):
              #m=(left+right+1)/2
              #self.swap(a,left,m)
              pivot=a[left]
              i=left+1
              j=right
              while i<=j:
                     while a[j]>pivot:
                            j=j-1
                     while i<=j and a[i]<pivot:
                            i=i+1
                     if i<j :
                            self.swap(a,i,j)
                            i=i+1
                            j=j-1
              self.swap(a,left,j)
              return j
       
       def quickSort(self,a,left,right):
              if(left<right):
                     pivote=self.getPivote(a,left,right)
                     self.quickSort(a,left,pivote-1);
                     self.quickSort(a,pivote+1,right);
              self.printThis(a,left,right);
                     
       def quickSort2(self,a,left,right):
              while (left<right):
                     pivote=self.getPivote2(a,left,right)
                     if(pivote-right < left-pivote):
                            self.quickSort2(a,left,pivote-1)
                            left=pivote+1
                     else:
                            self.quickSort2(a,pivote+1,right)
                            right=pivote-1
              self.printThis(a,left,right);
       def __init__(self):
              self.count=0
if __name__=='__main__':
       qs=quickSort()
       a=[5,0,2,3,7,1,4,8,6]
       #print(qs.getPivote2(a,0,len(a)-1));
       print("----------------------------------")
       #a=[0,1,2,3,4,5,6,7,8]
       qs.quickSort2(a,0,len(a)-1)
       print("----------------------------------")
       #a=[0,1,2,3,4,5,6,7,8]
       a=[5,0,2,3,7,1,4,8,6]
       qs=quickSort()
       qs.quickSort(a,0,len(a)-1)
       print("----------------------------------")
                     
