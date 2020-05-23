from flask_restplus import Api

from .sign_up import api as sign_up_api
from .verify_user import api as verify_user_api
from .get_topics import api as get_topics_api
from .add_topic import api as add_topics_api
from .add_course import api as add_course_api
from .get_courses import api as get_courses_api
from .auth import api as auth_api
from .add_test import api as add_test_api
from .add_student_pool_sub import api as add_student_pool_sub_api
from .get_student_tests import api as get_student_tests_api
from .add_pool import api as add_pool_api

api = Api(
    title='Learn and Earn',
    version='1.0',
    description='For HackMoney',
)

api.add_namespace(sign_up_api)
api.add_namespace(verify_user_api)
api.add_namespace(add_topics_api)
api.add_namespace(get_topics_api)
api.add_namespace(add_course_api)
api.add_namespace(get_courses_api)
api.add_namespace(auth_api)
api.add_namespace(add_test_api)
api.add_namespace(add_student_pool_sub_api)
api.add_namespace(get_student_tests_api)
api.add_namespace(add_pool_api)