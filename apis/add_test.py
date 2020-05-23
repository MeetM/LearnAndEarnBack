from flask_restplus import Namespace, fields, Resource
from models import db
from models.course_test import Test
from models.topic import Topic

api = Namespace('api/addTest', description="")


add_topic_model = api.model('addTest',
                          {
                              'test_num': fields.String('test_num'),
                              'test_name': fields.String('test_name'),
                              'course_id': fields.String('course_id')
                          })


@api.route('')
class AddTest(Resource):

    def post(self):
        test_details = api.payload
        topic = Test(test_details['test_num'], test_details['test_name'],  test_details['course_id'])
        db.session.add(topic)
        db.session.commit()
        return topic
