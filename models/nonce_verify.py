from random import random

from models import db


class NonceVerify(db.Model):
    __tablename__ = 'nonceverify'

    id = db.Column(db.Integer, primary_key=True)
    eth_address = db.Column(db.String(1000), unique=True, nullable=False)
    nonce = db.Column(db.Integer)

    def __init__(self, eth_address, nonce):
        self.eth_address = eth_address
        self.nonce = nonce

    @classmethod
    def get_nonce(cls, eth_address):
        return cls.query.filter_by(eth_address=eth_address).first().nonce

    @classmethod
    def create_nonce(cls, eth_address):
        nonce_verify = cls.query.filter_by(eth_address=eth_address).first()
        if nonce_verify is not None:
            nonce_verify.nonce = nonce_verify.nonce + 1
        else:
            nonce = int(random() * 10000)
            nonce_verify = NonceVerify(eth_address, nonce)
            db.session.add(nonce_verify)
        db.session.commit()
        return nonce_verify.nonce
