# Importar os módulos necessários
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Configurações básicas
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db = SQLAlchemy(app)

# Cabeçalho do código
"""
* Curso de Engenharia de Software - UniEVANGÉLICA
* Disciplina de Programação Web
* Dev: Jerônimo Neto
* 06/06/2024
"""

# Definição dos modelos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # Nova coluna para categoria de produto

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Camada de Serviço
class ProductService:
    @staticmethod
    def get_products_by_category(category):
        # Retorna todos os produtos de uma categoria específica
        return Product.query.filter_by(category=category).all()

# Camada de Repositório
class ProductRepository:
    @staticmethod
    def get_product_by_id(product_id):
        # Retorna um produto pelo ID
        return Product.query.get(product_id)

# Rotas
@app.route('/login', methods=['POST'])
def login():
    # Implementação do login
    pass

@app.route('/register', methods=['POST'])
def register():
    # Implementação do registro de usuário
    pass

@app.route('/products/<category>', methods=['GET'])
def get_products_by_category(category):
    products = ProductService.get_products_by_category(category)
    result = [{'name': product.name, 'description': product.description, 'price': product.price} for product in products]
    return jsonify(result)

@app.route('/orders', methods=['GET'])
def get_orders():
    # Implementação para retornar todas as ordens de serviço
    pass

# Controller
# Aqui você pode definir funções para cada rota para processar as requisições

# Conexão com banco de dados
if __name__ == '__main__':
    app.run(debug=True)
