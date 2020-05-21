from random import random

from flask import request
from flask_restplus import Namespace, fields, Resource
from models import db
from models.nonce_verify import NonceVerify
from models.student import Student

api = Namespace('api/signUp', description="Sign Up a new user")


sign_up_model = api.model('signUp',
                          {
                              'name': fields.String('Student Name'),
                              'email': fields.String('Email'),
                              'eth_address': fields.String('Eth-Address')
                          })


@api.route('')
class SignUp(Resource):

    @api.marshal_with(sign_up_model)
    @api.expect(sign_up_model)
    def post(self):
        student_details = api.payload
        print(student_details)
        student = Student(student_details['email'], student_details['eth_address'], student_details['name'])
        print(student)
        db.session.add(student)
        db.session.commit()
        return student
