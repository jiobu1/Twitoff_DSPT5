# Twitoff_DSPT5
``sh
git clone https://github.com/jiobu1/Twitoff_DSPT5.git
cd twitoff_ DSPT5/
``

# SETUP: 
``sh
pipenv install:
python 3.7
-Flask 
-Flask-SQLAlchemy
-Flask-Migrate
``

# Migrate the database:
``sh
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
``

# USAGE
``sh
FLASK_APP=web_app flask run
``

## Production
``sh
# first login to the server, then run the migration commands there:
heroku run bash
... FLASK_APP=web_app flask db init
... FLASK_APP=web_app flask db migrate
... FLASK_APP=web_app flask db upgrade

# alternatively run these detached commands (if you didn't ignore your migrations dir):
heroku run "FLASK_APP=web_app flask db init"
heroku run "FLASK_APP=web_app flask db stamp head"
heroku run "FLASK_APP=web_app flask db migrate"
heroku run "FLASK_APP=web_app flask db upgrade"
``

