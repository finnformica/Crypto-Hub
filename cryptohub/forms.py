from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateField, SelectField, FloatField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import datetime

tickers_list = ["BTC","LTC","ETH","NEO","BNB","QTUM","EOS","SNT","BNT","GAS","BCC","USDT","HSR","OAX","DNT","MCO","ICN","ZRX","OMG","WTC","YOYO","LRC","TRX","SNGLS","STRAT","BQX","FUN","KNC","CDT","XVG","IOTA","SNM","LINK","CVC","TNT","REP","MDA","MTL","SALT","NULS","SUB","STX","MTH","ADX","ETC","ENG","ZEC","AST","GNT","DGD","BAT","DASH","POWR","BTG","REQ","XMR","EVX","VIB","ENJ","VEN","ARK","XRP","MOD","STORJ","KMD","RCN","EDO","DATA","DLT","MANA","PPT","RDN","GXS","AMB","ARN","BCPT","CND","GVT","POE","BTS","FUEL","XZC","QSP","LSK","BCD","TNB","ADA","LEND","XLM","CMT","WAVES","WABI","GTO","ICX","OST","ELF","AION","WINGS","BRD","NEBL","NAV","VIBE","LUN","TRIG","APPC","CHAT","RLC","INS","PIVX","IOST","STEEM","NANO","AE","VIA","BLZ","SYS","RPX","NCASH","POA","ONT","ZIL","STORM","XEM","WAN","WPR","QLC","GRS","CLOAK","LOOM","BCN","TUSD","ZEN","SKY","THETA","IOTX","QKC","AGI","NXS","SC","NPXS","KEY","NAS","MFT","DENT","IQ","ARDR","HOT","VET","DOCK","POLY","VTHO","ONG","PHX","HC","GO","PAX","RVN","DCR","USDC","MITH","BCHABC","BCHSV","REN","BTT","USDS","FET","TFUEL","CELR","MATIC","ATOM","PHB","ONE","FTM","BTCB","USDSB","CHZ","COS","ALGO","ERD","DOGE","BGBP","DUSK","ANKR","WIN","TUSDB","COCOS","PERL","TOMO","BUSD","BAND","BEAM","HBAR","XTZ","NGN","DGB","NKN","GBP","EUR","KAVA","RUB","UAH","ARPA","TRY","CTXC","AERGO","BCH","TROY","BRL","VITE","FTT","AUD","OGN","DREP","BULL","BEAR","ETHBULL","ETHBEAR","XRPBULL","XRPBEAR","EOSBULL","EOSBEAR","TCT","WRX","LTO","ZAR","MBL","COTI","BKRW","BNBBULL","BNBBEAR","HIVE","STPT","SOL","IDRT","CTSI","CHR","BTCUP","BTCDOWN","HNT","JST","FIO","BIDR","STMX","MDT","PNT","COMP","IRIS","MKR","SXP","SNX","DAI","ETHUP","ETHDOWN","ADAUP","ADADOWN","LINKUP","LINKDOWN","DOT","RUNE","BNBUP","BNBDOWN","XTZUP","XTZDOWN","AVA","BAL","YFI","SRM","ANT","CRV","SAND","OCEAN","NMR","LUNA","IDEX","RSR","PAXG","WNXM","TRB","EGLD","BZRX","WBTC","KSM","SUSHI","YFII","DIA","BEL","UMA","EOSUP","TRXUP","EOSDOWN","TRXDOWN","XRPUP","XRPDOWN","DOTUP","DOTDOWN","NBS","WING","SWRV","LTCUP","LTCDOWN","CREAM","UNI","OXT","SUN","AVAX","BURGER","BAKE","FLM","SCRT","XVS","CAKE","SPARTA","UNIUP","UNIDOWN","ALPHA","ORN","UTK","NEAR","VIDT","AAVE","FIL","SXPUP","SXPDOWN","INJ","FILDOWN","FILUP","YFIUP","YFIDOWN","CTK","EASY","AUDIO","BCHUP","BCHDOWN","BOT","AXS","AKRO","HARD","KP3R","RENBTC","SLP","STRAX","UNFI","CVP","BCHA","FOR","FRONT","ROSE","HEGIC","AAVEUP","AAVEDOWN","PROM","BETH","SKL","GLM","SUSD","COVER","GHST","SUSHIUP","SUSHIDOWN","XLMUP","XLMDOWN","DF","JUV","PSG","BVND","GRT","CELO","TWT","REEF","OG","ATM","ASR","1INCH","RIF","BTCST","TRU","DEXE","CKB","FIRO","LIT","PROS","VAI","SFP","FXS","DODO","AUCTION","UFT","ACM","PHA","TVK","BADGER","FIS","OM","POND","ALICE","DEGO","BIFI","LINA"]

currency_list = ["USD", "GBP"]


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SpotTradeForm(FlaskForm):
    date = DateField('Date Executed', format='%d-%m-%Y', validators=[DataRequired()], default=datetime.utcnow)
    ticker1 = SelectField('Ticker 1', choices=tickers_list+currency_list, default='BTC')
    ticker2 = SelectField('Ticker 2', choices=tickers_list+currency_list, default='USD')
    type = SelectField('Type', choices=['Buy', 'Sell'], default='Buy')
    price = FloatField('Price of ticker 1 compared to ticker 2', validators=[DataRequired()])
    quantity = FloatField('Quantity of ticker 1', validators=[DataRequired()])
    fee_quantity = FloatField('Fee', validators=[DataRequired()])
    fee_currency = SelectField('Type', choices=tickers_list+currency_list, default='USD')

    submit = SubmitField('Log trade')


class PerpetualTradeForm(FlaskForm):
    date = DateField('Date Executed', format='%d-%m-%Y', validators=[DataRequired()], default=datetime.utcnow)
    ticker1 = SelectField('Ticker 1', choices=tickers_list+currency_list, default='BTC')
    ticker2 = SelectField('Ticker 2', choices=tickers_list+currency_list, default='USD')
    type = SelectField('Type', choices=['Long', 'Short'], default='Long')
    leverage = IntegerField('Leverage', validators=[DataRequired()], default=0)
    balance = FloatField('Account balance', validators=[DataRequired()])
    percent_risked = FloatField('Percent of account risked', validators=[DataRequired()])
    entry_price = FloatField('Entry price', validators=[DataRequired()])
    stop_loss = FloatField('Stop loss', validators=[DataRequired()])
    take_profit = FloatField('Take profit', validators=[DataRequired()])
    exit_price = FloatField('Exit price', validators=[DataRequired()])
    notes = StringField('Strategy used', validators=[DataRequired()])

    submit = SubmitField('Log trade')
