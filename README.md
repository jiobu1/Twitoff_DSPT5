# Twitoff_DSPT5

``git clone https://github.com/jiobu1/Twitoff_DSPT5.git``<br/>
``cd twitoff_ DSPT5/``<br/>

# SETUP: 
``pipenv install``<br/>
``-python 3.7``<br/>
``-Flask ``<br/>
``-Flask-SQLAlchemy`` <br/>
``-Flask-Migrate``<br/>

# Migrate the database:
``FLASK_APP=web_app flask db init``<br/>
``FLASK_APP=web_app flask db migrate``<br/>
``FLASK_APP=web_app flask db upgrade``<br/>

# USAGE
``FLASK_APP=web_app flask run``<br/>

## Production
### first login to the server, then run the migration commands there:
``heroku run bash``
``# ... FLASK_APP=web_app flask db init``<br/>
``# ... FLASK_APP=web_app flask db migrate``<br/>
``# ... FLASK_APP=web_app flask db upgrade``<br/>

### that should work, but alternatively you might be able to run these detached commands (if you didn't ignore your migrations dir):
``heroku run "FLASK_APP=web_app flask db init"``<br/>
``heroku run "FLASK_APP=web_app flask db stamp head"``<br/>
``heroku run "FLASK_APP=web_app flask db migrate"``<br/>
``heroku run "FLASK_APP=web_app flask db upgrade"``<br/>
