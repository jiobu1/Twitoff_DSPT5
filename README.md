# Twitoff_DSPT5

git clone https://github.com/jiobu1/Twitoff_DSPT5.git
cd twitoff_ DSPT5/

SETUP:
pipenv install
-python 3.7
-Flask 
-Flask-SQLAlchemy 
-Flask-Migrate

Migrate the database:
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade

USAGE
FLASK_APP=web_app flask run


