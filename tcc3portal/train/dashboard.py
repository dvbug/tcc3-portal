# coding:utf-8
"""
    train
    ~~~~~~~~~~~~~~~~

    train data analytics - dashboard view module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask import Blueprint, url_for, render_template
from ..tcc_core.babel import _

bp = Blueprint('dashboard', __name__)


@bp.route('/', methods=['GET'])
def index():
    return render_template('dashboard.html')
