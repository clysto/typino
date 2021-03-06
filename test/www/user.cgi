#!/usr/bin/env python3

import os
from urllib.parse import parse_qsl

query_string = os.environ["QUERY_STRING"]
query = dict(parse_qsl(query_string))
if "name" in query:
    name = query["name"]
else:
    name = "unknowed"

print("Server: simple-httpd/0.0.1")
print("Content-Type: text/html")
print("\n\n", end="")
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("</head>")
print("<body>")
print(f"<h1>Hello {name}</h1>")
print("</body>")
print("</html>")
