import flask
from flask import request
from flask_restplus import Namespace, fields, Resource
from models.nonce_verify import NonceVerify
from models.student import Student

api = Namespace('api/verifyUser', description="Verify User Address")

user_address_verify_parser = api.parser()
user_address_verify_parser.add_argument('publicAddress', type=str, help='Public Address', location='path')


@api.route('')
class VerifyUser(Resource):

    @api.expect(user_address_verify_parser)
    def get(self):
        data = request.args
        print("Received data = ", data)
        address = data["publicAddress"]
        student = Student.get_student_by_address(address)
        if student is not None:
            return [VerifyUser.return_nonce(address)], 200
        return [], 200

    @classmethod
    def return_nonce(cls, address):
        nonce = NonceVerify.create_nonce(address)
        return {'publicAddress': address, 'nonce': nonce}
