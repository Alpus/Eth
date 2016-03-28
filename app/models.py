from app import db
from datetime import datetime
import requests
import re

def get_page_likes(link):
    r = requests.get(r"https://api.facebook.com/method/fql.query?query=select%20like_count%20from%20link_stat%20where%20url=%27"+link+r"%27&format=json")
    data = r.json()
    try: 
        return int(data[0]["like_count"])
    except: 
        print -1


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), nullable=(False), default="No name")
    desc = db.Column(db.String(300), default="")
    link = db.Column(db.String(300), nullable=False, default="http://badurld.com")
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    likes = db.Column(db.Integer, default=-1)
    is_ad = db.Column(db.Boolean, default=False)
    checked = db.Column(db.Boolean, default=False)
    mail = db.Column(db.String(60))

    def __init__(self, title, desc, link, mail):
        self.title = title
        self.desc = desc
        self.link = link
        self.likes = get_page_likes(link)
        self.mail = mail

    def __repr__(self):
        return '<User %r>' % (self.title)
