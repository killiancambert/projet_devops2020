import pymysql

conn = pymysql.connect(host  ="localhost",
                            user   ="root",
                            port = 3308,
                            password ='',
                            db ='testdevops')

myCursor = conn.cursor()

myCursor.execute("INSERT INTO automate(num unit, num autom, mesure ph, mesure k+) VALUES(1,1,3.5,5);")

conn.commit()
conn.close()
