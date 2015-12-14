# coding:utf-8
"""
    train.config_view
    ~~~~~~~~~~~~~~~~~

    train data analytics - marey diagram upload_line_config module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
import os
from urllib import parse
from http.client import HTTPConnection, HTTPException

from flask import Blueprint, url_for, redirect, render_template, current_app, request, json, flash
from werkzeug.utils import secure_filename
from tcc3portal.tcc_core.babel import _
from .forms import LineConfigForm

bp = Blueprint('config', __name__, url_prefix='/config')


@bp.route('/', methods=['GET'])
def index():
    form = LineConfigForm()
    configs_lines_api_url = os.path.join(current_app.config['DAC_HOST_URL'],
                                         current_app.config['DAC_API_CONFIGS_LINES_URL'])
    try:
        conn = HTTPConnection(current_app.config['DAC_HOST_URL'])
        conn.request("GET", configs_lines_api_url)
        resp = conn.getresponse()
        if resp.code == 200:
            data = json.loads(resp.read().decode())
        else:
            raise HTTPException()
    except HTTPException:
        data = {}
        flash(_("Can not connect to DAC server."))
    except ConnectionError:
        data = {}
        flash(_("Can not connect to DAC server."))
    finally:
        conn.close()

    if data != {}:
        lines = [line for line in data['data']['configs'].keys()]
        configs = data['data']['configs']
    else:
        lines = []
        configs = {}

    return render_template('config_view.html', form=form, data=configs, lines=lines, totail_lines=form.line_no.choices)


@bp.route('/upload_line', methods=['POST'])
def upload_line():
    file = request.files['config_file'] if 'config_file' in request.files else None
    if file:
        filename = secure_filename(file.filename)
        upload_api = os.path.join(current_app.config['DAC_API_CONFIGS_LINES_URL'], request.form['line_no'])
        # print(upload_url)
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        data = parse.urlencode({'file': file.read().decode('utf-8')})

        try:
            conn = HTTPConnection(current_app.config['DAC_HOST_URL'])
            conn.request("POST", upload_api, data, headers)
            resp = conn.getresponse()
            resp_data = json.loads(resp.read().decode('utf-8'))
            print(resp_data)
        except HTTPException as e:
            print("POST CONFIG FILE ERROR", e)
            resp_data = {}
        finally:
            conn.close()
        flash(resp_data)
    else:
        message = "Please select a file for upload."
        flash(message)
    return redirect(url_for('config.index'))
