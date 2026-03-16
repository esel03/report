# test_readcsv.py
import os
import tempfile
import pytest
from report.tests.create_test_data import generate_data_report
from report.project.gen_report import CoffieMedianReportHandler

NUM_STUDENTS = 10
NUM_DAYS = 1


@pytest.fixture
def create_report():
    return CoffieMedianReportHandler()

def test_parse_returns_expected_data(create_report):
    data_dict, data_shuffle, data_tuple = generate_data_report(num_students=NUM_STUDENTS, days=NUM_DAYS)

    data_verify_notshuffle = create_report.process(data=data_dict)

    data_verify_shuffle = create_report.process(data=data_shuffle)
    assert data_tuple == data_verify_notshuffle, "Сортировка (без перемешивания) не успешна"
    assert data_tuple == data_verify_shuffle, "Сортировка (с перемешиванием) не успешна"



    # Сравниваем каждую запись
    #for i, (expected, actual) in enumerate(zip(expected_data, actual_data)):
    #    assert actual == expected, f"Расхождение в строке {i}: {actual} != {expected}"