from flask_restplus import Namespace, fields, Resource
from models import db
from models.course import Course
from models.topic import Topic

api = Namespace('api/addCourse', description="")


add_course_model = api.model('addCourse',
                          {
                              'topic_id': fields.Integer('topic_id'),
                              'course_name': fields.String('course_name'),
                              'course_param': fields.String('course_param')
                          })


@api.route('')
class AddCourse(Resource):

    @api.marshal_with(add_course_model)
    @api.expect(add_course_model)
    def post(self):
        course_details = api.payload
        course = Course(course_details['topic_id'], course_details['course_name'], course_details['course_param'])
        db.session.add(course)
        db.session.commit()
        return course
