#!/usr/bin/env python3
""" Basic Flask app. """
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


class Config:
    """ Config class for the Babel object. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Returns a user dictionary
    None if the ID cannot be found
    or if value is missing
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """ Makes sure the user is logged in before each request. """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """ Determines the best language to use for the user. """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index() -> str:
    """
    Renders the '1-index.html' template and returns it as a response.

    This function is a Flask route that is mapped to the root URL ("/").
    It is responsible for displaying the home page of the application.

    Returns:
        A rendered HTML template.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    """ Runs the Flask app. """
    app.run()
