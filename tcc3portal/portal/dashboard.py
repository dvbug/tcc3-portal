# coding:utf-8
"""
    tcc3portal.portal.dashboard
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    tcc3portal portal dashboard page.
"""

from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__)


@bp.route('/')
def index():
    return render_template('dashboard.html')
