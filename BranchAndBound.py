class BranchAndBound:
    def __init__(self,matrix):
        self.matrix = matrix
        self.matrix_reduced = matrix
        self.cost = 0
    
    def reduce_matrix_row(self,matrix):
        for i in matrix:
            mini = min(i)
            if(mini>0):
                self.cost+=mini
                for j in range(len(i)):
                    i[j]-=mini
        self.print_matrix(matrix)
    def reduce_matrix_column(self,matrix):
        for i in matrix:
            mini = min([row for row in i])
            if(mini>0):
                self.cost+=mini
                for j in range(len(i)):
                    i[j]-=mini
        self.print_matrix(matrix)
        print(self.cost)
    
    def branch(self):
        pass
    
    def branch_rec(self,matrix,src,des):
        for i in range(len(matrix)):
            mini = min(matrix[i])
            if(mini>0):
                self.cost+=mini
                for j in range(i):
                    if(i!=src and j!=des):
                        self.matrix_reduced[i][j]

    
    def print_matrix(self,matrix):
        for i in matrix:
            print(i)
