# coding:utf-8
"""
    train.forms
    ~~~~~~~~~~~~~~~~~~~~~~~~

    train data analytics - forms module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask_wtf import Form
from wtforms import FileField, SelectField
from wtforms.validators import DataRequired

LINES = [
    ("02", "02"),
    ("04", "04"),
    ("05", "05"),
    ("06", "06"),
    ("07", "07"),
    ("08", "08"),
    ("09", "09"),
    ("10", "10"),
    ("13", "13"),
    ("14", "14"),
    ("15", "15"),
    ("94", "94"),
    ("95", "95"),
    ("96", "96"),
    ("97", "97"),
    ("98", "98"),
]

class LineConfigForm(Form):
    line_no = SelectField('Line No', choices=LINES)
    config_file = FileField('File', validators=[DataRequired()])
