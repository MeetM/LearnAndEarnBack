
from flask_restplus import Namespace, Resource

from models.course import Course

api = Namespace('api/getCourses', description="")


@api.route('')
class GetCourses(Resource):

    def get(self):
        return Course.get_all_courses(), 200
