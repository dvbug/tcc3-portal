# coding:utf-8
"""
    train.forms
    ~~~~~~~~~~~~~~~~~~~~~~~~

    train data analytics - forms module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask_wtf import Form
from wtforms import SelectField, DateField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from .settings import LINES, SCHEDULE_TYPES


# class DatePickerWidget(object):
#     def __call__(self, field, **kwargs):
#
#         return HTMLString("""
#             <div id="datepicker-container" >
#                 <div class="input-group date" >
#                     <input id="datepicker" type="text" class="form-control" value="07/02/2014" data-provide="datepicker">
#                     <span class="input-group-addon"><i class="glyphicon glyphicon-th"></i></span>
#                 </div>
#                 <script>
#                     $('#datepicker-container .input-group.date').datepicker({
#                         autoclose: false,
#                         todayBtn: "linked",
#                         format: "mm/dd/yyyy",
#                         orientation: "bottom auto",
#                         todayHighlight: "true"
#                     });
#                 </script>
#             </div>
#             """)


class LineConfigForm(Form):
    line_no = SelectField('Line No', choices=LINES)
    config_file = FileField('File', validators=[FileRequired(),
                                                FileAllowed(['csv'], 'CSV only!')])


class ScheduleForm(Form):
    # widget=DatePickerWidget()
    date = DateField('Date', validators=[InputRequired()])
    type = SelectField('Type', choices=SCHEDULE_TYPES, validators=[InputRequired()])
    file = FileField('File', validators=[FileRequired(),
                                         FileAllowed(['csv'], 'CSV only!')])
