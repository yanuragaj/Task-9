#!/usr/bin/python3
import cgi
import webbrowser

print("content-type: text/html")
print()


form = cgi.FieldStorage()
cmd = form.getvalue("x")

#print(cmd)

import subprocess
x=subprocess.getoutput(cmd)
#print(x)
message="""
<!Doctype html>
<html>
<head><title>OUTPUT</title></head>
<body style="color: white; 
font-family: BlinkMacSystemFont; 
font-weight: bolder; 
text-align: center;  
background-image: url('http://192.168.43.54/wp5400997.jpg'); 
background-repeat: no-repeat; 
background-attachment: fixed;   
background-size: cover;">
<h1 align="middle" style=" align-content: center;
color: white;
text-shadow: 2px 4px black;
font-weight: bolder;
width: 1350px;
height: 40px;
border-radius: 40px;
font-family: fantasy;
color: white;
text-shadow: 2px 4px black;
font-weight: bolder;
width: 1350px;
height: 40px;
border-radius: 40px;
font-family: fantasy;
background-image: url('http://192.168.43.54/xqchjntqp5451.png');
background-repeat: no-repeat;
background-attachment: fixed;  
background-size: cover; border-bottom: 6px solid white;"> OUTPUT </h1>
</br> </br>
<p align="middle" style="font-family: BlinkMacSystemFont;">{}</p>
</body>
</html>
""".format(x)
print(message)
