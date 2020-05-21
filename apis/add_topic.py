from flask_restplus import Namespace, fields, Resource
from models import db
from models.topic import Topic

api = Namespace('api/addTopic', description="")


add_topic_model = api.model('addTopic',
                          {
                              'topic_name': fields.String('topic_name'),
                              'topic_param': fields.String('topic_param')
                          })


@api.route('')
class AddTopic(Resource):

    @api.marshal_with(add_topic_model)
    @api.expect(add_topic_model)
    def post(self):
        topic_details = api.payload
        topic = Topic(topic_details['topic_name'], topic_details['topic_param'])
        db.session.add(topic)
        db.session.commit()
        return topic
