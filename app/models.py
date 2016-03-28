from app import db
from datetime import datetime
import requests

def get_page_likes(link):
    r = requests.get(r"https://api.facebook.com/method/fql.q\uery?\
        query=select%20like_count%20from%20link_stat%20where%20ur\
        l=%27"+link+r"%27&format=json")
    data = r.json()


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), nullable=(False), default="No name")
    desc = db.Column(db.String(300), default="")
    link = db.Column(db.String(300), nullable=False, default="http://badurld.com")
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    likes = db.Column(db.Integer, nullable=False, default=datetime.now())

    def __init__(self, title, desc, link, ):
        pass
    def __repr__(self):
        return '<User %r>' % (self.title)
