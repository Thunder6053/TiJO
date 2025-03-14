import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from student_management import StudentManagement

class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        self.student_management = StudentManagement()

    def test_add_student(self):
        result = self.student_management.add_student("1", "Jan Kowalski", 20)
        self.assertTrue(result)

    def test_add_existing_student(self):
        self.student_management.add_student("1", "Jan Kowalski", 20)
        result = self.student_management.add_student("1", "Jan Kowalski", 20)
        self.assertFalse(result)  # Nie powinno pozwolić na dodanie tego samego studenta ponownie

    def test_update_student(self):
        self.student_management.add_student("1", "Jan Kowalski", 20)
        result = self.student_management.update_student("1", "Jan Nowak", 21)
        self.assertTrue(result)

    def test_update_nonexistent_student(self):
        result = self.student_management.update_student("999", "Nie Istnieje", 25)
        self.assertFalse(result)  # Nie powinno pozwolić na aktualizację nieistniejącego studenta

    def test_remove_student(self):
        self.student_management.add_student("1", "Jan Kowalski", 20)
        result = self.student_management.remove_student("1")
        self.assertTrue(result)

    def test_remove_nonexistent_student(self):
        result = self.student_management.remove_student("999")
        self.assertFalse(result)  # Nie powinno pozwolić na usunięcie nieistniejącego studenta

    def test_add_grade_valid(self):
        self.student_management.add_student("1", "Jan Kowalski", 20)
        result = self.student_management.add_grade("1", "Matematyka", 4.0)
        self.assertTrue(result)

    def test_add_grade_invalid(self):
        self.student_management.add_student("1", "Jan Kowalski", 20)
        result = self.student_management.add_grade("1", "Matematyka", 6.0)
        self.assertFalse(result)  # Powinno zwrócić False, bo 6.0 nie jest poprawną oceną

    def test_add_grade_to_nonexistent_student(self):
        result = self.student_management.add_grade("999", "Matematyka", 4.0)
        self.assertFalse(result)  # Nie można dodać oceny do studenta, który nie istnieje

    def test_avg_grades(self):
        self.student_management.add_student("1", "Jan Kowalski", 20)
        self.student_management.add_student("2", "Anna Nowak", 22)
        self.student_management.add_grade("1", "Matematyka", 4.0)
        self.student_management.add_grade("2", "Matematyka", 5.0)
        avg = self.student_management.avg_grades("Matematyka")
        self.assertEqual(avg, 4.5)  # Poprawne porównanie wartości średniej

    def test_avg_grades_no_grades(self):
        self.student_management.add_student("1", "Jan Kowalski", 20)
        avg = self.student_management.avg_grades("Matematyka")
        self.assertEqual(avg, 0.0)  # Jeśli brak ocen, średnia powinna wynosić 0.0

    def test_avg_grades_single_student(self):
        self.student_management.add_student("1", "Jan Kowalski", 20)
        self.student_management.add_grade("1", "Matematyka", 5.0)
        avg = self.student_management.avg_grades("Matematyka")
        self.assertEqual(avg, 5.0)  # Jeśli jest tylko jedna ocena, średnia powinna wynosić tę ocenę

if __name__ == '__main__':
    unittest.main()