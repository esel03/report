from typing import List
from tabulate import tabulate

def print_table(data: List[tuple]):
    return tabulate(data, headers=["student", "median_coffe"], tablefmt='grid')