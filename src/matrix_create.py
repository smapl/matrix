import pandas as pd
from loguru import logger

from random import randint


def matrix_build(size: int, filename: str):
    matrix = []

    for i in range(size):
        logger.info(i)
        row = [randint(0, 9) for _ in range(size)]
        matrix.append(row)

        if len(matrix) >= 100:
            matrix_frame = pd.DataFrame(matrix)
            matrix_frame.to_csv(filename, mode="a", index=False, header=False, sep="\t")
            matrix = []
            log_message = (
                f"column = {i}\nlen matrix after writing to file = {len(matrix)}"
            )
            logger.info(log_message)

    return matrix


if __name__ == "__main__":
    filename = "matrix.csv"
    matrix = matrix_build(530, filename)

    if len(matrix) != 0:

        matrix_frame = pd.DataFrame(matrix)
        matrix_frame.to_csv(filename, mode="a", index=False, header=False, sep="\t")
