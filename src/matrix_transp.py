import pandas as pd


def transp_matrix(matrix):
    transp = []

    for i in range(len(matrix)):

        column = matrix[i].to_list()
        transp.append(column)

    return transp


if __name__ == "__main__":
    matrix = pd.read_csv("matrix.csv", delimiter="\t", header=None, index_col=None)
    transp = transp_matrix(matrix)
    transp_frame = pd.DataFrame(transp)
    transp_frame.to_csv("matrix_transp.csv", sep="\t", index=False, header=False)
