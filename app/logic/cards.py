from app import db
from app.models import Card

def query_to_list(query, tab):
   return [{'tab': tab, 'link': element.link,
            'title': element.title, 'desc': element.desc}
            for element in query]

def get_all_checked():
    return Card.query.filter_by(checked=True)

def get_ad():
    cards = get_all_checked().filter_by(is_ad=True).order_by(Card.date).all()
    return query_to_list(cards, "Ad")

def get_new():
    cards = get_all_checked().order_by(Card.date).limit(10).all()
    return query_to_list(cards, "New")

def get_all():
    cards = get_all_checked().order_by(Card.likes).all()
    return query_to_list(cards, "All")
