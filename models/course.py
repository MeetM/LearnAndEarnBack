from models import db


class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer)
    course_name = db.Column(db.String(500), unique=True, nullable=False)
    course_param = db.Column(db.String(500), unique=True, nullable=False)

    def __init__(self, topic_id, course_name, course_param):
        self.topic_id = topic_id
        self.course_name = course_name
        self.course_param = course_param

    @classmethod
    def get_course(cls, course_id):
        return cls.query.filter_by(course_id=course_id).first()

    @classmethod
    def get_all_courses(cls):
        courses = cls.query.all()
        response = []
        for course in courses:
            response.append(Course._response_marshall(course))
        return response

    @staticmethod
    def _response_marshall(course):
        return {
            "topic_id": course.topic_id,
            "course_param": course.course_param,
            "course_name": course.course_name
        }