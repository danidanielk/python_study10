from cx_Oracle import connect

file= open("C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/test6.csv","a",encoding="UTF-8")


con = connect("danieldb/1@192.168.123.102:1521/xe")
cur = con.cursor()

sql="select * from weather__15"
cur.execute(sql)

for i,ii,iii in cur:
    file.write(f"{i},{ii},{iii}\n")


con.close()
file.close()
print("success")