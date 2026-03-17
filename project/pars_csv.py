from typing import List
import csv


class ReadCSV:
    def parse(self, file_paths: list) -> List[tuple]:
        result_list = []
        for file_path in file_paths:
            with open(file_path, newline="") as csvfile:
                temp = csv.DictReader(csvfile)
                result_list.extend(temp)
        return result_list
