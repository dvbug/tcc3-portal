# coding:utf-8
"""
    train.upload_line_config
    ~~~~~~~~~~~~~~~~~~~~~~~~

    train data analytics - marey diagram upload_line_config module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask import Blueprint, url_for, redirect, render_template, g
from tcc3portal.tcc_core.babel import _
from .forms import LineConfigForm

bp = Blueprint('config', __name__, url_prefix='/config')


@bp.route('/', methods=['GET'])
def index():
    form = LineConfigForm()
    g.line_config_form = form

    return render_template('config_view.html', form=form)


@bp.route('/upload_line', methods=['POST'])
def upload_line():
    if g.line_config_form.validate_on_submit():
        pass

    return redirect(url_for('config.index'))