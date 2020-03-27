#!/usr/local/bin/python3
#위의 것은 맥os에서 파이썬으로 이 문서를 다루라고 하는 설명
print("Content-Type: text/html")
#위의 것은 CGI 어플리케이션 구 현하기 위한 =헤더
print()
#한줄을 띄운다는 뜻 or \n으로 가능
import cgi
form = cgi.FieldStorage()
print('''
<!doctype html>
<html>
<head>
  <title>Talent Exchange</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
  <script src="https://kit.fontawesome.com/3a63b9f09e.js" crossorigin="anonymous"></script>
<style>
body {
    background-image: url(a.jpg);
    background-size: cover;
    background-position: center;
}
.a h1 {
    font-size: 2.5em;
}
.a p {
    margin-bottom: 30px;
}
.a {
   text-align: center;
   position: absolute;
   top: 50%;
   left: 50%;
   transform: translate(-50%, -50%);
   color: black;
 }
</style>
</head>
<body>
<div class="bar">
  <ul>
  <li><a href="#"><i class="fas fa-file-upload"></i>Upload</a>
    <div class="sub1">
        <ul>
        <li><a href="english.py">English</a></li>
        </ul>
    </div>
  </li>
  <li><a href="#"><i class="fas fa-file-download"></i>Download</a></li>
</ul>
<div class="a">
<h1>Talent exchange</h1>
<p id="pur">The objectives of this site is to create a virtual place to build an interactive knowledge exchange ecosystem for my fellow students and friends.</p>
</div>
  </body>
  </html>
''')
#위는 index.html을 python화 한 것
