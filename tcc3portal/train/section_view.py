# coding:utf-8
"""
    train.section_view
    ~~~~~~~~~~~~~~~~~~

    train data analytics - section diagram view module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask import Blueprint, url_for, render_template
from ..tcc_core.babel import _

bp = Blueprint('section', __name__)


@bp.route('/', methods=['GET'])
@bp.route('/section', methods=['GET'])
def index():
    return render_template('section_view.html')
