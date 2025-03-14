class StudentManagement:
    """
    Klasa zarządzająca studentami i ich ocenami.
    """

    def __init__(self):
        self.students = {}  # Przechowuje studentów w formacie {id: {"name": str, "age": int, "grades": {}}}

    def add_student(self, id: str, name: str, age: int) -> bool:
        """
        Dodaje nowego studenta do bazy danych.
        """
        if id in self.students:
            return False  # Student już istnieje
        self.students[id] = {"name": name, "age": age, "grades": {}}
        return True

    def update_student(self, id: str, name: str, age: int) -> bool:
        """
        Aktualizuje dane istniejącego studenta na podstawie identyfikatora.
        """
        if id not in self.students:
            return False  # Student nie istnieje
        self.students[id]["name"] = name
        self.students[id]["age"] = age
        return True

    def remove_student(self, id: str) -> bool:
        """
        Usuwa studenta z bazy danych na podstawie jego identyfikatora.
        """
        if id not in self.students:
            return False  # Student nie istnieje
        del self.students[id]
        return True

    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        """
        Dodaje ocenę z danego przedmiotu dla określonego studenta.
        """
        valid_grades = {2.0, 3.0, 3.5, 4.0, 4.5, 5.0}
        if student_id not in self.students or grade not in valid_grades:
            return False  # Student nie istnieje lub ocena niepoprawna

        if subject not in self.students[student_id]["grades"]:
            self.students[student_id]["grades"][subject] = []

        self.students[student_id]["grades"][subject].append(grade)
        return True

    def avg_grades(self, subject: str) -> float:
        """
        Oblicza średnią ocen z danego przedmiotu dla wszystkich studentów.
        """
        total, count = 0, 0
        for student in self.students.values():
            if subject in student["grades"] and student["grades"][subject]:
                total += sum(student["grades"][subject])
                count += len(student["grades"][subject])

        return total / count if count > 0 else 0.0