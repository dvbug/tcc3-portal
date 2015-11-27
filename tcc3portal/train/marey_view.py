# coding:utf-8
"""
    train.marey_view
    ~~~~~~~~~~~~~~~~

    train data analytics - marey diagram view module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask import Blueprint, url_for, render_template
from ..tcc_core.babel import _

bp = Blueprint('marey', __name__)


@bp.route('/', methods=['GET'])
@bp.route('/marey', methods=['GET'])
def index():
    return render_template('marey_diagram_view.html')
