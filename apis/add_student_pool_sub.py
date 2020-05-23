from flask_restplus import Namespace, fields, Resource
from models import db
from models.course import Course
from models.course_test import Test
from models.pool_subscripion import PoolSubscription
from models.student_test import StudentTest
from models.topic import Topic

api = Namespace('api/addStudentPoolSub', description="")

add_student_pool_model = api.model('addStudentPoolSub',
                          {
                              'pool_id': fields.Integer('pool_id'),
                              'course_id': fields.String('course_id'),
                              'student_id': fields.String('student_id')
                          })

add_student_pool_response = api.model('addStudentPoolSub',
                          {
                              'pool_subscription_id': fields.Integer('pool_subscription_id'),
                              'pool_id': fields.Integer('pool_id'),
                              'course_id': fields.String('course_id'),
                              'student_id': fields.String('student_id')
                          })

@api.route('')
class AddStudentPoolSub(Resource):

    @api.marshal_with(add_student_pool_response)
    @api.expect(add_student_pool_model)
    def post(self):
        pool_sub_details = api.payload
        student_id = pool_sub_details['student_id']
        course_id = pool_sub_details['course_id']
        pool_sub_details = PoolSubscription(pool_sub_details['pool_id'], course_id, student_id)
        # get tests for course
        test_list = Test.get_all_tests(pool_sub_details['course_id'])
        db.session.add(pool_sub_details)
        for test in test_list:
            student_test = StudentTest(student_id, "NT", test["test_id"], course_id)
            db.session.add(student_test)
        db.session.commit()
        return pool_sub_details
