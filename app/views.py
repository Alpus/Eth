from app import app
from flask import render_template

@app.route("/")
def index():
    #https://api.facebook.com/method/fql.query?query=select%20like_count%20from%20link_stat%20where%20url=%27http://apushin.com%27&format=json
    ad = [{'tab': 'Ad', 'link': 'hse.ru', 'title': 'Title', 'desc': 'D\
    escription  are 4 colors and 3 sizes of circular spinners. The spi\
    nner should be nested in a preloader-wrapper div. The default size\
     is medium, but you can add the classes big or small to adjust the\
      size accordingly. You can add the classes spinner-red-only, spin\
      ner-blue-only, spinner-yellow-only and spinner-green-only. You c\
      an also leave this class as just spinner-layer and it will be se\
      t to the $spinner-default-color variable in our variables.sc'}]
    return render_template('cards.html', ad=ad)
