from models import db


class Test(db.Model):
    __tablename__ = 'test'

    test_id = db.Column(db.Integer, primary_key=True)
    test_num = db.Column(db.Integer)
    test_name = db.Column(db.String(2000))
    course_id = db.Column(db.Integer)

    def __init__(self, test_num, test_name, course_id):
        self.test_name = test_name
        self.test_num = test_num
        self.course_id = course_id

    @classmethod
    def get_all_tests(cls, course_id):
        tests = cls.query.filter_by(course_id=course_id)
        response = []
        for test in tests:
            response.append(Test._response_marshall(test))
        return response

    @staticmethod
    def _response_marshall(test):
        return {
            "test_id": test.test_id,
            "test_num": test.test_num,
            "test_name": test.test_name,
            "course_id": test.course_id
        }