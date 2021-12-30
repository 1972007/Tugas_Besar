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

def main():
    matrix = (csv_to_int_arr('Tugas_Besar/test2.csv'))
    # csv_viewer(open('Person_per_time.csv'))
    res = BranchAndBound(matrix)
    res.branch_bound()


if __name__=="__main__":
    main()