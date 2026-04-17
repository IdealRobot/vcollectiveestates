from flask import Blueprint, render_template
from core.estate.models import Sale

estate = Blueprint('estate', __name__, url_prefix='')

@estate.route('/dashboard')
def dashboard():
    sales = Sale.query.all()
    return render_template('estate/dashboard.html', sales=sales)

@estate.route('/sale/new')
def sale_new():
    return render_template('estate/sale_new.html')

@estate.route('/sale/<int:id>')
def sale_view(id):
    return render_template('estate/sale_view.html', id=id)

@estate.route('/sale/<int:id>/add')
def item_add(id):
    return render_template('estate/item_add.html', id=id)

@estate.route('/pos/<int:sale_id>')
def pos(sale_id):
    return render_template('estate/pos.html', sale_id=sale_id)

@estate.route('/client/<int:sale_id>')
def client_view(sale_id):
    return render_template('estate/client_view.html', sale_id=sale_id)
