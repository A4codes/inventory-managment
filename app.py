from flask import Flask, jsonify, request, render_template
from flask_migrate import Migrate

from config import Config
from models import db, Product

app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Initialize migration
migrate = Migrate(app, db)


# Home Page
@app.route("/")
def home():
    return "Connected Successfully"


# Inventory Management Page
@app.route("/inventory")
def inventory():
    return render_template("index.html")
@app.route("/dashboard-page")
def dashboard_page():
    return render_template("dashboard.html")


# Add Product
@app.route("/add-product", methods=["POST"])
def add_product():

    data = request.get_json()

    product = Product(
        product_id=data["product_id"],
        product_name=data["product_name"],
        category=data["category"],
        quantity=data["quantity"],
        unit_price=data["unit_price"],
        supplier_name=data.get("supplier_name")
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "message": "Product added successfully"
    })


# View All Products

@app.route("/products")
def products():

    products = Product.query.all()

    result = []

    for p in products:
        result.append({
            "id": p.id,
            "product_id": p.product_id,
            "product_name": p.product_name,
            "category": p.category,
            "quantity": p.quantity,
            "unit_price": p.unit_price,
            "supplier_name": p.supplier_name
        })

    return jsonify(result)


# Dashboard Data
@app.route("/dashboard")
def dashboard():

    products = Product.query.all()

    total_products = len(products)

    total_quantity = sum(
        p.quantity for p in products
    )

    total_inventory_value = sum(
        p.quantity * p.unit_price
        for p in products
    )

    low_stock_count = len([
        p for p in products
        if p.quantity < 10
    ])

    return jsonify({
        "total_products": total_products,
        "total_quantity": total_quantity,
        "total_inventory_value": total_inventory_value,
        "low_stock_count": low_stock_count
    })

@app.route("/routes")
def routes():
    output = []

    for rule in app.url_map.iter_rules():
        output.append(str(rule))

    return "<br>".join(output)

if __name__ == "__main__":
    app.run(debug=True)
