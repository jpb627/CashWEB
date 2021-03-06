# ./server/__init__.py


#################
#### imports ####
#################

import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_restful import Api

from ..config import DevelopmentConfig

################
#    Config    #
################

app = Flask(
    __name__,
    template_folder='../client/templates',
    static_folder='../client/static'
)

app_settings = os.getenv('APP_SETTINGS', DevelopmentConfig)
app.config.from_object(app_settings)


####################
#### extensions ####
####################

# SQLAlchemy db setup
db = SQLAlchemy(app)

# Debugging Toolbar
toolbar = DebugToolbarExtension(app)

# Mail setup
mail = Mail(app)

#####################
### flask-security ##
#####################
# Uncomment to use flask-security

from cashweb.server.models import User, Role, Anonymous
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, anonymous_user=Anonymous)

###################
### blueprints ####
###################

from cashweb.server.user.views import user_blueprint
from cashweb.server.main.views import main_blueprint
app.register_blueprint(user_blueprint)
app.register_blueprint(main_blueprint)


###################
###  API Setup  ###
###################
api = Api(app)


###################
### flask-login ####
###################
# Uncoment if not using flask_security

# from cashweb.server.models import User
#
# login_manager.login_view = "user.login"
# login_manager.login_message_category = 'danger'


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.filter(User.id == int(user_id)).first()


########################
#### error handlers ####
########################

@app.errorhandler(401)
def forbidden_page(error):
    return render_template("errors/401.html"), 401


@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500
