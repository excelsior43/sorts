# Sorts a Python list in ascending order using the merge sort algorithm.
# Sorts a virtual subsequence in ascending order using merge sort.
def recMergeSort( theSeq, first, last, tmpArray ):
    # The elements that comprise the virtual subsequence are indicated
    # by the range [first...last]. tmpArray is temporary storage used in
    # the merging phase of the merge sort algorithm.
    # Check the base case: the virtual sequence contains a single item.
    if first == last :
        return;
    else :
         # Compute the mid point.
         mid = (first + last) // 2
    # Split the sequence and perform the recursive step.
    recMergeSort( theSeq, first, mid, tmpArray )
    recMergeSort( theSeq, mid+1, last, tmpArray )

    mergeVirtualSeq(theSeq, first, mid+1, last+1, tmpArray )

 # Merge the two ordered subsequences.
def mergeVirtualSeq( theSeq, left, right, end, tmpArray ):
    # Initialize two subsequence index variables.
    a = left
    b = right
    # Initialize an index variable for the resulting merged array.
    m = 0
    # Merge the two sequences together until one is empty.
    while a < right and b < end :
        if theSeq[a] < theSeq[b] :
            tmpArray[m] = theSeq[a]
            a += 1
        else :
            tmpArray[m] = theSeq[b]
            b += 1
        m += 1
    # If the left subsequence contains more items append them to tmpArray.
    while a < right :
         tmpArray[m] = theSeq[a]
         a += 1
         m += 1
    # Or if right subsequence contains more, append them to tmpArray.
    while b < end :
         tmpArray[m] = theSeq[b]
         b += 1
         m += 1
# Copy the sorted subsequence back into the original sequence structure.
    for i in range( end - left ) :
        theSeq[i+left] = tmpArray[i]
    print ("%r  -- %r " % (theSeq,tmpArray))

if __name__=="__main__":
    a=[9,8,7,6,5,4,3,2,1,0]
    b=a[::]
    recMergeSort(a,0,len(a)-1, b )
    print (b)
