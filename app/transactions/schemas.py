from config import ma
from transactions.models import Transaction


class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction
        fields = (
            "id",
            "amount",
            "description",
            "transaction_date",
            "update_at",
            "group",
            "account",
        )


transaction_schema = TransactionSchema()
transaction_many_schema = TransactionSchema(many=True)
