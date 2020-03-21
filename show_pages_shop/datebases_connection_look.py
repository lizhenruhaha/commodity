from flask_sqlalchemy import SQLAlchemy
from database_connect import HOST, PORT, USER, PASSWORD, DB
from flask import Flask
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}:{}/{}'.format(USER,PASSWORD,HOST,PORT,DB)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Info(db.Model):
    __tablename__='info'
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    shop_names = db.Column(db.String(100))
    prices = db.Column(db.Integer())
    shop_urls = db.Column(db.String(1000))
    pic_urls = db.Column(db.String(1000))
    search_name = db.Column(db.String(20))


    def __init__(self,id,shop_names,prices,shop_url,spic_urls,search_name):
        self.id=id
        self.shop_names=shop_names
        self.prices=prices
        self.shop_url=shop_url
        self.spic_urls=spic_urls
        self.search_name=search_name




# ret=db.session.query(Tm).order_by(Tm.prices).all()
# print(ret[2].tmall_id)