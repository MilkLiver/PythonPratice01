import pymysql


print("start")
db = pymysql.connect(
    host="127.0.0.1",
    port=1433,
    user="admin",
    passwd="Admin12345",
    db="pythonTest01")

print("test1")
cursor = db.cursor()
print("test2")
cursor.execute("DROP TABLE IF EXISTS test01")
print("test3")
sql = """CREATE TABLE test01 (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1)
         );"""


cursor.execute(sql)

db.close()
