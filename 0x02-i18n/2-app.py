#!/usr/bin/env python3
""" Basic Flask app. """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Config class for the Babel object. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Determines the best language to use for the user. """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index():
    """
    Renders the '1-index.html' template and returns it as a response.

    This function is a Flask route that is mapped to the root URL ("/").
    It is responsible for displaying the home page of the application.

    Returns:
        A rendered HTML template.
    """
    # Render the '1-index.html' template and return it as a response.
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
