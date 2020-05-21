import datetime

from models import db


class Pool(db.Model):
    __tablename__ = 'pool'

    pool_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer)
    pool_buy_in_start = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    pool_buy_in_end = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    pool_maturity_end = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    stake = db.Column(db.Integer, nullable=False)
    donated_amount = db.Column(db.Integer, nullable=False)

    def __init__(self, pool_id, course_id, pool_buy_in_start, pool_buy_in_end, pool_maturity_end, stake, donated_amount):
        self.pool_id = pool_id
        self.course_id = course_id
        self.pool_buy_in_start = pool_buy_in_start
        self.pool_buy_in_end = pool_buy_in_end
        self.pool_maturity_end = pool_maturity_end
        self.stake = stake
        self.donated_amount = donated_amount