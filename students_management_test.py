import students_management
import unittest

class StudentManagementTest(unittest.TestCase):
    def test_add_student_to_empty_list(self):
        result = students_management.add([], 7, "Rufus")
        self.assertEqual(result, [{ "id": 7, "name": "Rufus" }])

if __name__ == '__main__':
    unittest.main()

