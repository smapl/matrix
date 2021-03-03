import pandas as pd

from random import randint


def random_row(size):
    random_list = []
    for _ in range(size):
        random_list.append(randint(-100, 100))

    return random_list


# TODO: make with multiprocessing or async
def matrix_build(size=5):
    matrix = []

    for _ in range(size):

        row = random_row(size)
        matrix.append(row)

    return matrix


if __name__ == "__main__":
    matrix = matrix_build()
    matrix_frame = pd.DataFrame(matrix)
    matrix_frame.to_csv("matrix.csv", index=False, header=False)