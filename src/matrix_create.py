import pandas as pd
from loguru import logger

from random import randint


def load_data(matrix, filename):

    matrix_frame = pd.DataFrame(matrix)
    matrix_frame.to_csv(filename, mode="a", index=False, header=False, sep="\t")

    return


def matrix_build(size: int, step: int, filename: str):
    matrix = []

    for i in range(size):
        logger.info(i)
        row = [randint(0, 9) for _ in range(size)]
        matrix.append(row)

        if len(matrix) >= step:
            load_data(matrix, filename)
            matrix = []

    return matrix


if __name__ == "__main__":
    filename = "matrix.csv"
    size = 10000
    step = 100

    matrix = matrix_build(size, step, filename)

    if len(matrix) != 0:
        load_data(matrix, filename)
