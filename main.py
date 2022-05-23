from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
import pymysql
app = Flask(__name__)


def getConnection ():
    return pymysql.connect(
        host = 'localhost',
        db = 'qrcode',
        user = 'root',
        password = '',
        charset = 'utf8',
        cursorclass = pymysql.cursors.DictCursor
		)
    
def showUser():
    connection = getConnection()
    sql = "SELECT * FROM user ORDER BY Date,user.time DESC"
    cursor = connection.cursor()
    cursor.execute(sql)
    user = cursor.fetchall()
    return user   



@app.route('/')
def showuser():
    user = showUser()
    connection = getConnection()
    cursor = connection.cursor()
    re = f"SELECT Date,SUM(Van01) Van01,SUM(Van02) Van02,SUM(Van03) Van03,SUM(Van04) Van04,SUM(Van05) Van05,SUM(Van06) Van06,SUM(Van07) Van07,SUM(Bus01) Bus01,SUM(Bus02) Bus02,SUM(Bus03) Bus03 FROM result  GROUP BY Date"
    cursor = connection.cursor()
    cursor.execute(re)
    res = cursor.fetchall()
    return render_template('dashboard.html',user=user,res=res)

@app.route('/table')
def table():
    user = showUser()
    return render_template('table.html',user=user)

@app.route('/test01')
def test01():
    return render_template('test.html')


@app.route('/tablesearch', methods=['GET', 'POST'])
def tablesearch():
    startday = request.args.get('startdaterange')
    stopday = request.args.get('stopdaterange')
    connection = getConnection()
    u = f"SELECT * FROM user WHERE date BETWEEN '{startday}' AND '{stopday}' ORDER BY Date,user.time DESC"
    cursor = connection.cursor()
    cursor.execute(u)
    user = cursor.fetchall()
    return render_template('table.html',user=user)
#
@app.route('/chart')
def chart():
    connection = getConnection()
    cursor = connection.cursor()
    re = f"SELECT Date,SUM(Van01) Van01,SUM(Van02) Van02,SUM(Van03) Van03,SUM(Van04) Van04,SUM(Van05) Van05,SUM(Van06) Van06,SUM(Van07) Van07,SUM(Bus01) Bus01,SUM(Bus02) Bus02,SUM(Bus03) Bus03 FROM result  GROUP BY Date"
    cursor = connection.cursor()
    cursor.execute(re)
    res = cursor.fetchall()
    return render_template('charts.html',res = res)

@app.route('/chart_DWMY', methods=['GET', 'POST'])
def chart_DWMY():
    times = request.args.get('type')
    print(times)
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    date_time = datetime.fromtimestamp(timestamp)
    date_times = date_time.strftime("%Y-%m-%d,%H:%M:%S")
    day,time = date_times.split(',')
    y,m,d = day.split('-')
    connection = getConnection()
    cursor = connection.cursor()
    c = ''
    print(y)
    if times =='All': #pass
        c = "SELECT Date,SUM(Van01) Van01,SUM(Van02) Van02,SUM(Van03) Van03,SUM(Van04) Van04,SUM(Van05) Van05,SUM(Van06) Van06,SUM(Van07) Van07,SUM(Bus01) Bus01,SUM(Bus02) Bus02,SUM(Bus03) Bus03 FROM result  GROUP BY Date"
    if times =='Daily': 
        c = f"SELECT date_format(date, "'"%d/%m"'") Date,SUM(Van01) Van01,SUM(Van02) Van02,SUM(Van03) Van03,SUM(Van04) Van04,SUM(Van05) Van05,SUM(Van06) Van06,SUM(Van07) Van07,SUM(Bus01) Bus01,SUM(Bus02) Bus02,SUM(Bus03) Bus03 FROM result  where year(Date) LIKE year(CURDATE()) GROUP BY Day(Date)"
        print(c)
    if times == 'Monthly': #pass 
        c = f"SELECT date_format(date, "'"%m-%y"'") Date,SUM(Van01) Van01,SUM(Van02) Van02,SUM(Van03) Van03,SUM(Van04) Van04,SUM(Van05) Van05,SUM(Van06) Van06,SUM(Van07) Van07,SUM(Bus01) Bus01,SUM(Bus02) Bus02,SUM(Bus03) Bus03 FROM result where year(Date) LIKE year(CURDATE()) GROUP BY month(Date)"
        print(c)
    if times == 'Yearly': #pass
        c = "SELECT year(Date) Date,SUM(Van01) Van01,SUM(Van02) Van02,SUM(Van03) Van03,SUM(Van04) Van04,SUM(Van05) Van05,SUM(Van06) Van06,SUM(Van07) Van07,SUM(Bus01) Bus01,SUM(Bus02) Bus02,SUM(Bus03) Bus03 FROM result GROUP BY Year(Date)" 
    if times == 'Weekly': #pass
        c = f"SELECT date_format(date, "'"wk%U"'") Date, SUM(Van01) Van01,SUM(Van02) Van02,SUM(Van03) Van03,SUM(Van04) Van04,SUM(Van05) Van05,SUM(Van06) Van06,SUM(Van07) Van07,SUM(Bus01) Bus01,SUM(Bus02) Bus02,SUM(Bus03) Bus03 FROM result GROUP BY YEARWEEK(Date, 2) ORDER BY YEARWEEK(Date, 2)"
    
            
    cursor = connection.cursor()
    cursor.execute(c)    
    res = cursor.fetchall()
    return render_template('charts.html',res=res) 
    

