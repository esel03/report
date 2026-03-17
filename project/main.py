import sys
from cli_comand import read_cli
from handler import choice_report_handler
from pars_csv import ReadCSV
from output import print_table

read_csv = ReadCSV()

def main():
    try:
        param_cli = read_cli()
    except FileNotFoundError:
        print('File does not exist')
        sys.exit(1)
    handler_class = choice_report_handler(param_repo=param_cli['report'])
    if handler_class is None:
        print('Report does not exist')
        sys.exit(1)
    raw_data = read_csv.parse(file_paths=param_cli['file'])
    processed_data = handler_class().process(data=raw_data)
    print(print_table(processed_data))
        


if __name__ == '__main__':
    main()