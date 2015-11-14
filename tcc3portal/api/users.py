# coding:utf-8
"""
    tcc3portal.api.users
    ~~~~~~~~~~~~~~~~~~~~

    User endpoints.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from flask import Blueprint, current_app
from flask_login import login_required
# from flask import json
# from . import route
from ..tcc_core import User, Q

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/')
@login_required
def show_list():
    """Return the user instance of the currently authenticated user."""
    print(current_app)
    # a = current_user._get_current_object()
    # ret = mongo.db.users.find().sort([("_id", 1)])
    ret = User.objects().all().order_by('+name')  # '-name' or 'name'
    # ret = list(map(lambda x: x, ret))
    # return JSONEncoder().default(ret)
    return ret.to_json()


# @route(bp, '/<user_name>')
@bp.route('/<user_name>')
def show_user(user_name):
    """Return a user instance."""
    # ret = mongo.db.users.find_one_or_404({"name": user_name})
    ret = User.objects(Q(name=user_name) | Q(email=user_name))

    # return JSONEncoder().default(ret)
    return ret.to_json()
