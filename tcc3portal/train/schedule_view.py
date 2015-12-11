# coding:utf-8
"""
    train.schedule_view
    ~~~~~~~~~~~~~~~~~~~

    train data analytics - marey diagram upload schedule data module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
import os
import datetime
from urllib import parse
from http.client import HTTPConnection, HTTPException

from flask import Blueprint, url_for, redirect, render_template, current_app, request, json, flash
from werkzeug.utils import secure_filename
from tcc3portal.tcc_core.babel import _
from .forms import ScheduleForm

bp = Blueprint('schedule', __name__, url_prefix='/schedule')


@bp.route('/', methods=['GET', 'POST'])
def upload():
    form = ScheduleForm()
    if form.validate_on_submit():
        schedule_date = form.date.data.strftime('%Y%m%d')
        schedule_type = form.type.data  # request.form['type']
        schedule_file = form.file.data
        # .read().decode('utf-8')
        filename = secure_filename(schedule_file.filename)
        upload_api = os.path.join(current_app.config['DAC_API_SCHEDULES_URL'], schedule_date, schedule_type)
        # print(upload_url)
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        data = parse.urlencode({
            'file': schedule_file.read().decode('utf-8'),
            'fname': filename,
        })

        try:
            conn = HTTPConnection(current_app.config['DAC_HOST_URL'])
            conn.request("POST", upload_api, data, headers)
            resp = conn.getresponse()
            if resp.code == 200:
                resp_data = json.loads(resp.read().decode('utf-8'))
                print(resp_data)
            else:
                raise HTTPException()

        except HTTPException:
            resp_data = {}
            flash(_("Can not connect to DAC server."))
        finally:
            conn.close()
        flash(resp_data)

        return redirect(url_for('schedule.upload'))

    return render_template('schedule_view.html', form=form)




