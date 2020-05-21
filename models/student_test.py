from models import db


class StudentTest(db.Model):
    __tablename__ = 'student-test'

    st_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(255), unique=True, nullable=False)
    student_id = db.Column(db.Integer)
    test_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer)

    def __init__(self, st_id, status, student_id, test_id, course_id):
        self.st_id = st_id
        self.student_id = student_id
        self.status = status
        self.test_id = test_id
        self.course_id = course_id
