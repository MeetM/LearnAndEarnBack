from flask import request
from flask_restplus import Namespace, Resource

from models.course import Course
from models.student_test import StudentTest

api = Namespace('api/getStudentTests', description="")

'''
{
            "st_id": student_test.st_id,
            "status": student_test.status,
            "student_id": student_test.student_id,
            "test_num": test.test_num,
            "test_name": test.test_name,
            "test_id": student_test.test_id,
            "course_id": student_test.course_id
        }

'''
@api.route('')
class GetStudentTests(Resource):

    def get(self):
        data = request.args
        return StudentTest.get_all_tests_for_student(data["student_id"]), 200
