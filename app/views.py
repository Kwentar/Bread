from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Хлебушек'}
    posts = [
        { 
            'author': {'nickname': 'karim-abdul'},
            'body': '''илья старается скорее\n
                        уравновесить зло добром\n
                        увидел парни бьют мальчишку\n
                        красиво рядом станцевал'''},
        {
            'author': {'nickname': 'tequilaman'},
            'body':  '''купил айфон а чо с ним делать\n
                        где кнопки чтобы нажимать\n
                        и как мне позвонить сереге\n
                        а вот и он звонит и чо'''
        },
        {
            'author': {'nickname': 'supposedly-me'},
            'body': '''входя в автобус не стесняйся\n
            садись на лучшие места\n
            в россии все немножко дети\n
            и каждый в чём то инвалид'''
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)
