#!/usr/local/bin/python3
#위의 것은 맥os에서 파이썬으로 이 문서를 다루라고 하는 설명
print("Content-Type: text/html")
#위의 것은 CGI 어플리케이션 구현하기 위한 =헤더
print()
#한줄을 띄운다는 뜻 or \n으로 가능
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value
print('''
<!doctype html>
<html>
<head>
  <title>Talent Exchange</title>
  <meta charset="utf-8">
  <style>
  ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
  }
  li {
  float: left;
  }
  li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  }
  li a:hover {
  background-color: #111;
  }
  .ab {
      text-align: center;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
    a {
      text-decoration: none;
    }
    h1 { font-size: 45px;
         text-align: center;
         color: white;
    }
    </style>
    </head>
    <body>
    <ul>
    <li><a href="index.py">Main</a></li>
    <li><a href="upload.py">Create</a></li>
    </ul>
    <div class="ab"> <h1><a href="create.py">Create</a></h1> </div>
    <div>
    <h2>{title}</h2>
    </div>
    </body>
    </html>
''')
