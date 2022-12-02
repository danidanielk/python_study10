# Final - 메뉴 만들기
from cx_Oracle import connect
from pickle import NONE

# 1. 학생등록
# 2. 강의장 조회
# 3. 학생 조회
# 4. 학생정보 파일로 내보내기
# 0. 종료


def showMenu():
    print("1. 학생 등록")
    print("2. 강의장 조회")
    print("3. 학생 조회")
    print("4. 학생정보 파일로 내보내기")
    print("0. 종료")
    print("--------------------")
    return input("번호 입력 : ")

#학생등록
def regStudent():
    name=input("이름: ")
    bd=input("생일(YYYYMMDD): ")
    classroom= int(input("강의장: "))
    mid = int(input("중간고사 점수: "))
    fin = int(input("기말고사 점수: "))
    
    con=connect("danieldb/1@192.168.123.102:1521/xe")
    cur=con.cursor()
    sql=f"insert into student_1115 values(student_1115_seq.nextval,'{name}',to_date('{bd}','yyyymmdd'),{classroom},{mid},{fin})"
    cur.execute(sql)
    if cur.rowcount==1:
        print("success")
        con.commit()
    con.close()


#강의장 조회
def selectroom():
    n=int(input("조회하실 강의장 번호: "))
    con=connect("danieldb/1@192.168.123.102:1521/xe")
    sql=f"select * from room_1115 where r_no={n}"
    cur=con.cursor()
    cur.execute(sql)
    for i,ii in cur:
        print("-------------")
        print(i,ii)
        print("-------------")
    con.close()
    

#학생 조회
def selectStudent():
    n=input("이름을 입력해주세요: ")
    con=connect("danieldb/1@192.168.123.102:1521/xe")
    sql=f"select * from student_1115 where s_name='{n}'"
    cur=con.cursor()
    cur.execute(sql)
    for i in cur:
        print(i)
    con.close()
 
    
#학생정보 전체를 csv 파일로 내보내기.
def write():
    file = open("C:/Users/NT731QCJ-K582D/Desktop/test/pythonFile/test7.csv","a",encoding="UTF-8")
    con=connect("danieldb/1@192.168.123.102:1521/xe")
    sql="select * from student_1115"
    cur=con.cursor()
    cur.execute(sql)
    for i,ii,iii,iiii,iiiii,iiiiii in cur:
        file.write(f"번호:{i}\n이름:{ii}\n생년월일:{iii}\n강의장번호:{iiii}\n중간고사점수:{iiiii}\n기말고사점수:{iiiiii}\n------------")
    con.close()
    file.close()    
    
    
def start(menu):
    while True:
        menu=showMenu()
        if menu=="1":
            regStudent()
        elif menu=="2":
            selectroom()
        elif menu=="3":
            selectStudent()
        elif menu=="4":
            write()
        elif menu=="0":
            break


        
menu=None
start(menu)