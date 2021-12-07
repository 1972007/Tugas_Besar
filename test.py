import csv

from BranchAndBound import BranchAndBound

def csv_to_int_arr(path):
    matrix = []
    with open(path) as file:
        reader = csv.reader(file)
        next(reader,None)
        for row in reader:
            arr=[]
            for i in row:
                arr.append(int(i)) 
            matrix.append(arr)
    return matrix

matrix = (csv_to_int_arr('Person_per_cost.csv'))
# csv_viewer(open('Person_per_time.csv'))
res = BranchAndBound(matrix)
res.reduce_matrix_row()
print()
res.reduce_matrix_column()


