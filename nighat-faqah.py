def minesweeper(A):
    # code that converts the test matrix into desired output 
    # get the number of rows and columns in the matrix
    rows=len(A)
    cols=len(A[0])

    # convert the input matrix from list of strings to list of lists
    A=[list (A[i]) for i in range(rows)]

    # iterate over each element in the matrix
    for i in range(rows):
            for j in range(cols):
                
                # if the element is not a mine
                if not A[i][j]=="X": 
                    
                    # set a counter to zero
                    counter=0

                    # iterate over neighbouring elements
                    for k in range(i-1,i+2):
                        for l in range(j-1,j+2):

                            # use try-except block to handle edge cases
                            try:

                                # if neighbouring element is a mine,increment the counter
                                if not (k==-1 or l==-1) and A[k][l]=='X':
                                 counter+=1
                            except:
                                pass

                    A[i][j]=str(counter) 


    # convert the matrix back to list of strings
    A=[''.join(A[i]) for i in range(rows)]                                           
    return A

if __name__=="__main__":

    # the input matrix
    
    test = ["XOOXXXOO", 
            "OOOOXOXX", 
            "XXOXXOOO", 
            "OXOOOXXX", 
            "OOXXXXOX", 
            "XOXXXOXO", 
            "OOOXOXOX", 
            "XOXXOXOX"]

    """Desired Output is as under
    
    ["X11XXX32", 
     "3335X5XX", 
     "XX3XX554", 
     "3X556XXX", 
     "24XXXX6X"
     "X3XXX5X3", 
     "245X6X5X", 
     "X2XX4X4X"]
    """

    print(minesweeper(test))

