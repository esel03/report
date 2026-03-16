from cli import read_cli
from handler import choice_report_handler
from pars_csv import ReadCSV
from output import print_table

read_csv = ReadCSV()

def main():
    param_cli = read_cli()
    report_handler = choice_report_handler(param_repo=param_cli['report'])
    temp = report_handler.process(data=read_csv.pars(file_paths=param_cli['file']))
    print(print_table(temp))
        


if __name__ == '__main__':
    main()