@app.route('/chartsearch', methods=['GET', 'POST'])
def chartsearch():
    startday = request.args.get('startdaterange')
    stopday = request.args.get('stopdaterange')
    connection = getConnection()
    cursor = connection.cursor()
    re = f"SELECT * FROM result WHERE date BETWEEN '{startday}' AND '{stopday}' GROUP BY Date"
    cursor = connection.cursor()
    cursor.execute(re)
    res = cursor.fetchall()
    return render_template('charts.html',res = res)
    
@app.route('/table_DWMY', methods=['GET', 'POST'])
def table_DWMY():
    times = request.args.get('type')
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    date_time = datetime.fromtimestamp(timestamp)
    date_times = date_time.strftime("%Y-%m-%d,%H:%M:%S")
    day,time = date_times.split(',')
    y,m,d = day.split('-')
    connection = getConnection()
    cursor = connection.cursor()
    u = ''
    
    if times =='All':
        u = "SELECT * FROM user ORDER BY Date,user.time DESC"
    elif times =='Daily':
        u = f"SELECT * FROM user WHERE Date LIKE '%{y}-{m}-{d}' ORDER BY Date,user.time DESC"
    elif times == 'Monthly':
        u = f"SELECT * FROM user WHERE Date LIKE '%{y}-{m}-%' ORDER BY Date,user.time DESC"
    elif times == 'Yearly':
        u = f"SELECT * FROM user WHERE Date LIKE '{y}%' ORDER BY Date,user.time DESC"  
    elif times == 'Weekly':
        u = f"SELECT * FROM user WHERE week(Date) = week(now()) ORDER BY Date,user.time DESC"
        
    cursor = connection.cursor()
    cursor.execute(u)    
    user = cursor.fetchall()
    return render_template('table.html',user=user) 
    
        


@app.route('/home', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    print(username)
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    date_time = datetime.fromtimestamp(timestamp)
    date_times = date_time.strftime("%Y-%m-%d,%H:%M:%S")
    day,time = date_times.split(',')
    return render_template('index.html',username=username,day=day,time=time)

@app.route('/savecontainer', methods=['GET', 'POST'])
def savecontainer():
    username = request.args.get('username')
    day = request.args.get('day')
    time = request.args.get('time')
    container = request.args.get('container')
    print(container,username,day,time)
    connection = getConnection()
    Van01,Van02,Van03,Van04,Van05,Van06,Van07,Bus01,Bus02,Bus03 = 0,0,0,0,0,0,0,0,0,0
    if username != "" :
        if username != "None":
            if container =='Van01':
                Van01 = 1
            elif container =='Van02':
                Van02 = 1
            elif container =='Van03':
                Van03 = 1
            elif container =='Van04':
                Van04 = 1
            elif container =='Van05':
                Van05 = 1
            elif container =='Van06':
                Van06 = 1
            elif container =='Van07':
                Van07 = 1
            elif container =='Bus01':
                Bus01 = 1
            elif container =='Bus02':
                Bus02 = 1
            elif container =='Bus03':
                Bus03 = 1
            sql = "INSERT INTO user(Username, Container, Time ,Date) VALUES('%s', '%s', '%s', '%s')" % (username,
             container, time, day)
            ins = "INSERT  INTO result(Date,Van01,Van02,Van03,Van04,Van05,Van06,Van07,Bus01,Bus02,Bus03) VALUES('%s', '%s', '%s', '%s','%s', '%s', '%s', '%s','%s', '%s', '%s')" % (day,Van01,Van02,Van03,Van04,Van05,Van06,Van07,Bus01,Bus02,Bus03)
            cursor = connection.cursor()
            cursor.execute(sql)
            cursor.execute(ins)
            connection.commit()
        

    return redirect(url_for('resultsave'))


@app.route('/resultsave')
def resultsave():
    a = request.url
    print(a)
    print("tab closed")
    return render_template('index2.html')


if __name__ == '__main__':
   app.run(debug = True)