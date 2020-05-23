from flask_restplus import Namespace, fields, Resource
from models import db
from models.course import Course
from models.pool import Pool
from models.topic import Topic

api = Namespace('api/addPool', description="")


add_pool_model = api.model('addPool',
                          {
                              'course_id': fields.Integer('course_id'),
                              'pool_buy_in_start': fields.DateTime('pool_buy_in_start'),
                              'pool_buy_in_end': fields.DateTime('pool_buy_in_end'),
                              'pool_maturity_end': fields.DateTime('pool_maturity_end')
                          })

add_pool_model_response = api.model('addPool',
                          {
                              'pool_id': fields.Integer('pool_id'),
                              'course_id': fields.Integer('course_id'),
                              'pool_buy_in_start': fields.DateTime('pool_buy_in_start'),
                              'pool_buy_in_end': fields.DateTime('pool_buy_in_end'),
                              'pool_maturity_end': fields.DateTime('pool_maturity_end')
                          })
'''
pool_buy_in_start = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    pool_buy_in_end = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    pool_maturity_end = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    stake = db.Column(db.Integer, nullable=False)
    donated_amount = db.Column(db.Integer, nullable=False)
'''


@api.route('')
class AddCourse(Resource):

    @api.marshal_with(add_pool_model_response)
    @api.expect(add_pool_model)
    def post(self):
        pool_details = api.payload
        pool = Pool(pool_details['course_id'], pool_details['pool_buy_in_start'], pool_details['pool_buy_in_end'], pool_details['pool_maturity_end'])
        db.session.add(pool)
        db.session.commit()
        return pool
