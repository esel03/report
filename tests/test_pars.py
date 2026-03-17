# test_readcsv.py
import os
import tempfile
import pytest
from report.tests.create_test_data import generate_csv
from report.project.pars_csv import ReadCSV

NUM_STUDENTS = 5
NUM_DAYS = 3


@pytest.fixture
def read_csv():
    return ReadCSV()

def test_parse_returns_expected_data(read_csv):
    # Создаём временный файл
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "test_data.csv")

        # Генерируем ожидаемые данные и файл
        expected_data = generate_csv(filepath, num_students=NUM_STUDENTS, days=NUM_DAYS)

        # Читаем через parse
        actual_data = read_csv.parse([filepath])

    # Проверяем количество
    assert actual_data == expected_data, "Данные не совпадает"

