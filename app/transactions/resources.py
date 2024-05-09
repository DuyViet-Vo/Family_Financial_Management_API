from config import db
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource, abort
from transactions.models import Transaction
from transactions.schemas import transaction_many_schema, transaction_schema


class TransactionsResource(Resource):
    @jwt_required()
    def get(self):
        group = Transaction.query.all()
        return transaction_many_schema.dump(group)

    @jwt_required()
    def post(self):
        amount = request.json["amount"]
        description = request.json["description"]
        update_at = request.json["update_at"]
        group = request.json["group"]
        account = request.json["account"]
        new_transaction = Transaction(
            amount=amount,
            group=group,
            description=description,
            update_at=update_at,
            account=account,
        )
        db.session.add(new_transaction)
        db.session.commit()
        return transaction_schema.dump(new_transaction), 201


class TransactionsResourceID(Resource):
    @jwt_required()
    def get(self, transaction_id):
        transaction = Transaction.query.get(transaction_id)
        if transaction:
            return transaction_schema.dump(transaction)
        else:
            abort(404, message="Transaction not found")

    @jwt_required()
    def put(self, transaction_id):
        transaction = Transaction.query.get(transaction_id)
        if transaction:
            transaction.amount = request.json["amount"]
            transaction.description = request.json["description"]
            transaction.update_at = request.json["update_at"]
            db.session.commit()
            return transaction_schema.dump(transaction)
        else:
            abort(404, message="Transaction not found")

    @jwt_required()
    def delete(self, transaction_id):
        transaction = Transaction.query.get(transaction_id)
        if transaction:
            db.session.delete(transaction)
            db.session.commit()
            return "", 204
        else:
            abort(404, message="Transaction not found")
