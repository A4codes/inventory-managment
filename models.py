from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    product_id = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    product_name = db.Column(
        db.String(100),
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        nullable=False
    )

    unit_price = db.Column(
        db.Float,
        nullable=False
    )

    supplier_name = db.Column(
        db.String(100)
    )

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "product_name": self.product_name,
            "category": self.category,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "supplier_name": self.supplier_name
        }
