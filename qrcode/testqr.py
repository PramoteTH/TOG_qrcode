import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode
import cv2
import pymysql

def getConnection ():
    return pymysql.connect(
        host = 'localhost',
        db = 'qrcode',
        user = 'root',
        password = '',
        charset = 'utf8',
        cursorclass = pymysql.cursors.DictCursor
		)
    
connection = getConnection()
sql = "SELECT * FROM employee"
cursor = connection.cursor()
cursor.execute(sql)
em = cursor.fetchall()

user = []

for x in em:
  a =str(x.get('user'))
  user.append(a)

# id = ["S650002","S650003","S650004"]
url = "https://d0e1-119-76-14-208.ap.ngrok.io"

for i in range(len(user)):
    qr = pyqrcode.create(url+"/home?username="+user[i])
    qr.png(""+user[i]+".png", scale=6)
    
    

