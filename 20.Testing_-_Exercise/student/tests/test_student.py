from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):

    def setUp(self):
        self.student1 = Student('Student1')
        self.student2 = Student('Student2', {'math': ['some note']})

    def test_initialization(self):
        # test student1
        self.assertEqual('Student1', self.student1.name)
        self.assertEqual({}, self.student1.courses)

        # test student2
        self.assertEqual('Student2', self.student2.name)
        self.assertEqual({'math': ['some note']}, self.student2.courses)

    # сега трябва да направим 4 теста за enroll
    def test_add_notes_to_existing_course(self):
        result = self.student2.enroll('math', ['second note'])
        # долните 2 реда реално са еднакви
        self.assertEqual(self.student2.courses, {'math': ['some note', 'second note']})
        self.assertEqual(self.student2.courses['math'][1], 'second note')
        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_add_notes_to_non_existing_course_without_third_param(self):
        result = self.student1.enroll('math', ['math notes'])
        self.assertEqual(self.student1.courses['math'][0], "math notes")
        self.assertEqual(result, "Course and course notes have been added.")

    def test_add_notes_to_non_existing_course_with_third_param(self):
        result = self.student1.enroll('math', ['math notes'], "Y")
        self.assertEqual(self.student1.courses['math'][0], "math notes")
        self.assertEqual(result, "Course and course notes have been added.")

    def test_add_new_course_without_adding_the_notes(self):
        result = self.student1.enroll('math', ['math notes'], "N")
        self.assertEqual(len(self.student1.courses['math']), 0)
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student2.add_notes('biology', ['some note'])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_return_result(self):
        result = self.student2.add_notes('math', ['second note'])
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student2.leave_course('biology')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_return_result(self):
        result = self.student2.leave_course('math')
        self.assertEqual("Course has been removed", result)


if __name__ == "__main__":
    main()