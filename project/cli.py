import argparse


def read_cli():
    parser = argparse.ArgumentParser(
                prog='ProgramName',
                description='What the program does',
                epilog='Text at the bottom of help')
    parser.add_argument('--file', nargs='+', help='List file for report')
    parser.add_argument("--report")
    args = parser.parse_args()
    
    return {'file': args.file, 
            'report': args.report}

