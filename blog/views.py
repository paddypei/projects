from django.shortcuts import render_to_response
import MySQLdb
import datetime
from system.models import Role
def hello(request):
    return render_to_response("hello.html")
def current_datetime(request):
    current_date = datetime.datetime.now()
    current_section = "header nav"
    return render_to_response('current_datetime.html', locals())

def hours_ahead(request, offset):
    hour_offset = int(offset)
    a = 2014
    next_time = hour_offset + a
    return render_to_response('hours_ahead.html', locals())

def list_user(request):
    #db = MySQLdb.connect(user="root", db="test", passwd="abc123", host="localhost")
    #cursor = db.cursor()
    #cursor.execute('select * from role')
    #names = [row[1] for row in cursor.fetchall()]
    names = Role.objects.order_by('id')
    #db.close()
    return render_to_response('list_user.html', locals())