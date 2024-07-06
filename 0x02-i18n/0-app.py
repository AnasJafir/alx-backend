#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Index route that renders the '0-index.html' template.

    Returns:
        render_template('0-index.html'): The rendered '0-index.html' template.
    """

    # Render the '0-index.html' template
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug='True')
