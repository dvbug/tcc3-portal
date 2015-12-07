# coding:utf-8
"""
    train.schedule_view
    ~~~~~~~~~~~~~~~~~~~

    train data analytics - marey diagram upload schedule data module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
import os
from urllib import parse
from http.client import HTTPConnection, HTTPException

from flask import Blueprint, url_for, redirect, render_template, current_app, request, json, flash
from werkzeug.utils import secure_filename
from tcc3portal.tcc_core.babel import _
from .forms import ScheduleForm

bp = Blueprint('schedule', __name__, url_prefix='/schedule')


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = ScheduleForm()
    if form.validate_on_submit():
        print(form.date)
    return render_template('schedule_view.html', form=form)


# @bp.route('/upload', methods=['POST'])
# def upload():
#     date = request.form['date']
#     print(date)
#     return redirect(url_for('schedule.index'))




