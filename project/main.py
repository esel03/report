import sys
from cli import read_cli
from handler import choice_report_handler
from pars_csv import ReadCSV
from output import print_table

read_csv = ReadCSV()

def main():
    param_cli = read_cli()
    report_handler = choice_report_handler(param_repo=param_cli['report'])
    if (raw_data := read_csv.pars(file_paths=param_cli['file'])) is None:
        print('File does not exit / it`s dir')
        sys.exit(1)
    temp = report_handler.process(data=raw_data)
    print(print_table(temp))
        


if __name__ == '__main__':
    main()