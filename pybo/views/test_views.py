from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from .. import db
from ..forms import QuestionForm, AnswerForm
from ..models import Question, Test, Battery

import json 
from .. import var 

bp = Blueprint('test', __name__, url_prefix='/test')

@bp.route('/list/')
def _list():
    test_list = Test.query.order_by(Test.create_date.desc())
    test_list = test_list.paginate(per_page=10)
    flag = False
    if var.connectionCountdown:
        flag = True 

    return render_template('test/test_list.html', test_list=test_list, flag = flag)

@bp.route('/batteryList/')
def batteryList():
    print('+++++++++++++++&&&&&&&&&&&&&++++++++++ batteryList')
    test_list = Battery.query.order_by(Battery.create_date.desc())
    test_list = test_list.paginate(per_page=10)

    return render_template('test/battery_list.html', test_list=test_list)

@bp.route('/create/<user_data>', methods=('GET', 'POST'))
def createDb(user_data):
    var.connectionCountdown = 20
    print("received: {}".format(user_data))
    obj = json.loads(user_data)
    area = obj.get('area')
    rack = obj.get('rack')
    status = obj.get('status')
    v37 = obj.get('v37')
    v74 = obj.get('v74')
    print('area: {}, rack: {}'.format(area, rack))
    test = Test(area=area, rack=rack, status=status, 
        v37=v37, v74=v74, create_date=datetime.now())
    db.session.add(test)
    db.session.commit()
    return 'ok'
    # return render_template('question/question_form.html', form=form)

# @bp.route('/checkCon/', methods=('GET', 'POST'))
@bp.route('/checkCon/', methods=('GET', 'POST'))
def checkCon():
    returnStr = 'Not Connected'
    if var.connectionCountdown:
        returnStr = 'Connected'

    return returnStr

@bp.route('/battery/<user_data>', methods=('GET', 'POST'))
def batttery(user_data):
    print("battery received: {}".format(user_data))
    obj = json.loads(user_data)
    area = obj.get('area')
    rack = obj.get('rack')
    v37 = obj.get('v37')
    v74 = obj.get('v74')
    print('area: {}, rack: {}'.format(area, rack))
    battery = Battery(area=area, rack=rack, 
        v37=v37, v74=v74, create_date=datetime.now())
    db.session.add(battery)
    db.session.commit()
    return 'ok'


@bp.route('/getChart/')
def getChart():
    global testCount
    # uttec_list = Test.query.filter(Test.rack == 1).order_by(Test.create_date.desc())
    # uttec_list = Battery.query.order_by(Battery.create_date.desc())
    uttec_list = Battery.query.order_by(Battery.create_date)
    data = list()
    count = 0
    for i in uttec_list:
        if i.area == 2:
            data.append(i.rack + 30)
        else:
            data.append(i.rack)
        data.append(i.v37)
        dateStr = i.create_date.strftime('%Y-%m-%d %H:%M:%S')
        data.append(dateStr)
        # print('{},{}'.format(i.v37, dateStr))
        count += 1
    # print('+++++++++++++++++++++++++++++++ getChart, list length:{}'.format(len(data)))
    return data 
