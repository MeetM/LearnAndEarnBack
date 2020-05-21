from models import db


class Student(db.Model):
    __tablename__ = 'student'

    student_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    eth_address = db.Column(db.String(1000), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, email, eth_address, name):
        self.email = email.lower().strip()
        self.eth_address = eth_address
        self.name = name

    @classmethod
    def get_student(cls, student_id):
        return cls.query.filter_by(student_id=student_id).first()

    @classmethod
    def get_student_by_address(cls, eth_address):
        return cls.query.filter_by(eth_address=eth_address).first()