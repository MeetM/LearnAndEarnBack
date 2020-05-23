from models import db


class Student(db.Model):
    __tablename__ = 'student'

    student_id = db.Column(db.Integer, primary_key=True)
    public_address = db.Column(db.String(1000), unique=True)

    def __init__(self, public_address):
        self.public_address = public_address

    @classmethod
    def get_student(cls, student_id):
        return cls.query.filter_by(student_id=student_id).first()

    @classmethod
    def get_student_by_address(cls, public_address):
        return cls.query.filter_by(public_address=public_address).first()
