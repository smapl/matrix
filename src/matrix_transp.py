import pandas as pd
from loguru import logger


def divide_to_batches(data: list, count):
    batches = []
    for n in range(0, len(data), count):
        batches.append(data[n : n + count])

    return batches


def transp_matrix(matrix):
    transp = []

    for col in matrix:
        logger.info(col)
        column = matrix[col].to_list()
        transp.append(column)

    return transp


if __name__ == "__main__":
    filename_source = "matrix.csv"
    filename_transp = "matrix_transp.csv"

    step = 100

    size = pd.read_csv(
        filename_source, delimiter="\t", header=None, index_col=None, usecols=[0]
    ).size
    cols = [_ for _ in range(size)]

    batches = divide_to_batches(cols, step)
    for batch in batches:
        matrix = pd.read_csv(
            filename_source, delimiter="\t", header=None, index_col=None, usecols=batch
        )

        transp = transp_matrix(matrix)
        transp_frame = pd.DataFrame(transp)
        transp_frame.to_csv(
            filename_transp, sep="\t", mode="a", index=False, header=False
        )
