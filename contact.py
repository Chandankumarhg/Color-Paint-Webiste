#!C:\Users\sinne\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10\python.exe
print("Content-Type:text/html")
print()
import cgi


print("<h1>Welcome</h1>")
print("<hr/>")
print("<h1>Using input tag</h1>")
print("<body bgcolor='red'>")

form=cgi.FieldStorage()

name = form.getvalue("name","Chandan")
email = form.getvalue("email","Chadan@gmail.com")
subject = form.getvalue("subject","HELLO")
message = form.getvalue("message","good morning")    

import mysql.connector

con = mysql.connector.connect(user='root',password='',host='localhost',database='ContactForm')
cur = con.cursor()

cur.execute("insert into contactform values(%s,%s,%s,%s)",(name,email,subject,message))
con.commit()

cur.close()
con.close()

print("<h3>record inserted succesfully</h3>")

