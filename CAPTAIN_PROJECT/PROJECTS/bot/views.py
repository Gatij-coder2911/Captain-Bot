from django.shortcuts import render, redirect 
import mysql.connector
import subprocess as sp
# Create your views here.
# data base connection
mycon = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345678',
    database = 'captaindb'
)
cur = mycon.cursor()
mycon.autocommit = True


def index(request):
    return render(request, 'index.html')

def base(request):
    if request.method == 'POST': 
        # MYSQL
        username = request.POST['username']
        if(mycon.is_connected()):
            print('connection successful')
            # fetching the username from the first page and inserting it into database
            cur.execute("insert into users(username) values('{}')".format(username))
        # file_path="../PROJECTS/Captain.py"
        # sp.run(['python', file_path], check=True)
        return redirect('/captain/')
    return render(request, 'base.html')

def startprogram(request):
    file_path="../PROJECTS/Captain.py"
    sp.run(['python', file_path], check=True)
    return redirect('/logs/')

def showlog(request):
    if(mycon.is_connected()):
        # fetch latest user
        cur.execute('select username from users order by id desc limit 1')
        curr_user = cur.fetchall()[0][0]
        print(curr_user)
        
        # get log data of the user 
        cur.execute("select userquery , query_datetime from data where username = '{}'".format(curr_user))
        data = cur.fetchall()
        print(data)
        #  Converting List of touples into list of dictionary
        # [('user_command','command_datetime'),] --> [{'command':'user_command', 'datetime':'command_datetime'},]
        userdata = []
        # list me iterate kar ke touples uhta rhee hai
        for i in data:
            userdata.append({'command' : i[0] , 'datetime' : i[1]})
        print(userdata)
        
        context = {
            'currentuser' : curr_user,
            'loglist' : userdata
        }
        return render(request, 'logs.html', context)