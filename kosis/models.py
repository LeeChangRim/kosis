from kosis import db

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(12), nullable=False, unique=True)    #종목코드
    name = db.Column(db.String(100), nullable=True)                 #종목명
    symbol = db.Column(db.String(20), nullable=True)                #심볼코드
    country_code = db.Column(db.String(3), nullable=True)           #국가코드
    country_name = db.Column(db.String(50), nullable=True)          #국가명
    currency_code = db.Column(db.String(3), nullable=True)          #통화코드
    currency_name = db.Column(db.String(50), nullable=True)         #통화명
    price_per_share = db.Column(db.Float, nullable=True)            #주당가격
    market_cap = db.Column(db.Float, nullable=True)                 #시가총액
    dividend_yield = db.Column(db.Float, nullable=True)             #배당수익률
    pe_ratio = db.Column(db.Float, nullable=True)                   #P/E Ratio
    dividend = db.Column(db.Float, nullable=True)                   #배당금
    sector = db.Column(db.String(100), nullable=True)               #섹터
    industry = db.Column(db.String(100), nullable=True)             #산업
    exchange = db.Column(db.String(50), nullable=True)              #거래소
    create_date = db.Column(db.DateTime(), nullable=False)          #생성일자

class StockPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(12), nullable=False)                 #종목코드
    t_date = db.Column(db.String(8), nullable=True)                 #거래일자
    price = db.Column(db.Float, nullable=True)
    volume = db.Column(db.Float, nullable=True)