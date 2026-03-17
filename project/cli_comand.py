import argparse
from pathlib import Path


def read_cli() -> dict:
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
        epilog="Text at the bottom of help",
        allow_abbrev=False,
    )
    parser.add_argument("--files", nargs="+", help="List file for report")
    parser.add_argument("--report")
    args = parser.parse_args()

    for file_path in args.files:
        path = Path(file_path)
        if not (path.exists() and path.is_file()):
            raise FileNotFoundError
    return {"file": args.files, "report": args.report}
