from flask import Flask, Blueprint
from flask import send_from_directory
import os

blueprint = Blueprint('frontend', __name__)


@blueprint.route('/app')
@blueprint.route('/app/')
@blueprint.route('/app/<path:path>')
def app_index(path=None):
    """
    An endpoint that isn't using method view
    ---
    tags:
    - Frontend
    """

    return send_from_directory(os.path.join(os.getcwd(), "frontend"), "index.html")
