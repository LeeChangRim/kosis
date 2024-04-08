from flask import Blueprint, render_template, request, url_for

from kosis.models import Stock, StockPrice

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

@bp.route('/chart/<string:code>/')
def chart(code):
    page = request.args.get('page', type=int, default=1)  # 페이지
    
    stockinfo = Stock.query.filter_by(code=code)

    # 해당 주식 코드(stock_code)에 대한 주가 시세를 일자 기준으로 오름차순 정렬하여 가져오기
    stockprice = StockPrice.query.filter_by(code=code).order_by(StockPrice.t_date.asc())
    
    stockprice = stockprice.paginate(page=page, per_page=10)
    
    # 결과를 JSON 형태로 반환
    dates = [price.t_date for price in stockprice]
    prices = [price.price for price in stockprice]
    volumes = [price.volume for price in stockprice]
    
    return render_template('stock/stock_chart.html', stockprice=stockprice, dates=dates, prices=prices, volumes=volumes, stockinfo=stockinfo)
