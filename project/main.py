import sys
from cli_comand import read_cli
from handler import choice_report_handler
from pars_csv import ReadCSV
from output import print_table

read_csv = ReadCSV()

def main():
    if isinstance(param_cli := read_cli(), str):
        print(f'File {param_cli} does not exist / it`s dir')
        sys.exit(1)
    if (report_handler := choice_report_handler(param_repo=param_cli['report'])) is None:
        print('Report does not exist')
        sys.exit(1)
    raw_data = read_csv.pars(file_paths=param_cli['file'])
    processed_data = report_handler.process(data=raw_data)
    print(print_table(processed_data))
        


if __name__ == '__main__':
    main()