from models import db
from models.course_test import Test


class StudentTest(db.Model):
    __tablename__ = 'student-test'

    st_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(255), unique=True, nullable=False)
    student_id = db.Column(db.Integer)
    test_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer)

    def __init__(self, student_id, status, test_id, course_id):
        self.student_id = student_id
        self.status = status
        self.test_id = test_id
        self.course_id = course_id

    @classmethod
    def get_all_tests_for_student(cls, student_id):
        student_test_list = cls.query.filter_by(student_id=student_id)
        response = []
        for student_test in student_test_list:
            response.append(StudentTest._response_marshall(student_test))
        return response

    @staticmethod
    def _response_marshall(student_test):
        test = Test.query.filter_by(test_id=student_test.test_id)
        return {
            "st_id": student_test.st_id,
            "status": student_test.status,
            "student_id": student_test.student_id,
            "test_num": test.test_num,
            "test_name": test.test_name,
            "test_id": student_test.test_id,
            "course_id": student_test.course_id
        }