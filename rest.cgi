#!/usr/bin/python3
import cgi
import MySQLdb
import passwords
import os
import json
form = cgi.FieldStorage()

if("PATH_INFO" in os.environ):
    path_info = os.environ['PATH_INFO']
    if(path_info[1:] == "getDetails"):
        print("Content-Type: text/html")
        print("Status: 200 OK")
        print()
        print("These are the details: ")
        print("\n")
        if "iden" in form:
                iden = form["iden"].value
                name1 = "Graham"
                age1 = 29

        else:
                    iden = "1"
                    conn = MySQLdb.connect(host = passwords.SQL_HOST,
                                           user = passwords.SQL_USER,
                                           passwd = passwords.SQL_PASSWD,
                                           db = "akshiththumma")
                    cursor = conn.cursor()
                    mySql_insert = ''' INSERT INTO Details(iden,name1,age1)VALUES(2,'Graham',29)  '''

                    cursor.execute("SELECT * FROM Details")
                    
                    details = cursor.fetchall()
                    conn.commit()

                    cursor.close()
                    tot = []
                    
                    for i in details: 
                        Id = i[0]
                        name = i[1]
                        age = i[2]
                        x = {"ID" : Id,"Name" : name,"Age" :age}
                        tot.append(x)
                    x_json = json.dumps(tot, indent=2)
                    print(x_json)
    else:
        print("Content-Type: text/html")
        print("Status: 200 OK")
        print()
        print("Welcome!!!")
        print("<br>")
        print("Your path_info is " + path_info)
        print("<br>")
        print("Add 'getDetails' to your path to view results")




else:
    print("Status: 302 Redirect")
    print("Location: rest.cgi/")
    print()
    print("Welcome!!!\n")
    print("add getDetails to the path")

