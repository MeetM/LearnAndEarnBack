import flask
from eth_account.messages import defunct_hash_message
from flask import request
from flask_restplus import Namespace, fields, Resource
from web3.auto import w3

from models.nonce_verify import NonceVerify
from models.student import Student

from web3 import Web3

api = Namespace('api/auth', description="Verify User Address")


@api.route('')
class Auth(Resource):

    @classmethod
    def recover_address(cls, message, signature):
        message_hash = defunct_hash_message(text=message)
        address = w3.eth.account.recoverHash(message_hash, signature=signature)
        return address

    # @api.expect(sign_up_model)
    def post(self):
        data = request.get_json()
        public_address = data["publicAddress"]
        signature = data["signature"]
        nonce = NonceVerify.get_nonce(public_address)
        recovered_address = Auth.recover_address(message=str(nonce), signature=signature)
        print(recovered_address)
        return {"auth": recovered_address}, 200
