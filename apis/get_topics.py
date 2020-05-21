from flask_restplus import Namespace, fields, Resource
from models.topic import Topic

api = Namespace('api/getTopics', description="")


@api.route('')
class GetTopics(Resource):

    def get(self):
        return Topic.get_all_topics(), 200
