from random import random

from flask import request
from flask_restplus import Namespace, fields, Resource

from apis.verify_user import VerifyUser
from models import db
from models.nonce_verify import NonceVerify
from models.student import Student

api = Namespace('api/signUp', description="Sign Up a new user")


sign_up_model = api.model('signUp',
                          {
                              'publicAddress': fields.String('publicAddress')
                          })

sign_up_response = api.model('signUp',
                          {
                              'public_address': fields.String('public_address')
                          })


@api.route('')
class SignUp(Resource):

    # @api.expect(sign_up_model)
    def post(self):
        data = request.get_json()
        print(data)
        student = Student(data['publicAddress'])
        print(student)
        db.session.add(student)
        db.session.commit()
        return VerifyUser.return_nonce(student.public_address), 200

    # def options(self):
    #     return self.post()
