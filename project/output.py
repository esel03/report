from typing import List
from tabulate import tabulate


def print_table(data: List[tuple]) -> tabulate:
    return tabulate(data, headers=["student", "median_coffee"], tablefmt="grid")
