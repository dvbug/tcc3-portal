# coding:utf-8
"""
    train.forms
    ~~~~~~~~~~~~~~~~~~~~~~~~

    train data analytics - forms module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask_wtf import Form
from wtforms import SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from .settings import LINES


class LineConfigForm(Form):
    line_no = SelectField('Line No', choices=LINES)
    config_file = FileField('File', validators=[FileRequired(),
                                                FileAllowed(['csv', 'tcsv'], 'CSV only!')])
