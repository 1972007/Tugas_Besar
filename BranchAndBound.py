class BranchAndBound:
    def __init__(self,matrix):
        self.matrix = matrix
        self.matrix_reduced = matrix
        self.cost = 0
    
    def reduce_matrix_row(self):
        for i in self.matrix_reduced:
            mini = min(i)
            if(mini>0):
                self.cost+=mini
                for j in range(len(i)):
                    i[j]-=mini
        self.print_matrix(self.matrix_reduced)
    def reduce_matrix_column(self):
        for i in ((self.matrix_reduced)):
            mini = min([row for row in i])
            if(mini>0):
                self.cost+=mini
                for j in range(len(i)):
                    i[j]-=mini
        self.print_matrix(self.matrix_reduced)
        
    def print_matrix(self,matrix):
        for i in matrix:
            print(i)