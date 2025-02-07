from flask import Blueprint, render_template

bp = Blueprint('initial', __name__, url_prefix='/')

@bp.route('/')
def _initial():
    return render_template('initial/initial_detail.html')