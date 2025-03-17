import sqlite3
import requests

URL = "http://172.16.112.19:8000/login" 
html_code = requests.get(URL).text

naam  = "johnaa.qs"
query = f"SELECT UserId, Name, Password FROM Users WHERE UserId = 105 or 1=1"
account = sqlite3.executequery(query)
