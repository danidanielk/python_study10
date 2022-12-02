#서울 데이터광장 -> 미세먼지 검색 -> 공공데이터탭 -> 서울시 권역별 실시간 대기환경 현황
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
from cx_Oracle import connect
from json import loads

#첫번째 URL 긁어옴 http://openAPI.seoul.go.kr:8088/(인증키)/xml/RealtimeCityAir/1/25/
#인증키 = 4f626857416f6c6c3632586a416843

# xml-> json 으로 바꿈 
# http://openAPI.seoul.go.kr:8088/4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/25/

hc=HTTPConnection("openAPI.seoul.go.kr:8088")
hc.request("GET", "/4f626857416f6c6c3632586a416843/json/RealtimeCityAir/1/25/")
resbody=hc.getresponse().read()
# print(resbody.decode())
weather=loads(resbody)
# weather=fromstring(resbody).iter()  이건 xml 파싱할때 json은 loads로

con=connect("danieldb/1@192.168.123.102:1521/xe")
cur = con.cursor()


# a=weather["RealtimeCityAir"]["row"]["MSRSTE_NM"]
# b=weather["RealtimeCityAir"]["row"]["PM10"]
# c=weather["RealtimeCityAir"]["row"]["PM25"]

for i in weather["RealtimeCityAir"]["row"]:
    sql="insert into weather__15 values('%s',%2f,%2f)"%(i["MSRSTE_NM"],i["PM10"],i["PM25"])
    cur.execute(sql)
 
print("success")
con.commit()
con.close()
