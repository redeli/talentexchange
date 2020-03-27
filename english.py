#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
else:
    pageId = 'Welcome'
print('''<!doctype html>
<html>
<head>
  <title>English</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="bar">
    <ul>
        <li><a href="index.py">Main</a></li>
    </ul>
    </div>
    <div class="contents_english">
    <ul>
        <li><a href="english.py?id=Wonder">Wonder</a></li>
        <li><a href="english.py?id=HarryPotter">Harry Potter</a></li>
    </ul>
        <div class="article_english">
            <h2>{title}</h2>
            <p> simon says </p>
        </div>
    </div>
</body>
</html>
'''.format(title=pageId))
# - problem with pageId identifying
