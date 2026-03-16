import csv
from pathlib import Path


class ReadCSV:
    def pars(self, file_paths: list):
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


'''
class CsvReader:
    def __init__(self):
        self.csv_dict = dict()
    
    def check_csv_file(self, file_path: str):
        path = Path(file_path)
        return path.exists() and path.is_file()
        
    def read_csv(self, file_path: str):
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not row['student'] in self.csv_dict:
                    self.csv_dict[f'{row['student']}'] = {
                        f'{row['exam']}': 
                            [{'date': row['date'],
                            'coffee_spent': row['coffee_spent'],
                            'sleep_hours': row['sleep_hours'],
                            'study_hours': row['study_hours'],
                            'mood': row['mood']
                            }]
                        }
                elif not row['exam'] in self.csv_dict[row['student']]:
                    self.csv_dict[f'{row['student']}'][f'{row['exam']}'] = [
                            {'date': row['date'],
                            'coffee_spent': row['coffee_spent'],
                            'sleep_hours': row['sleep_hours'],
                            'study_hours': row['study_hours'],
                            'mood': row['mood']
                            }]
                else:
                    self.csv_dict[f'{row['student']}'][f'{row['exam']}'].append({
                            'date': row['date'],
                            'coffee_spent': row['coffee_spent'],
                            'sleep_hours': row['sleep_hours'],
                            'study_hours': row['study_hours'],
                            'mood': row['mood']
                            })
            
        return self.csv_dict
'''
