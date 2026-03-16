import argparse
from pathlib import Path


def read_cli() -> dict | str:
    parser = argparse.ArgumentParser(
                prog='ProgramName',
                description='What the program does',
                epilog='Text at the bottom of help')
    parser.add_argument('--file', nargs='+', help='List file for report')
    parser.add_argument("--report")
    args = parser.parse_args()

    for file_path in args.file:
        path = Path(file_path)
        if not (path.exists() and path.is_file()):
            return file_path
    return {'file': args.file, 
            'report': args.report}

