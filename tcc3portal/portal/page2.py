# coding:utf-8
"""
    tcc3portal.portal.page2
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    tcc3portal portal page2 page.
"""

from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('page2', __name__, url_prefix='/page2')


@bp.route('/')
@login_required
def index():
    return render_template('page2.html')

