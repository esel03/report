from typing import List
import csv
from pathlib import Path


class ReadCSV:
    def pars(self, file_paths: list) -> List[tuple]:
        result_list = []
        for file_path in file_paths:
            path = Path(file_path)
            if not (path.exists() and path.is_file()):
                return None

            with open(file_path, newline='') as csvfile:
                result = csv.DictReader(csvfile)
                for row in result:
                    result_list.append(row)
        return result_list

