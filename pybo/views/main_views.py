from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def initial_page():
    return render_template('initial/initial_detail.html')


#questionlist
@bp.route('/community')
def community_page():
   return redirect(url_for('question._list'))

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template('question/question_detail.html', question=question)

