import datetime

from models import db


class Pool(db.Model):
    __tablename__ = 'pool'
    __table_args__ = {'extend_existing': True}

    pool_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer)
    pool_buy_in_start = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    pool_buy_in_end = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    pool_maturity_end = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    stake = db.Column(db.Integer, nullable=True)
    donated_amount = db.Column(db.Integer, nullable=True)

    def __init__(self, course_id, pool_buy_in_start, pool_buy_in_end, pool_maturity_end):
        self.course_id = course_id
        self.pool_buy_in_start = pool_buy_in_start
        self.pool_buy_in_end = pool_buy_in_end
        self.pool_maturity_end = pool_maturity_end

    @classmethod
    def get_all_pools(cls):
        pools = cls.query.all()
        response = []
        for pool in pools:
            response.append(Pool._response_marshall(pool))
        return response

    @staticmethod
    def _response_marshall(pool):
        return {
            "pool_id": pool.pool_id,
            "course_id": pool.course_id,
            "pool_buy_in_start": pool.pool_buy_in_start,
            "pool_maturity_end": pool.pool_maturity_end,
            "stake": pool.stake,
            "donated_amount": pool.donated_amount
        }