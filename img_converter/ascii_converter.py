import numpy as np
from typing import List
ASCII_TABLE_DETAILED = (
    " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
)


class AsciiConverter:

    def convert(self, array_grey:np.array) -> List[List[str]]:
        new_matrix = []
        for row in array_grey:
            new_row = []
            for index, column in enumerate(row):
                new_row.append(self._get_ascii_value(column))
            new_matrix.append(new_row)

        return new_matrix


    @classmethod
    def _get_ascii_value(cls, grey_value:int) -> str:
        if grey_value == 0:
            return ASCII_TABLE_DETAILED[0]

        position = int( grey_value / len(ASCII_TABLE_DETAILED))
        return ASCII_TABLE_DETAILED[position]
    


    @classmethod
    def print_ascii(cls,matrix_parsed) -> None:
        for row in matrix_parsed:
            print("".join(row))
