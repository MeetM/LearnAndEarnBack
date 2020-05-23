from models import db


class PoolSubscription(db.Model):
    __tablename__ = 'pool'

    pool_subscription_id = db.Column(db.Integer, primary_key=True)
    pool_id = db.Column(db.Integer)
    course_id = db.Column(db.Integer)
    student_id = db.Column(db.Integer)

    def __init__(self, pool_id, course_id, student_id):
        self.pool_id = pool_id
        self.course_id = course_id
        self.student_id = student_id

    @classmethod
    def get_all_pool_subscriptions(cls):
        pool_subscriptions = cls.query.all()
        response = []
        for pool_sub in pool_subscriptions:
            response.append(PoolSubscription._response_marshall(pool_sub))
        return response

    @staticmethod
    def _response_marshall(pool_sub):
        return {
            "pool_subscription_id": pool_sub.pool_subscription_id,
            "pool_id": pool_sub.pool_id,
            "course_id": pool_sub.course_id,
            "student_id": pool_sub.student_id
        }