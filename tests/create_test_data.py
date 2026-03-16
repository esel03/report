import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

def generate_csv(output_path, num_students=50, days=10):
    fake = Faker('ru_RU')
    Faker.seed(42)
    random.seed(42)

    moods = ['отл', 'норм', 'устал', 'зомби', 'не выжил']
    exam_names = ['Математика']

    data = []
    data_verify = []

    for _ in range(num_students):
        student = fake.name()
        start_date = datetime(2024, 6, 1)

        for i in range(days):
            date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
            coffee_spent = str(random.uniform(100.0, 700.0))
            sleep_hours = str(round(random.uniform(2.0, 8.5), 1))
            study_hours = str(random.randint(2, 18))
            mood = random.choice(moods)
            exam_name = random.choice(exam_names)

            data_verify.append({'student': student,
                                'date': date,
                                'coffee_spent': coffee_spent,
                                'sleep_hours': sleep_hours,
                                'study_hours': study_hours,
                                'mood': mood,
                                'exam': exam_name
                                })
            data.append([
                student, date, coffee_spent,
                sleep_hours, study_hours, mood, exam_name
            ])

    df = pd.DataFrame(data, columns=[
        'student', 'date', 'coffee_spent',
        'sleep_hours', 'study_hours', 'mood', 'exam'
    ])

    df.to_csv(output_path, index=False, encoding='utf-8')
    return data_verify


def generate_data_report(num_students=10, days=2):
    fake = Faker('ru_RU')
    Faker.seed(42)
    random.seed(42)

    moods = ['отл', 'норм', 'устал', 'зомби', 'не выжил']
    exam_names = ['Математика']

    data_tuple = []
    data_dict = []

    for item in range(num_students):
        student = fake.name()
        start_date = datetime(2024, 6, 1)

        for i in range(days):
            date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
            coffee_spent = float(num_students*100 - item*10 - i*2)
            sleep_hours = str(round(random.uniform(2.0, 8.5), 1))
            study_hours = str(random.randint(2, 18))
            mood = random.choice(moods)
            exam_name = random.choice(exam_names)

            data_dict.append({'student': student,
                                'date': date,
                                'coffee_spent': str(coffee_spent),
                                'sleep_hours': sleep_hours,
                                'study_hours': study_hours,
                                'mood': mood,
                                'exam': exam_name
                                })
            data_tuple.append((student, coffee_spent))
            data_shuffle = data_dict
            random.shuffle(data_shuffle)

    return data_dict, data_shuffle, data_tuple
