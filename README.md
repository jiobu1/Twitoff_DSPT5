# Twitoff_DSPT5

git clone https://github.com/jiobu1/Twitoff_DSPT5.git
cd twitoff_ DSPT5/

SETUP:
pipenv install
-python 3.7
-Flask 
-Flask-SQLAlchemy 
-Flask-Migrate

USAGE
FLASK_APP=web_app flask run


FLASK_APP=web_app flask db init #> generates app/migrations dir
# run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the specified tables