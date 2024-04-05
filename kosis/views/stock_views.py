from flask import Blueprint, render_template, request, url_for

from kosis.models import Stock

bp = Blueprint('stock', __name__, url_prefix='/stock')


@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)  # 페이지
    stock_list = Stock.query.order_by(Stock.code.asc())
    stock_list = stock_list.paginate(page=page, per_page=10)
    return render_template('stock/stock_list.html', stock_list=stock_list)


@bp.route('/detail/<int:stock_id>/')
def detail(stock_id):
    stock = Stock.query.get_or_404(stock_id)
    return render_template('stock/stock_detail.html', stock=stock)