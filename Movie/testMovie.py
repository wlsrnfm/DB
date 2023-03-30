from unittest import result
import pymysql

con = pymysql.connect(host='localhost',
                      user='root',
                      password='dhkfk1004',
                      db='mydb',
                      charset='utf8')

cursorObject = con.cursor()

print('=======================================')
print('(0) 종료')
print('(1) 릴레이션 생성 및 데이터 추가')
print('(2) 제목을 이용한 검색')
print('(3) 관객수를 이용한 검색')
print('(4) 개봉일을 이용한 검색')
print('=======================================')
n = int(input('원하는 번호를 입력하시오 '))

if(n == 0):
    print("프로그램 종료.")
    exit()
    
if(n == 1):
    m = int(input('원하는 기능을 선택하세요(1: 릴레이션 생성 2: 데이터 추가)'))
    if(m == 1):
        f = open("create_table.txt")
        
        query1 = ''
        while True:
            line = f.readline()
            if not line: break
            a = str(line)
            query1 = query1 + a
        f.close()
        cursorObject.execute(query1)
        result = cursorObject.fetchall()
        print("테이블 생성이 완료되었습니다.")
        
    if(m == 2):
        fp = open("movie_data.txt", "r", encoding='euc-kr')

        for line in fp.readlines():
            valueList = line.strip().split("\t")
            
            query1_2 = "Insert into movie values ("
        
            for curValue in valueList:
                if (len(curValue) > 255):
                    curValue = curValue[0:255]
                query1_2  = query1_2 + "'" + curValue + "', "
                query1_2 = query1_2.replace("|", "','")
                query1_2 = query1_2.replace("('',", "(")
    
            query1_2 = query1_2[0:len(query1_2) -2] + ")"
            result = cursorObject.execute(query1_2)
        fp.close
        print("데이터 입력이 완료되었습니다.")
        

if(n == 2):
    c = input("사용자 입력(제목): ")

    query2_1 = "select * from movie where title like "
    query2_2 = "'%"+c+"%'"
    query2 = query2_1 + query2_2
    cursorObject.execute(query2)
    result = cursorObject.fetchall()
    print(result)
        
if(n == 3):
    i = input("사용자 입력(관객수): ")

    query3 = "select * from movie where totalnum >= " + i
    cursorObject.execute(query3)
    result = cursorObject.fetchall()
    print(result)
    
if(n == 4):
    a = input("사용자 입력(시작)0000-00-00: ")
    b = input("사용자 입력(끝)0000-00-00:")
    
    query4 = "select * from movie where releasedate >= " + "'"+a+"'" + "and releasedate <= " + "'"+b+"'" 
    cursorObject.execute(query4)
    result = cursorObject.fetchall()
    print(result)

con.commit()
con.close()