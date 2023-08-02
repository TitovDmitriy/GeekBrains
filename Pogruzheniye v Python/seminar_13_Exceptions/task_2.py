import csv


class InvalidNameError(ValueError):
    def __init__(self):
        super().__init__("ФИО должно содержать только буквы и начинаться с заглавной буквы")


class OutOfRangeError(ValueError):
    def __init__(self, field, min_value, max_value):
        super().__init__(f"{field} должно быть в диапазоне от {min_value} до {max_value}")


class Student:
    def __init__(self, name, subjects_file):
        self._validate_name(name)
        self.name = name
        self._load_subjects(subjects_file)
        self._grades = {subject: [] for subject in self.subjects}
        self._test_results = {subject: [] for subject in self.subjects}

    def _validate_name(self, name):
        if not name.isalpha() or not name.istitle():
            raise InvalidNameError()

    def _load_subjects(self, file_path):
        with open(file_path, newline='') as file:
            reader = csv.reader(file)
            self.subjects = [subject[0] for subject in reader]

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не доступен для данного студента")
        if grade < 2 or grade > 5:
            raise OutOfRangeError("Оценка", 2, 5)
        self._grades[subject].append(grade)

    def add_test_result(self, subject, result):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не доступен для данного студента")
        if result < 0 or result > 100:
            raise OutOfRangeError("Результат теста", 0, 100)
        self._test_results[subject].append(result)

    def _calculate_average(self, data):
        if not data:
            return 0
        return sum(data) / len(data)

    def get_subject_average_grade(self, subject):
        return self._calculate_average(self._grades.get(subject, []))

    def get_subject_average_test_result(self, subject):
        return self._calculate_average(self._test_results.get(subject, []))

    def get_overall_average_grade(self):
        all_grades = [grade for grades in self._grades.values() for grade in grades]
        return self._calculate_average(all_grades)

    def get_overall_average_test_result(self):
        all_test_results = [result for results in self._test_results.values() for result in results]
        return self._calculate_average(all_test_results)


if __name__ == "__main__":
    try:
        subjects_file = "subjects.csv"
        student_name = "Иванов Иван Иванович"

        student = Student(student_name, subjects_file)

        # Добавим оценки и результаты тестов для предметов
        student.add_grade("Математика", 4)
        student.add_test_result("Математика", 80)
        student.add_grade("Физика", 5)
        student.add_test_result("Физика", 95)
        student.add_grade("История", 3)
        student.add_test_result("История", 70)

        # Получим средний балл и результаты тестов для каждого предмета
        for subject in student.subjects:
            print(f"Предмет: {subject}")
            print(f"Средний балл: {student.get_subject_average_grade(subject)}")
            print(f"Средний результат тестов: {student.get_subject_average_test_result(subject)}")
            print()

        # Получим общий средний балл и общий средний результат тестов
        print(f"Общий средний балл по оценкам: {student.get_overall_average_grade()}")
        print(f"Общий средний результат тестов: {student.get_overall_average_test_result()}")

    except InvalidNameError:
        print("Ошибка: ФИО должно содержать только буквы и начинаться с заглавной буквы")
    except OutOfRangeError as e:
        print(f"Ошибка: {e}")
