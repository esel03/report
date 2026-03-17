import os
import pytest
import pandas as pd
from report.project.pars_csv import ReadCSV
from report.project.gen_report import CoffieMedianReportHandler


@pytest.fixture
def csv_data():
    data_to_csv = [
        ["Иван", "2026-01-01", "98", "4.5", "12", "норм", "Математика"],
        ["Иван", "2026-01-01", "75", "5.5", "11", "норм", "Математика"],
        ["Иван", "2026-01-01", "100", "6.5", "10", "норм", "Математика"],
        ["Иван", "2026-01-01", "24", "7.5", "9", "норм", "Математика"],
        ["Алексей", "2026-01-01", "105", "4.5", "12", "норм", "Математика"],
        ["Алексей", "2026-01-01", "24", "5.5", "11", "норм", "Математика"],
        ["Алексей", "2026-01-01", "98", "6.5", "10", "норм", "Математика"],
        ["Алексей", "2026-01-01", "75", "7.5", "9", "норм", "Математика"],
        ["Алексей", "2026-01-01", "100", "8.5", "8", "норм", "Математика"],
    ]
    return data_to_csv


@pytest.fixture
def data_verify():
    data_verify = [
        ("Алексей", 98.0),
        ("Иван", 86.5),
    ]
    return data_verify


@pytest.fixture
def create_csv_test_file(csv_data):
    with open("test_csv_file.csv", "w") as f:
        df = pd.DataFrame(
            csv_data,
            columns=[
                "student",
                "date",
                "coffee_spent",
                "sleep_hours",
                "study_hours",
                "mood",
                "exam",
            ],
        )
        df.to_csv(f, index=False, encoding="utf-8")
    yield "test_csv_file.csv"
    os.remove("test_csv_file.csv")


def test_function_parse_and_report(create_csv_test_file, data_verify):
    raw_data = ReadCSV().parse([create_csv_test_file])
    processed_data = CoffieMedianReportHandler().process(raw_data)

    assert processed_data == data_verify
