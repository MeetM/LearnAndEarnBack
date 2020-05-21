from models import db


class Test(db.Model):
    __tablename__ = 'test'

    test_id = db.Column(db.Integer, primary_key=True)
    test_num = db.Column(db.Integer)
    pool_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer)

    def __init__(self, test_id, test_num, pool_id, course_id):
        self.test_id = test_id
        self.test_num = test_num
        self.pool_id = pool_id
        self.course_id = course_id